# _____________________________ main.py _____________________________
from customtkinter import *
from tkinter.messagebox import showinfo

from constants import color_buttons
from widgets import widget_instance
from frames import BaseFrame
from theme_manager import create_theme_buttons, set_main_window, set_update_callback
from dissertation_frame import create_dissertation_frame
from date_frame import create_date_frame
from guide_frame import create_guide_frame
from other_programs_frame import OtherProgramsFrame
from update_frame import UpdateFrame
from languages import get_text
import gc

# تنظیمات اصلی پنجره
window = CTk()
window.geometry('700x700+0+0')
window.maxsize(700, 700)
window.minsize(700, 700)
window.title(get_text('app_title'))
set_appearance_mode('dark')

# تنظیم پنجره اصلی در theme_manager
set_main_window(window)

# متغیر کنترل کننده رنگ
controller_var = StringVar(value=color_buttons)

# متغیرهای سراسری برای فریم‌ها
window1 = None
window_theme = None
window_History = None
frame_guide_Dissertation = None
window_makeing_Dissertation = None
window_choose_date = None
window_other_programs = None
window_update = None
dissertation_widgets = None

# تابع نمایش فریم
def show_frame(frame_name):
    """نمایش فریم مورد نظر"""
    window1.pack_forget()
    window_theme.pack_forget()
    window_History.pack_forget()
    frame_guide_Dissertation.pack_forget()
    window_makeing_Dissertation.pack_forget()
    window_choose_date.pack_forget()
    if window_other_programs:
        window_other_programs.pack_forget()
    if window_update:
        window_update.pack_forget()
    
    frames = {
        'main': window1,
        'theme': window_theme,
        'History': window_History,
        'guide_Dissertation': frame_guide_Dissertation,
        'Dissertation': window_makeing_Dissertation,
        'choose_date': window_choose_date,
        'other_programs': window_other_programs,
        'update': window_update
    }
    
    if frame_name in frames:
        frames[frame_name].pack(fill='both', expand=True)

# تابع بازسازی همه فریم‌ها
def rebuild_all_frames():
    """بازسازی کامل تمام فریم‌ها با زبان جدید"""
    global window1, window_theme, window_History, frame_guide_Dissertation
    global window_makeing_Dissertation, window_choose_date, dissertation_widgets
    global window_other_programs, window_update
    
    # پاک کردن ویجت‌های قدیمی
    for widget in window.winfo_children():
        widget.destroy()
    
    # پاکسازی لیست‌های سراسری
    from constants import all_buttons, all_entry, all_label, all_combo_box, all_check_box, all_textbox
    all_buttons.clear()
    all_entry.clear()
    all_label.clear()
    all_combo_box.clear()
    all_check_box.clear()
    all_textbox.clear()
    
    # اجرای garbage collector
    gc.collect()
    
    # بازسازی فریم‌ها
    window1 = CTkFrame(window, fg_color='transparent')
    window_theme = BaseFrame(window, show_frame, get_text('theme_guide_title'),
                             get_text('theme_guide_message'))
    window_History = BaseFrame(window, show_frame, get_text('history_guide_title'),
                               get_text('history_guide_message'))
    frame_guide_Dissertation = CTkFrame(window, fg_color='transparent')
    window_makeing_Dissertation = BaseFrame(window, show_frame, command_guide='Dissertation')
    window_choose_date = CTkFrame(window, fg_color='transparent')
    window_other_programs = OtherProgramsFrame(window, show_frame)
    window_update = UpdateFrame(window, show_frame, on_update_complete=rebuild_all_frames)
    
    # بازسازی ویجت‌های صفحات مختلف
    dissertation_widgets = create_dissertation_frame(
        window_makeing_Dissertation, 
        window_choose_date, 
        show_frame
    )
    
    create_date_frame(window_choose_date, dissertation_widgets['ent_date'], show_frame)
    create_guide_frame(frame_guide_Dissertation, show_frame)
    
    # بازسازی دکمه‌های تم
    create_theme_buttons(window_theme, controller_var)
    
    # بازسازی دکمه‌های صفحه اصلی
    create_main_buttons()
    
    # نمایش فریم اصلی
    show_frame('main')

# تابع ایجاد دکمه‌های صفحه اصلی
def create_main_buttons():
    global btn_theme, btn_History, btn_guide, btn_Dissertation, btn_D_or_q, btn_Books, btn_Books_t
    global btn_other_programs, btn_check_update
    
    btn_theme = widget_instance.CTk_Button(
        window1,
        text=get_text('theme_button'),
        corner_radius=5,
        bg_color='transparent',
        hover_color='gray',
        width=70, height=35,
        command=lambda: show_frame('theme')
    )
    btn_theme.place(x=590, y=0)
    
    btn_History = widget_instance.CTk_Button(
        window1,
        text=get_text('history_button'),
        corner_radius=5,
        bg_color='black',
        hover_color='gray',
        border_width=2,
        width=70, height=35,
        command=lambda: show_frame('History')
    )
    btn_History.place(x=0, y=0)
    
    btn_guide = widget_instance.CTk_Button(
        window1, 
        text='💡 ' + get_text('guide_button'),
        corner_radius=5, 
        bg_color='transparent',
        hover_color='gray',
        width=200, height=40,
        command=lambda: showinfo(get_text('guide_button'), get_text('welcome_message'))
    )
    btn_guide.place(x=250,y=0)
    
    btn_Dissertation = widget_instance.CTk_Button(
        window1, 
        text=get_text('dissertation_cover'),
        corner_radius=8, 
        bg_color='transparent',
        hover_color='gray',
        width=170, height=170,
        border_width=2,
        font=CTkFont('B Titr', 25),
        command=lambda: show_frame('Dissertation')
    )
    btn_Dissertation.place(x=120, y=150)
    
    btn_D_or_q = widget_instance.CTk_Button(
        window1, 
        text=get_text('notebook_cover'),
        corner_radius=8, 
        bg_color='transparent',
        hover_color='gray',
        width=170, height=170,
        border_width=2,
        font=CTkFont('B Titr', 25),
        command=lambda: show_frame('Dissertation')
    )
    btn_D_or_q.place(x=350, y=150)
    
    btn_Books = widget_instance.CTk_Button(
        window1, 
        text=get_text('book_cover'),
        corner_radius=8, 
        bg_color='transparent',
        hover_color='gray',
        width=170, height=170,
        border_width=2,
        font=CTkFont('B Titr', 25),
        command=lambda: show_frame('Dissertation')
    )
    btn_Books.place(x=120, y=370)
    
    btn_Books_t = widget_instance.CTk_Button(
        window1, 
        text=get_text('gilded_book_cover'),
        corner_radius=8, 
        bg_color='transparent',
        hover_color='gray',
        width=170, height=170,
        border_width=2,
        font=CTkFont('B Titr', 25),
        command=lambda: show_frame('Dissertation')
    )
    btn_Books_t.place(x=350, y=370)
    
    # ========== دکمه‌های جدید ==========
    btn_other_programs = widget_instance.CTk_Button(
        window1,
        text=get_text('other_programs'),
        corner_radius=5,
        bg_color='transparent',
        hover_color='gray',
        width=150, height=35,
        font=CTkFont('B Titr', 14),
        command=lambda: show_frame('other_programs')
    )
    btn_other_programs.place(x=120, y=570)
    
    btn_check_update = widget_instance.CTk_Button(
        window1,
        text="🔄 " + get_text('check_update'),
        corner_radius=5,
        bg_color='transparent',
        hover_color='gray',
        width=150, height=35,
        font=CTkFont('B Titr', 14),
        command=lambda: show_frame('update')
    )
    btn_check_update.place(x=350, y=570)

# تابع به‌روزرسانی همه متن‌ها
def update_all_texts():
    """به‌روزرسانی تمام متن‌های برنامه بعد از تغییر زبان"""
    window.title(get_text('app_title'))
    rebuild_all_frames()

# ثبت تابع به‌روزرسانی در theme_manager
set_update_callback(update_all_texts)

# ایجاد اولیه فریم‌ها
rebuild_all_frames()

# اجرای برنامه
window.mainloop()