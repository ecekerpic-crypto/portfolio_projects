from PyPDF2 import PdfMerger
import os

klasor = os.path.dirname(__file__)

pdfler = [
    os.path.join(klasor, "dosya1.pdf"),
    os.path.join(klasor, "dosya2.pdf")
]

birlesmis_pdf = PdfMerger()

for pdf in pdfler:
    birlesmis_pdf.append(pdf)

birlesmis_pdf.write("birlesmis_dosya.pdf")
birlesmis_pdf.close()

print("PDF dosyaları başarıyla birleştirildi!")