# Usage

This section covers how to use the PDF Text Digitizer tool.

## Installation

First, clone the repository and install the required dependencies:

```shell
git clone https://github.com/yourusername/pdf-text-digitizer.git
cd pdf-text-digitizer
pip install -r requirements.txt
```

## Basic Usage

To extract text from a PDF, you can use the following script:

```python
from pdf_text_digitizer.digitize import digitize_pdf

text = digitize_pdf('path/to/your/pdf_file.pdf')
print(text)
```

## Examples

You can find example usage in the examples directory. To run the example:

```sh
python examples/example_usage.py
```
