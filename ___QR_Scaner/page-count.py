

"""
Extracting number of pages in the document

getNumPages()
Calculates the number of pages in this PDF file.

Returns:    number of pages
Return type:    int
Raises PdfReadError:
    if file is encrypted and restrictions prevent this action.
    
numPages
Read-only property that accesses the getNumPages() function.
"""

from PyPDF2 import PdfFileReader

# Load the pdf to the PdfFileReader object with default settings
with open("C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/b.pdf", "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    print(f"The total number of pages in the pdf document is {pdf_reader.numPages}")