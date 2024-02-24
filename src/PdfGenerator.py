from weasyprint import HTML
from interfaces.aliases import html_template
from utils.console import print_info, print_success, print_warning
from os import path, mkdir, chdir

class PdfGenerator(object):
    def __init__(self, template: html_template) -> None:
        print_info("Creating PDF from HTML template...")
        self.html = HTML(string=template)

    def save(self, filename: str) -> None:
        dirname = path.dirname(filename)

        if not path.exists(dirname):
            print_warning(f"Directory '{dirname}' does not exist. Creating it...")
            mkdir(dirname)

        if path.isfile(filename):
            print_warning(f"File '{filename}' already exists. Overwriting it...")

        print_info(f"Writing PDF into file...")
        self.html.write_pdf(filename)       
        
        print_success(f"PDF file saved as '{filename}'.")

