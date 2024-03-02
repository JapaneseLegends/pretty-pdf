from src.adapters.PdfBuilderAdapter import PdfBuilderAdapter
from src.adapters.TemplateEngineAdapter import TemplateEngineAdapter
from src.services.PdfService import PdfService
from src.services.TemplateService import TemplateService
import json
# types
from typing import Any, TypedDict, Optional

class TemplateOptions(TypedDict):
    template_path: str
    json_path: str
    output_path: str


class PdfGenerationController():
    def __init__(self):
        self.pdfBuilder = PdfBuilderAdapter()
        self.templateEngine = TemplateEngineAdapter()
        self.pdfService = PdfService(self.pdfBuilder)
        self.templateService = TemplateService(self.templateEngine)

    def __open_template(self, path: str) -> str:
        with open(path, 'r') as file:
            return file.read()

    def __open_json(self, path: str) -> dict[str, Any] | list[Any]:
        with open(path, 'r') as file:
            return json.load(file)

    def generate(self, options: TemplateOptions) -> None:
        template = self.__open_template(options['template_path'])
        data = self.__open_json(options['json_path'])

        html = self.templateService.render({
            'template': template,
            'data': { "json": data }
        })

        self.pdfService.create(html, options.get('output_path')) 