# types
from typing import Any, TypedDict
from src.services.interfaces.TemplateEngine import TemplateEngine

class TemplateServiceOptions(TypedDict):
    template_path: str
    data: dict[str, Any]

class TemplateService(object):
    def __init__(self, adapter: TemplateEngine):
        self.adapter = adapter

    def __check_template_options(self, options: TemplateServiceOptions):
        if options.get('template_path'): return
        raise ValueError('Template path is required')
        
    def render(self, options: TemplateServiceOptions):
        self.__check_template_options(options)

        self.adapter.set_template(options['template_path'])
        self.adapter.set_data(options['data'])

        return self.adapter.render()
    
    