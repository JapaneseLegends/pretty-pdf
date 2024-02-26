from os import path, mkdir
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
from utils.console import print_error, print_info, print_warning, print_success
import json
from interfaces.objects import TemplateRenderOptions
from interfaces.aliases import html_template
from interfaces import JinjaAdapter


class TemplateRenderService(object):
    def __init__(self, adapter: JinjaAdapter):
        self.adapter = adapter
    
    def __extract_basedir(self, options) -> str:
        return options.get('baseDir', '')

    def __extract_path_list(callback, options) -> list[str]:
        return [
            options.get('templatePath', ''),
            options.get('jsonPath', ''),
            options.get('envPath', ''),
            options.get('stylesheetPath', '')
        ]
    
    def __extract_data(self, options) -> dict:
        return options.get('templateData', {})

    def __handle_path_list (self, base_dir: str, path_list: list[str]) -> str:
        if not base_dir:
            return path_list

        print_info(f"Creating base directory '{base_dir}'...")
        return [path.join(base_dir, x) for x in path_list if x]

    def render(self, options) -> html_template:
        base_dir = self.__extract_basedir(options)
        path_list = self.__extract_path_list(options)
        data = self.__extract_data(options)

        template_path, json_path, env_path, stylesheet_path = \
            self.__handle_path_list(base_dir, path_list)

        self.adapter.set_template(template_path)
        self.adapter.set_json(json_path)
        self.adapter.set_env(env_path)
        self.adapter.set_stylesheet(stylesheet_path)
        self.adapter.set_data(data)

        return self.adapter.render()
    