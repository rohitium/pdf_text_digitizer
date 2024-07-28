# API Reference

## digitize_pdf

```python
digitize_pdf(file_path: str) -> str
```

Extracts text from a PDF file. If the PDF is text-based, it extracts the text directly. If the PDF is image-based, it uses OCR to extract text from images.

### Parameters

file_path (str): The path to the PDF file.

### Returns

str: The extracted text.

## extract_text_from_pdf

```python
extract_text_from_pdf(file_path: str) -> str
```

Extracts text from a text-based PDF file.

### Parameters

file_path (str): The path to the PDF file.

### Returns

str: The extracted text.

## extract_text_from_pdf_images

```python
extract_text_from_pdf_images(file_path: str) -> str
```

Extracts text from an image-based PDF file using OCR.

### Parameters

file_path (str): The path to the PDF file.

### Returns

str: The extracted text.
