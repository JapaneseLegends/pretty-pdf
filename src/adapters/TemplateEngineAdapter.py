from typing import Any, TypeVar
from src.services.interfaces.TemplateEngine import TemplateEngine
from jinja2 import Environment, FileSystemLoader


class TemplateEngineAdapter(TemplateEngine):
    def __init__(self):
        self.template = ""
        self.data = {}

    def set_template(self, template_path: str) -> TemplateEngine:
        self.template = template_path
        return self

    def set_data(self, data: dict[str, Any]) -> TemplateEngine:
        self.data = data
        return self

    def render(self) -> str:
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(self.template)
        
        return template.render(self.data)

