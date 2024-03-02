#!/usr/bin/env python3
from services.TemplateRender import TemplateRender
from services.PdfGenerator import PdfGenerator

def main():
    template = TemplateRender({
        'templatePath': 'artifacts/templates/index.html',
        'jsonPath': 'artifacts/data.json'
    })

    html = template.render()
    pdf = PdfGenerator(html)

    pdf.add_stylesheet('artifacts/styles/pdf.css')
    pdf.save('artifacts/output.pdf')

if __name__ == '__main__':
    main()