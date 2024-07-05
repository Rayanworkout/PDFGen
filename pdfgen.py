import os
import json
import argparse

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

class PDFGenerator:
    def __init__(self, template_name: str = None, verbose: bool = False) -> None:
        
        self.template_name = template_name
        self.verbose = verbose
        
        self.template_folder = 'templates'
        
        if not os.path.exists(self.template_folder):
            print(f'> Creating folder "{self.template_folder}"')
            os.makedirs(self.template_folder)
        
        if self.template_name is None:
            self.template_path = self.__get_default_template()
            
            if self.verbose:
                print(f'> Template name not provided, falling back to "{self.template_path}"')
                
        else:
            if not self.template_name.endswith('.html'):
                self.template_name = f'{self.template_name}.html'
                
            self.template_path = os.path.join(self.template_folder, self.template_name)
            
            if not os.path.exists(self.template_path):
                raise FileNotFoundError(f'Template file "{self.template_path}" not found.')

    def generate_pdf(self, output_filename) -> None:
        
        if output_filename is None:
            self.output_path = 'output.pdf'
        else:
            if not output_filename.endswith('.pdf'):
                output_filename = f'{output_filename}.pdf'
                
            self.output_path = output_filename
            
            
        file_loader = FileSystemLoader(self.template_folder)
        env = Environment(loader=file_loader)
        template = env.get_template(self.template_name)
        
        css_file = [f for f in os.listdir(self.template_folder) if f.endswith('.css')]
        
        if css_file:
            style = css_file[0]
            css_path = os.path.join(self.template_folder, style)
            css = [CSS(filename=css_path)]
            
            if self.verbose:
                print(f"> Using CSS: {style}")
                
        else:
            css = None
            if self.verbose:
                print("> No CSS file found.")

        # Render HTML
        template_vars = self.__load_template_vars()
            
        html_output = template.render(template_vars)

        HTML(string=html_output).write_pdf(self.output_path, stylesheets=css)
        
        print(f'> Successfully created "{self.output_path}".')
        exit(0)
    
    
    def __get_default_template(self) -> str | FileNotFoundError:
        template_files = [f for f in os.listdir(self.template_folder) if f.endswith('.html')]
        
        if not template_files:
            raise FileNotFoundError(f'No HTML file found in "{self.template_folder}".\nPlease create an html file in the templates folder.')
        else:
            self.template_name = template_files[0]
            
            return os.path.join(self.template_folder, self.template_name)
            
    def __load_template_vars(self, template_vars_file: str = "demo_vars.json") -> dict | FileNotFoundError:
        
        if not os.path.exists(template_vars_file):
            
            json_files = [f for f in os.listdir() if f.endswith('.json')]
            
            if json_files:
                template_vars_file = json_files[0]
                print(f'> "demo_vars.json" not found. Falling back to "{template_vars_file}".')
            
            else:
                raise FileNotFoundError(f'No template vars file found. Please create a JSON file with template variables.')                
                        
        if not template_vars_file.endswith('.json'):
            template_vars_file = f'{template_vars_file}.json'
        
        with open(template_vars_file, 'r') as f:
            template_vars = json.load(f)
            
        return template_vars
    
    def __repr__(self):
        return f'PDFGenerator(template_name="{self.template_name}", verbose={self.verbose})'

if __name__ == '__main__':
    
    # https://docs.python.org/3/library/argparse.html

    parser = argparse.ArgumentParser(prog="PDFGen", description="Easily generate PDFs from HTML templates using Jinja2 and Weasy> .")

    # DEMO MODE
    parser.add_argument("--demo", "-d", help="Run the demo to generate a sample PDF.", action="store_true", default=False)
    
    # VERBOSE MODE
    parser.add_argument("--verbose", "-v", help="Enable verbose mode.", action="store_true", default=False)
    
    # TEMPLATE NAME
    parser.add_argument("--template", "-t", help="Name of the template file.", type=str)
    
    # OUTPUT FILE
    parser.add_argument("--output", "-o", help="Name of the output file.", type=str)

    args = parser.parse_args()

    if args.demo is True:
        gen = PDFGenerator(verbose=args.verbose)
        
        gen.generate_pdf(output_filename="demo.pdf")
        
    else:
        gen = PDFGenerator(template_name=args.template, verbose=args.verbose)
        gen.generate_pdf(output_filename=args.output)