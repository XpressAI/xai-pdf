from xai_components.base import InArg, InCompArg, OutArg, Component, xai_component, InCompArg

import fitz  # PyMuPDF library for working with PDF files


@xai_component
class PDFExtractAllPagesText(Component):
    pdf_path: InCompArg[str]
    pages: OutArg[list]
    
    def execute(self, ctx) -> None:
        ret = []
        pdf_document = fitz.open(self.pdf_path.value)

        num_pages = pdf_document.page_count

        for i in range(0, num_pages):
            page = pdf_document[i]
            text = page.get_text()
            ret.append(text)
        
        self.pages.value = ret
        
        pdf_document.close()
        
        
@xai_component
class PDFExtractPageText(Component):
    pdf_path: InCompArg[str]
    page_number: InCompArg[int]
    extracted_text: OutArg[str]
    
    def execute(self, ctx) -> None:
        pdf_document = fitz.open(self.pdf_path.value)
        
        if self.page_number.value < 0 or self.page_number.value >= pdf_document.page_count:
            print("Invalid page number. Please provide a valid page number.")
            return None
        
        page = pdf_document[self.page_number.value]
        text = page.get_text()
        print("PDFExtractPageText:")
        print(text)
        
        self.extracted_text.value = text
        
        pdf_document.close()


@xai_component
class PDFGetPageCount(Component):
    pdf_path: InCompArg[str]
    num_pages: OutArg[int]
    
    def execute(self, ctx) -> None:
        pdf_document = fitz.open(self.pdf_path.value)
        
        num_pages = pdf_document.page_count
        
        self.num_pages.value = num_pages
        
        pdf_document.close()


@xai_component
class PDFRenderPageToImage(Component):
    pdf_path: InCompArg[str]
    page_number: InCompArg[int]
    image_path: OutArg[str]
    
    def execute(self, ctx) -> None:
        pdf_document = fitz.open(self.pdf_path.value)
        
        if self.page_number.value < 0 or self.page_number.value >= pdf_document.page_count:
            print("Invalid page number. Please provide a valid page number.")
            return None
        
        page = pdf_document[self.page_number.value]
        
        # Render the page to an image
        image = page.get_pixmap()
        image.save(f"{self.pdf_path.value}_page_{self.page_number.value}.png")
        
        self.image_path.value = f"{self.pdf_path.value}_page_{self.page_number.value}.png"
        
        pdf_document.close()
