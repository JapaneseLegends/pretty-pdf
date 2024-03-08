from src.adapters.PdfBuilderAdapter import PdfBuilderAdapter
from src.adapters.TemplateEngineAdapter import TemplateEngineAdapter
from src.services.PdfService import PdfService
from src.services.TemplateService import TemplateService
from src.utils.data import open_json
# types
from typing import Any, TypedDict, Optional
from typing_extensions import NotRequired

class TemplateOptions(TypedDict):
    template_path: str
    json_path: NotRequired[str]
    output_path: str


class LibController():
    def __init__(self):
        self.pdfBuilder = PdfBuilderAdapter()
        self.templateEngine = TemplateEngineAdapter()
        self.pdfService = PdfService(self.pdfBuilder)
        self.templateService = TemplateService(self.templateEngine)

    def __open_template(self, path: str) -> str:
        with open(path, 'r') as file:
            return file.read()

    def __load_json(self, path: Optional[str]) -> dict[str, Any] | list[Any]:
        return {} if not path else open_json(path)

    def generate(self, options: TemplateOptions) -> None:
        template = self.__open_template(options['template_path'])

        json_path = options.get("json_path", None)
        
        html = self.templateService.render({
            'template': template,
            'data': { "json": self.__load_json(json_path) }
        })

        blob = self.pdfService.create(html) 

        with open(options['output_path'], 'wb') as file:
            file.write(blob)