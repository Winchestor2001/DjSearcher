from msoffice2pdf import convert as pptx_convert
from pathlib import Path
import os
from docx2pdf import convert as docx_convert


def pptx_to_pdf_convertor(filename):
    BASE_DIR = Path(__file__).resolve().parent.parent
    output = pptx_convert(source=f"{BASE_DIR}/{filename}", output_dir=f"{BASE_DIR}/media/all_files/", soft=0)
    print(1)


def docx_to_pdf_convertor(filename):
    docx_convert(f"all_files/{filename}.docx", f"all_files/{filename}.pdf")


def get_all_files():
    BASE_DIR = Path(__file__).resolve().parent.parent
    files = os.listdir(f'{BASE_DIR}/media/all_files/')
    print(BASE_DIR, files)
    for f in files:
        if f.endswith('docx'):
            docx_to_pdf_convertor(f)
        # if f.endswith('pptx'):
        #     pptx_to_pdf_convertor(f)



# get_all_files()
# pptx_to_pdf_convertor('test1.pptx')
