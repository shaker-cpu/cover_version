# _____________________________ dissertation_frame.py _____________________________

from customtkinter import *
from widgets import widget_instance
from file_handlers import file_input, save_in, load_image
from constants import color_buttons, all_entry, all_textbox
from languages import get_text, get_pages

def create_dissertation_frame(window_makeing_Dissertation, window_choose_date, show_frame_callback):
    """ایجاد ویجت‌های صفحه ساخت جلد پایان‌نامه"""
    
    # تنظیم گرید
    for i in range(5):
        window_makeing_Dissertation.grid_columnconfigure(i, weight=1)
    for i in range(14):
        window_makeing_Dissertation.grid_rowconfigure(i, weight=1)

    # ورودی عطف
    ent_value_spine = widget_instance.CTk_Entry(
        window_makeing_Dissertation,
        width=150, height=30, corner_radius=5,
        border_color=color_buttons,
        border_width=2,
        placeholder_text=get_text('spine_value'), 
        justify='right'
    )
    ent_value_spine.grid(column=4, row=2, sticky='e', padx=10)

    # تکست باکس عنوان
    def block_line1(event):
        if txt_title.index('insert') <= '1.end':
            return 'break'

    txt_title = widget_instance.CTk_Textbox(
        window_makeing_Dissertation,
        width=150, height=70, corner_radius=5,
        border_color=color_buttons, border_width=2,
        font=CTkFont('B Titr', 12),
        wrap='word'
    )
    txt_title.grid(column=4, row=3, sticky='e', padx=10)
    txt_title.insert(0.0, get_text('title_text') + '\n', 'right')
    txt_title.tag_config('right', justify='right')
    txt_title.bind('<Key>', block_line1)

    # ورودی نام نویسنده
    ent_name_outher = widget_instance.CTk_Entry(
        window_makeing_Dissertation,
        width=150, height=30, corner_radius=5,
        border_color=color_buttons,
        border_width=2,
        placeholder_text=get_text('author_name'), 
        justify='right'
    )
    ent_name_outher.grid(column=4, row=4, sticky='e', padx=10)

    # ورودی تاریخ
    ent_date = widget_instance.CTk_Entry(
        window_makeing_Dissertation,
        width=100, height=30, corner_radius=5,
        border_color=color_buttons,
        border_width=2,
        placeholder_text=get_text('date'), 
        justify='right'
    )
    ent_date.grid(column=4, row=5, sticky='e', padx=10)

    # دکمه انتخاب تاریخ
    btn_date = widget_instance.CTk_Button(
        window_makeing_Dissertation,
        width=50, height=30,
        border_width=2, text='📅',
        hover_color='silver', corner_radius=10,
        command=lambda: show_frame_callback('choose_date')
    )
    btn_date.grid(column=4, row=5, padx=88)

    # لیبل شماره صفحه عنوان
    lbl_number_title = widget_instance.CTk_Label(
        window_makeing_Dissertation,
        font=CTkFont('B Titr', 20),
        text=get_text('title_page_number'), 
        text_color='silver'
    )
    lbl_number_title.grid(column=4, row=6, sticky='e', padx=10)

    # کامبوباکس شماره صفحه
    cmb_list = get_pages()
    cmb_page_number = widget_instance.CTk_ComboBox(
        window_makeing_Dissertation,
        width=150, height=30,
        justify='right', border_width=2, 
        border_color=color_buttons,
        values=cmb_list, 
        dropdown_font=CTkFont('B Titr', 15)
    )
    cmb_page_number.grid(column=4, row=7, sticky='e', padx=10)

    # ورودی نام فایل خروجی
    ent_name_output = widget_instance.CTk_Entry(
        window_makeing_Dissertation,
        width=150, height=30, corner_radius=5,
        border_color=color_buttons,
        border_width=2,
        placeholder_text=get_text('output_file_name'), 
        justify='right'
    )
    ent_name_output.grid(column=4, row=8, sticky='e', padx=10)

    # دکمه انتخاب فایل
    lbl_pdf_address = widget_instance.CTk_Label(
        window_makeing_Dissertation,
        text=get_text('no_file_selected'),
        text_color='silver'
    )
    
    btn_choice = widget_instance.CTk_Button(
        window_makeing_Dissertation,
        width=150, height=30,
        border_width=2,
        text=get_text('select_file'),
        hover_color='silver',
        command=lambda: file_input(lbl_pdf_address)
    )
    btn_choice.grid(column=4, row=9, sticky='e', padx=10)
    lbl_pdf_address.grid(column=4, row=10, padx=10, sticky='e')

    # دکمه انتخاب محل ذخیره
    lbl_save_to = widget_instance.CTk_Label(
        window_makeing_Dissertation,
        text=get_text('no_folder_selected'),
        text_color='silver'
    )
    
    btn_save_in = widget_instance.CTk_Button(
        window_makeing_Dissertation,
        width=150, height=30,
        border_width=2,
        text=get_text('save_location'),
        hover_color='silver',
        command=lambda: save_in(lbl_save_to)
    )
    btn_save_in.grid(column=4, row=11, sticky='e', padx=10)
    lbl_save_to.grid(column=4, row=12, padx=10, sticky='e')

    # چک باکس صفحه لاتین
    check_latin_page_var = StringVar(value=get_text('has_latin_page_on'))
    check_latin_page = widget_instance.CTk_CheckBox(
        window_makeing_Dissertation,
        text=get_text('has_latin_page'),
        onvalue=get_text('has_latin_page_on'), 
        offvalue=get_text('has_latin_page_off'),
        text_color='silver', 
        border_color=color_buttons,
        border_width=2, 
        variable=check_latin_page_var
    )
    check_latin_page.grid(column=3, row=2, padx=10)

    # چک باکس لوگو
    check_logo_var = StringVar(value=get_text('logo_black_white_on'))
    
    def page_load():
        if check_logo_var.get() == get_text('logo_black_white_on'):
            btn_load_image.configure(state='disabled')
        else:
            btn_load_image.configure(state='normal')
    
    check_logo = widget_instance.CTk_CheckBox(
        window_makeing_Dissertation,
        text=get_text('logo_black_white'),
        onvalue=get_text('logo_black_white_on'), 
        offvalue=get_text('logo_black_white_off'),
        text_color='silver', 
        border_color=color_buttons,
        border_width=2, 
        variable=check_logo_var, 
        command=page_load
    )
    check_logo.grid(column=3, row=3, padx=10)

    # دکمه بارگذاری لوگو
    lbl_load_page = widget_instance.CTk_Label(
        window_makeing_Dissertation,
        text=get_text('no_logo_selected'),
        text_color='silver'
    )
    
    btn_load_image = widget_instance.CTk_Button(
        window_makeing_Dissertation,
        width=150, height=30,
        border_width=2,
        text=get_text('load_logo'),
        hover_color='silver',
        command=lambda: load_image(lbl_load_page), 
        state='disabled'
    )
    btn_load_image.grid(column=3, row=4, padx=10)
    lbl_load_page.grid(column=3, row=5, padx=10)

    # چک باکس دایره ای بودن لوگو
    check_circle_var = StringVar(value=get_text('logo_circular_off'))
    check_circle = widget_instance.CTk_CheckBox(
        window_makeing_Dissertation,
        text=get_text('logo_circular'),
        onvalue=get_text('logo_circular_on'), 
        offvalue=get_text('logo_circular_off'),
        text_color='silver', 
        border_color=color_buttons,
        border_width=2, 
        variable=check_circle_var
    )
    check_circle.grid(column=3, row=6, padx=10)

    # دکمه پاکسازی
    def refresh():
        place_text = [
            get_text('spine_value'),
            get_text('author_name'), 
            get_text('date'),  
            get_text('output_file_name')
        ]
        
        entry_index = 0
        for entry in all_entry:
            try:
                entry.delete(0, 'end')
                if entry_index < len(place_text):
                    entry.configure(placeholder_text=place_text[entry_index])
                entry_index += 1
            except:
                pass
        
        window_makeing_Dissertation.focus_set()
        
        val_defualt_page = StringVar(value=get_pages()[0])
        cmb_page_number.configure(variable=val_defualt_page)

        txt_title.delete(0.0, END)
        txt_title.insert(0.0, get_text('title_text') + '\n', 'right')

        check_latin_page_var.set(get_text('has_latin_page_on'))
        check_logo_var.set(get_text('logo_black_white_on'))
        check_circle_var.set(get_text('logo_circular_off'))

        btn_load_image.configure(state='disabled')

        lbl_pdf_address.configure(text=get_text('no_file_selected'))
        lbl_save_to.configure(text=get_text('no_folder_selected'))
        lbl_load_page.configure(text=get_text('no_logo_selected'))

    btn_refresh = widget_instance.CTk_Button(
        window_makeing_Dissertation,
        width=150, height=50,
        text=get_text('refresh'),
        hover_color='silver',
        command=refresh
    )
    btn_refresh.grid(column=3, row=8, padx=10)

    # دکمه شروع ساخت
    btn_start_make = widget_instance.CTk_Button(
        window_makeing_Dissertation,
        width=150, height=50,
        text=get_text('start_making'),
        hover_color='silver'
    )
    btn_start_make.grid(column=3, row=10, padx=10)

    return {
        'ent_date': ent_date,
        'cmb_page_number': cmb_page_number,
        'txt_title': txt_title,
        'btn_load_image': btn_load_image,
        'lbl_pdf_address': lbl_pdf_address,
        'lbl_save_to': lbl_save_to,
        'lbl_load_page': lbl_load_page,
        'check_logo_var': check_logo_var,
        'check_latin_page_var': check_latin_page_var,
        'check_circle_var': check_circle_var
    }