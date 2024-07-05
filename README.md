# PDFGen

A simple tool to generate PDFs from HTML templates using Jinja2.

This can be used to generate invoices, reports, rent receipts, etc.

Supports everything a regular html/css page would support, including bootstrap, tailwind, images, tables, etc.


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

Then run the script with the example template:

```bash
python3 pdfgen.py --demo

# or if you want to use your own template without providing arguments

python3 pdfgen.py
```

Using the naked command will generate a pdf file named `output.pdf` using any html file found in the `templates` directory.

The variables of your template must be defined inside a json file in the root directory.

## Usage

```bash
python3 pdfgen.py --template <path_to_template> --output <output_file>
```

You can also use the `--verbose` flag to have more information about the process.