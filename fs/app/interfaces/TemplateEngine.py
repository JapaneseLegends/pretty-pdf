from typing import Any, Dict, List
from abc import ABC, abstractmethod

class TemplateEngine(ABC):
    @abstractmethod
    def set_template(self, template_path: str) -> None:
        pass

    @abstractmethod
    def set_data(self, data: Dict[any]) -> None:
        pass

    @abstractmethod
    def set_json(self, json_path: str) -> None:
        pass

    @abstractmethod
    def set_env(self, env_path: str) -> None:
        pass

    @abstractmethod
    def set_stylesheet(self, stylesheet_path: str) -> None:
        pass

    @abstractmethod
    def render(self) -> str:
        pass

