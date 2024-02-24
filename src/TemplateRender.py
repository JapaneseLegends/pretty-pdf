from os import path
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
from utils.console import print_error, print_info, print_warning, print_success
import json
from interfaces.objects import TemplateRenderOptions
from interfaces.aliases import html_template

class TemplateRender(object):
    def __init__(self, options: TemplateRenderOptions):
        self.basedir = path.dirname(options.get('templatePath', ''))
        self.filename = path.basename(options.get('templatePath', ''))

        self.jsonpath = options.get('jsonPath', '')
        self.renderdata = options.get('templateData', {})

    def __load_json(self, filepath: str):
        print_info(f"Loading JSON data from '{self.jsonpath}'...")

        try:
            with open(filepath, 'r') as file:
                return json.load(file)

        except FileNotFoundError:
            print_error(f"File '{filepath}' not found.")
            exit(1)
        
        except json.JSONDecodeError:
            print_error(f"File '{filepath}' is not a valid JSON file.")
            exit(1)

    def __merge_json(self, json_data: dict):
        self.renderdata = {**self.renderdata, "json": json_data}
        print_warning(f"JSON data merged. You can access it in the template using 'json' variable.")

    
    def render(self) -> html_template:
        try:
            env = Environment(loader=FileSystemLoader(self.basedir))
            template = env.get_template(self.filename)

            if self.jsonpath:
                json_data = self.__load_json(self.jsonpath)
                self.__merge_json(json_data)

            if not self.renderdata:
                print_warning(f"Template data was not provided.")

            print_info(f"Rendering template '{self.filename}'.")
    
            render = template.render()
            print_info(f"Template '{self.filename}' rendered successfully.")
    
            return render
    

        except TemplateNotFound:
            print_error(f"Template '{self.filename}' not found in directory '{self.basedir}'")
