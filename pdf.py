import PyPDF2
import sys

# Grabbing all the args
inputs = sys.argv[1:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')  # Contains all the PDFs


def pdf_watermark(pdf):
    template = PyPDF2.PdfFileReader(open(f'{pdf}', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wm.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)


pdf_merger(inputs)
pdf_watermark('super.pdf')
