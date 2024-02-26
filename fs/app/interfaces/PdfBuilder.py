from abc import ABC, abstractmethod

class PdfBuilder(ABC):
    @abstractmethod
    def set_template(self, template_path: str) -> None:
        pass

    @abstractmethod
    def save(self, filename: str) -> None:
        pass
