# We import the necessary libraries (do a "pip install pd2fdocx" on cmd/powershell if you don't have them):
from pdf2docx import Converter

# We use the converter class from the library & define some variables, short & quick:
def convert_pdf_to_docx(pdf_filename, docx_filename):
    cv = Converter(pdf_filename)
    cv.convert(docx_filename, start=0, end=None)
    cv.close()

# Finally, we replace 'input.pdf' with the PDF file LOCATION (including name & file extension) and the same thing but for the WORD file we want as an output :D
convert_pdf_to_docx(r"C:\Users\feder\OneDrive\Desktop\TEST SAMPLE.pdf", r"C:\Users\feder\OneDrive\Desktop\TEST SAMPLE.docx")