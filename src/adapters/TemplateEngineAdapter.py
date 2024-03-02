from src.services.interfaces.TemplateEngine import TemplateEngine
from jinja2 import Environment, BaseLoader
from os import path
# types
from typing import Any


class TemplateEngineAdapter(TemplateEngine):
    def __init__(self):
        self.template = ""
        self.data = {}

    def set_template(self, template: str) -> TemplateEngine:
        self.template = template
        return self

    def set_data(self, data: dict[str, Any]) -> TemplateEngine:
        self.data = data
        return self

    def render(self) -> str:
        env = Environment(loader=BaseLoader()).from_string(self.template)
        return env.render(self.data)

