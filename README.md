# Xircuits PDF Processing Components

A collection of Xircuits components for working with PDF files using PyMuPDF (fitz). This library provides components for extracting text, rendering pages to images, and getting basic PDF information.

## Components

### PDFExtractAllPagesText
Extracts text from all pages in a PDF file.
- Input: `pdf_path` (string) - Path to the PDF file
- Output: `pages` (list) - List of extracted text from each page

### PDFExtractPageText
Extracts text from a specific page in a PDF file.
- Input: 
  - `pdf_path` (string) - Path to the PDF file
  - `page_number` (integer) - Page number to extract (0-based index)
- Output: `extracted_text` (string) - Text content of the specified page

### PDFGetPageCount
Gets the total number of pages in a PDF file.
- Input: `pdf_path` (string) - Path to the PDF file
- Output: `num_pages` (integer) - Total number of pages

### PDFRenderPageToImage
Renders a specific page of a PDF to a PNG image.
- Input:
  - `pdf_path` (string) - Path to the PDF file
  - `page_number` (integer) - Page number to render (0-based index)
- Output: `image_path` (string) - Path to the saved PNG image

## Prerequisites

This component library requires:
- Python 3.6 or higher
- PyMuPDF (fitz) library

## Installation

To use this component library, ensure you have Xircuits installed, then run:

```bash
xircuits install https://github.com/XpressAI/xai-pdf
```

Alternatively, you may manually copy the directory / clone or submodule the repository to your working Xircuits project directory then install the packages using:

```bash
pip install -r requirements.txt
```

## Usage Example

1. Import the components into your Xircuits workflow
2. Connect components to process PDF files:
   - Use PDFGetPageCount to determine the number of pages
   - Extract text from specific pages with PDFExtractPageText
   - Get all text content using PDFExtractAllPagesText
   - Convert pages to images using PDFRenderPageToImage

Note: Page numbers in all components are 0-based (i.e., the first page is page 0).
