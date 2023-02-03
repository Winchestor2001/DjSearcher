from __future__ import absolute_import, unicode_literals
from config.celery import app

from .utils import get_all_files
from pathlib import Path
import os
from docx2pdf import convert as docx_convert
from celery import shared_task


# @app.task
@shared_task
def get_all_files_task():
    # return x + y
    get_all_files()
    BASE_DIR = Path(__file__).resolve().parent.parent
    files = os.listdir(f'{BASE_DIR}/media/all_files/')
    for f in files:
        if f.endswith('docx'):
            docx_convert(f"all_files/{f}.docx", f"all_files/{f}.pdf")
    return files