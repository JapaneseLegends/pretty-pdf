from weasyprint import HTML
from src.services.interfaces.PdfBuilder import PdfBuilder

class PdfBuilderAdapter(PdfBuilder):
    def __init__(self):
        self.html = None

    def set_template(self, template: str):
        self.html = HTML(string=template)
        return self

    def save(self) -> bytes:
        if self.html is None:
            raise Exception('Template not set')

        return self.html.write_pdf() or b''