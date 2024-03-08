#!/usr/bin/env python3
from controllers.LibController import LibController

def main():
    controller = LibController()
    controller.generate({
        'template_path': 'artifacts/template.html',
        # 'json_path': 'artifacts/data.json',
        'output_path': 'artifacts/output.pdf'
    })

if __name__ == '__main__':
    main()