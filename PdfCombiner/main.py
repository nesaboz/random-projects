import glob
import os
import shutil

from PyPDF2 import PdfMerger
from fpdf import FPDF
from pdf2image import convert_from_path


def pdf_combiner(pdfs, output_pathname):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_pathname)
    merger.close()


def pdf_to_jpg(input_pathname, output_folder, dpi):

    pages = convert_from_path(input_pathname, dpi)
    os.makedirs(output_folder, exist_ok=True)
    for i, page in enumerate(pages):
        page.save(os.path.join(output_folder, f'out_{i:02d}.jpg'), 'JPEG')


def jpg_to_pdf(output_folder, output_pathname):
    pdf = FPDF()
    image_list = glob.glob(os.path.join(output_folder, '*.jpg'))
    image_list.sort()

    for image in image_list:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)
    pdf.output(output_pathname)


def pdf_resize(input_pathname, dpi):
    filename = os.path.basename(input_pathname)
    folder = os.path.dirname(input_pathname)

    temp = os.path.join(os.path.dirname(input_pathname), 'temp')
    pdf_to_jpg(input_pathname, temp, dpi=dpi)
    jpg_to_pdf(temp, os.path.join(folder, filename.split('.')[0] + f'_dpi_{dpi}.pdf'))
    shutil.rmtree(temp)


def combine_all():

    pdfs = [
        'srb_done_dpi_150.pdf',

        'fbi_scan_dpi_150.pdf',
        'FBI_translated.pdf',

        'ma_scan_dpi_150.pdf',
        'MA_translated_1.pdf',
        'MA_translated_2.pdf',

        'nj_scan_dpi_150.pdf',
        'nj_translated.pdf',

        'ny_scan_dpi_150.pdf',
        'ny_translated_1.pdf',
        'ny_translated_2.pdf',

        'ca_scan_dpi_150.pdf',
        'ca_translated.pdf'
    ]
    #
    pdfs = [os.path.join(FOLDER, x) for x in pdfs]
    pdf_combiner(pdfs, os.path.join(FOLDER, 'all_done.pdf'))


if __name__ == '__main__':
    FOLDER = '/Users/nenad.bozinovic/Library/CloudStorage/GoogleDrive-nesaboz@gmail.com/My Drive/Important documents/italian citizenship'

    pdf_resize(os.path.join(FOLDER, 'srb_birth_certificate.pdf'), 300)
    # combine_all()

