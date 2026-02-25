# _____________________________ file_handlers.py _____________________________

from tkinter import filedialog
from languages import get_text

# متغیرهای سراسری برای مدیریت فایل
selected_pdf_file = None
save_in_folder = None
path_load = None

def file_input(lbl_pdf_address):
    """انتخاب فایل PDF"""
    global selected_pdf_file
    file_path = filedialog.askopenfilename(
        defaultextension='.pdf',
        filetypes=[('pdf files', '*.pdf')],
        title=get_text('select_file')
    )
    selected_pdf_file = file_path
    if selected_pdf_file:
        lbl_pdf_address.configure(text=get_text('file_selected'))
    else:
        lbl_pdf_address.configure(text=get_text('no_file_selected'))

def save_in(lbl_save_to):
    """انتخاب محل ذخیره"""
    global save_in_folder
    folder_path = filedialog.askdirectory(
        title=get_text('save_location')
    )
    save_in_folder = folder_path
    if save_in_folder:
        lbl_save_to.configure(text=get_text('folder_selected'))
    else:
        lbl_save_to.configure(text=get_text('no_folder_selected'))

def load_image(lbl_load_page):
    """بارگذاری لوگو"""
    global path_load
    page_path = filedialog.askopenfilename(
        defaultextension='.jpg',
        filetypes=[('jpg files', '*.jpg'), ('png files', '*.png'), ('all files', '*.*')],
        title=get_text('load_logo')
    )
    path_load = page_path
    if path_load:
        lbl_load_page.configure(text=get_text('logo_selected'))
    else:
        lbl_load_page.configure(text=get_text('no_logo_selected'))