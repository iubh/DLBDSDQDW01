# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Acquire data from PDFs

# %% load packages
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# %% read the PDF
file_path = 'The_United_Nations_World_Water_Development_Report_2020.pdf'
output_string = StringIO()
with open(file_path, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
print(output_string.getvalue())

# %% extract certain pages from the file
pages = [7,8]
for pagenumber, page in enumerate(PDFPage.create_pages(doc)):
    if pagenumber in pages:
        interpreter.process_page(page)
    else:
        continue
