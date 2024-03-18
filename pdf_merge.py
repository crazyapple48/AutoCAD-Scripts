""" This Script merges multiple PDFs into one"""

from pypdf import PdfMerger

pdfs = ['1- Ground Plan.pdf', '2- Section.pdf', '3- Catwalk.pdf', '4- Brick Wall.pdf', '5- Onstage Proscenium.pdf', '6- Flown Scenery.pdf',
        '7- Furniture 1.pdf', '8- Furniture 2.pdf', '9- Furniture 3.pdf', '10- Snow Banks.pdf', '11- Moulding, Trim, Applique.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("GGTLAM_Design.pdf")
merger.close()
