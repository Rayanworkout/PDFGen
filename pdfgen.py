import os
import json
import sys

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS


class PDFGenerator:
    def __init__(self) -> None:
        """
        Gather the necessary information to generate the PDF.
        """
        self.template_folder = "templates"

        if not os.path.exists(self.template_folder):
            print(f'> Creating folder "{self.template_folder}"')
            os.makedirs(self.template_folder)

        self.template_name = self.__get_default_template()

        if not self.template_name.endswith(".html"):
            self.template_name = f"{self.template_name}.html"

        self.template_path = os.path.join(self.template_folder, self.template_name)

    def generate_pdf(self, output_filename: str = "output.pdf") -> None:

        if not output_filename.endswith(".pdf"):
            output_filename = f"{output_filename}.pdf"

        file_loader = FileSystemLoader(self.template_folder)
        env = Environment(loader=file_loader)
        template = env.get_template(self.template_name)

        css_file = [f for f in os.listdir(self.template_folder) if f.endswith(".css")]

        if css_file:
            style = css_file[0]
            css_path = os.path.join(self.template_folder, style)
            css = [CSS(filename=css_path)]

            print(f"> Using CSS: {style}")

        else:
            css = None
            print("> No CSS file found.")

        # Render HTML
        template_vars = self.__load_template_vars()

        html_output = template.render(template_vars)

        HTML(string=html_output).write_pdf(output_filename, stylesheets=css)

        print(f'> Successfully created "{output_filename}".')
        exit(0)

    def __get_default_template(self) -> str | FileNotFoundError:
        template_files = [
            f for f in os.listdir(self.template_folder) if f.endswith(".html")
        ]

        if not template_files:
            raise FileNotFoundError(
                f'No HTML file found in "{self.template_folder}".\nPlease create an html file in the templates folder.'
            )
        else:
            self.template_name = template_files[0]

            return self.template_name

    def __load_template_vars(
        self, template_vars_file: str = "template_vars.json"
    ) -> dict | FileNotFoundError:

        if not os.path.exists(template_vars_file):

            json_files = [f for f in os.listdir() if f.endswith(".json")]

            if json_files:
                template_vars_file = json_files[0]
                print(
                    f'> "template_vars.json" not found. Falling back to "{template_vars_file}".'
                )

            else:
                raise FileNotFoundError(
                    f"No template vars file found. Please create a JSON file with template variables."
                )

        if not template_vars_file.endswith(".json"):
            template_vars_file = f"{template_vars_file}.json"

        with open(template_vars_file, "r") as f:
            template_vars = json.load(f)

        return template_vars


if __name__ == "__main__":

    gen = PDFGenerator()
    args = sys.argv

    if len(args) > 1:
        output_filename = args[1].strip()
        gen.generate_pdf(output_filename)
    else:
        gen.generate_pdf()
