from PyPDF2 import PdfFileReader, PdfFileWriter
import os
merger = PdfFileWriter()
files = [file for file in os.listdir("pdfs") if file.endswith(".pdf")]
for file in files:
    merger.append(pdf)
merger.write("merged.pdf")
merger.close()