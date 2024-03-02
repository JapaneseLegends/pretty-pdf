from src.services.interfaces.PdfBuilder import PdfBuilder

class PdfService:
    def __init__(self, adapter: PdfBuilder):
        self.adapter = adapter

    def create(self, template: str) -> bytes:
        self.adapter.set_template(template)
        return self.adapter.save()