from typing import Any, Dict
from abc import ABC, abstractmethod

class TemplateEngine(ABC):
    @abstractmethod
    def set_template(self, template_path: str):
        pass

    @abstractmethod
    def set_data(self, data: Dict[str, Any]):
        pass

    @abstractmethod
    def render(self):
        pass

