#!/usr/bin/env python3
from src.controllers.GenerationController import PdfGenerationController

def main():
    controller = PdfGenerationController()
    controller.generate({
        'template_path': 'artifacts/template.html',
        'json_path': 'artifacts/data.json',
        'output_path': 'artifacts/output.pdf'
    })

if __name__ == '__main__':
    main()