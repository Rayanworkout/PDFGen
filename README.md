# PDFGen

A simple CLI tool to generate PDFs from standard HTML files or Jinja2 templates.

Jinja is a templating language for Python that allows you to easily use variables, loops, and conditions in your HTML files.

This tool can be used to generate invoices, reports, rent receipts, etc.

Just clone the repo, create your html file inside the `templates` directory and run the script.

You can also add a css file along with your html file.


## Installation

```bash
git clone https://github.com/Rayanworkout/PDFGen.git

cd PDFGen
```

## Quick Start

First create a virtual environment and install the dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run the script either in demo mode or with your own template:

```bash
python3 pdfgen.py --demo

# or

python3 pdfgen.py --template invoice.html --output invoice.pdf
```

You can also simply use the command without any arguments:

```bash
python3 pdfgen.py
```

It will generate a pdf file named `output.pdf` using any html file found in the `templates` directory.

The variables of your template must be defined inside a json file in the root directory.

## Usage

```bash
python3 pdfgen.py --template <path_to_template> --output <output_file> --verbose
```

The `--verbose` flag allows to have more information about the process.

Feel free to contribute and improve the tool.