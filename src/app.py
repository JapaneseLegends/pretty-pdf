#!/usr/bin/env python3
from TemplateRender import TemplateRender
from PdfGenerator import PdfGenerator

def main():
    template = TemplateRender({
        'templatePath': 'templates/index.html',
        'jsonPath': 'data.json'
    })

    html = template.render()
    pdf = PdfGenerator(html)
    
    pdf.save('output/result.pdf')

if __name__ == '__main__':
    main()