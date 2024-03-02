from src.services.interfaces.PdfBuilder import PdfBuilder

class PdfService:
    def __init__(self, adapter: PdfBuilder):
        self.adapter = adapter

    def create(self, template: str, output_path: str) -> None:
        self.adapter.set_template(template)
        self.adapter.save(output_path)