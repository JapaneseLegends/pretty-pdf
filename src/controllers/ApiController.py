from src.adapters.PdfBuilderAdapter import PdfBuilderAdapter
from src.adapters.TemplateEngineAdapter import TemplateEngineAdapter
from src.services.PdfService import PdfService
from src.services.TemplateService import TemplateService
from base64 import b64encode, b64decode
# types
from typing import TypedDict, Optional

class TemplateOptions(TypedDict):
    html: str
    css: Optional[str]
    data: Optional[dict | list]


class ApiController():
    def __init__(self):
        self.pdfBuilder = PdfBuilderAdapter()
        self.templateEngine = TemplateEngineAdapter()
        self.pdfService = PdfService(self.pdfBuilder)
        self.templateService = TemplateService(self.templateEngine)

    def generate(self, options: TemplateOptions) -> str:
        template = options['html']
        data = options['data']
        
        html = self.templateService.render({
            'template': template,
            'data': { "data": data }
        })

        blob = self.pdfService.create(html)
        b64 = b64encode(blob)

        return b64.decode('utf-8')
