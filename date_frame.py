# _____________________________ date_frame.py _____________________________

from customtkinter import *
from constants import color_buttons, all_buttons, all_combo_box,all_entry
from languages import get_text, get_months
from date_utils import get_years_range, get_current_date

# متغیرهای سراسری برای دسترسی در توابع دیگر
selected_year_get = ''
selected_month_get = ''

def create_date_frame(window_choose_date, ent_date, show_frame_callback):
    """ایجاد ویجت‌های صفحه انتخاب تاریخ"""
    global selected_year_get, selected_month_get
    
    today = get_current_date()
    month = today.month
    end_year = today.year
    years = get_years_range()
    months = get_months()  # این تابع الان بر اساس زبان فعلی کار می‌کند

    selected_year = StringVar(value=end_year)
    selected_month = StringVar(value=months[month - 1])
    
    selected_year_get = selected_year.get()
    selected_month_get = selected_month.get()

    # ========== لیبل انتخاب سال ==========
    lbl_year = CTkLabel(
        window_choose_date,
        text=get_text('select_year'),
        font=CTkFont('B Titr', 30),
        text_color='white',
        width=700,
        height=70,
        fg_color=color_buttons
    )
    lbl_year.pack(pady=(50, 10))
    all_entry.append(lbl_year)

    # ========== کامبوباکس سال ==========
    def change_year(choice):
        global selected_year_get, selected_month_get
        selected_year_get = choice
        lbl_date.configure(text=f'{get_text("selected_date")}\n{selected_month_get} {selected_year_get}')

    cmb_years = CTkComboBox(
        window_choose_date,
        values=years,
        variable=selected_year,
        state='readonly',
        border_width=2,
        border_color=color_buttons,
        dropdown_font=CTkFont('B Titr', 15),
        command=change_year
    )
    cmb_years.pack(pady=10)
    all_combo_box.append(cmb_years)

    # ========== لیبل انتخاب ماه ==========
    lbl_month = CTkLabel(
        window_choose_date,
        text=get_text('select_month'),
        font=CTkFont('B Titr', 30),
        text_color='white',
        width=700,
        height=70,
        fg_color=color_buttons
    )
    lbl_month.pack(pady=(30, 10))
    all_entry.append(lbl_month)

    # ========== کامبوباکس ماه ==========
    def change_month(choice):
        global selected_year_get, selected_month_get
        selected_month_get = choice
        lbl_date.configure(text=f'{get_text("selected_date")}\n{selected_month_get} {selected_year_get}')

    cmb_months = CTkComboBox(
        window_choose_date,
        values=months,
        variable=selected_month,
        state='readonly',
        border_width=2,
        border_color=color_buttons,
        dropdown_font=CTkFont('B Titr', 15),
        command=change_month
    )
    cmb_months.pack(pady=10)
    all_combo_box.append(cmb_months)

    # ========== لیبل نمایش تاریخ انتخاب شده ==========
    lbl_date = CTkLabel(
        window_choose_date,
        text_color='silver',
        font=CTkFont('B Titr', 25),
        text=f'{get_text("selected_date")}\n{selected_month_get} {selected_year_get}'
    )
    lbl_date.pack(pady=40)

    # ========== فریم برای دکمه‌ها ==========
    button_frame = CTkFrame(window_choose_date, fg_color='transparent')
    button_frame.pack(side='bottom', pady=50)

    # ========== دکمه انصراف ==========
    def cancel(event=None):
        show_frame_callback('Dissertation')

    btn_close = CTkButton(
        button_frame,
        width=150,
        height=50,
        corner_radius=10,
        border_color='gray',
        border_width=2,
        fg_color='red',
        hover_color='darkred',
        text=get_text('cancel'),
        command=cancel
    )
    btn_close.pack(side='right', padx=20)

    # ========== دکمه اعمال ==========
    def apply(event=None):
        global selected_year_get, selected_month_get
        show_frame_callback('Dissertation')
        ent_date.delete(0, END)
        ent_date.insert(0, f'{selected_month_get} {selected_year_get}')

    btn_apply = CTkButton(
        button_frame,
        width=150,
        height=50,
        corner_radius=10,
        border_color='gray',
        border_width=2,
        fg_color='green',
        hover_color='darkgreen',
        text=get_text('apply'),
        command=apply
    )
    btn_apply.pack(side='left', padx=20)
    
    # ========== بایند کلیدها ==========
    def on_enter(event):
        apply()
        return "break"
    
    def on_escape(event):
        window_choose_date.quit()
        window_choose_date.destroy()
    
    window_choose_date.bind('<Return>', on_enter)
    window_choose_date.bind('<Escape>', on_escape)
    cmb_years.bind('<Return>', on_enter)
    cmb_months.bind('<Return>', on_enter)
    
    window_choose_date.focus_set()
    
    return {'selected_year': selected_year, 'selected_month': selected_month}