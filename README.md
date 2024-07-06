# HTML to PDF Generator

A simple CLI tool to generate PDFs from standard HTML files or Jinja2 templates.

_Jinja is a templating language for Python that allows you to easily use variables, loops, and conditions in your HTML files._

This tool can be used to generate invoices, reports, rent receipts ...

Just clone the repo, create your html file inside the `templates` directory and run the script.

You can also add a css file along with your html file.


## Installation

```bash
git clone https://github.com/Rayanworkout/PDFGen.git
```

## Quick Start

First create a virtual environment and install the dependencies:
```bash
cd PDFGen
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then put the html you want to convert to pdf in the `templates` directory and run the script:

```bash
python3 pdfgen.py
```

You can also specify the name of the output file:

```bash
python3 pdfgen.py my_output.pdf

# or simply

python3 pdfgen.py my_output
```

It will generate a pdf file named `my_output.pdf` using any html file found in the `templates` directory.

The variables of your template must be defined inside a json file in the root directory.

By default, the file is named `template_vars.json` but you can name it as you want.


Feel free to contribute and improve the tool.