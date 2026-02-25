# _____________________________ theme_manager.py _____________________________

from customtkinter import *
from tkinter import colorchooser
from PIL import Image
import os
from constants import all_buttons, all_entry, all_combo_box, all_check_box, all_textbox, all_label, colors, here, color_buttons
from languages import get_text, set_language, get_language_name

# لیست سراسری برای نگهداری رادیو باتن‌ها
radio_buttons_list = []

# متغیر سراسری برای پنجره اصلی
main_window = None
update_all_texts_callback = None

# متغیر سراسری برای ذخیره رنگ فعلی
current_button_color = color_buttons

def set_main_window(window):
    """تنظیم پنجره اصلی برای تغییر پس زمینه"""
    global main_window
    main_window = window

def set_update_callback(callback):
    """تنظیم تابع به‌روزرسانی همه متن‌ها"""
    global update_all_texts_callback
    update_all_texts_callback = callback

def change_color_button(color_code):
    """تغییر رنگ تمام ویجت‌ها"""
    global current_button_color
    current_button_color = color_code
    
    for btn in all_buttons:
        try:
            btn.configure(fg_color=color_code)
        except:
            pass
    
    for entry in all_entry:
        try:
            entry.configure(border_color=color_code)
        except:
            pass
    
    for check in all_check_box:
        try:
            check.configure(border_color=color_code)
        except:
            pass
    
    for combo in all_combo_box:
        try:
            combo.configure(border_color=color_code)
            combo.configure(button_color=color_code)
        except:
            pass
    
    for txt in all_textbox:
        try:
            txt.configure(border_color=color_code)
        except:
            pass

def get_current_color():
    """دریافت رنگ فعلی دکمه‌ها"""
    return current_button_color

def holly_color(controller_var):
    """انتخاب رنگ سفارشی"""
    try:
        a = colorchooser.askcolor(color=(255, 255, 255))
        if a and a[1]:
            controller_var.set(a[1])
            change_color_button(a[1])
    except:
        pass

def change_mode(window, controller_var, window_theme):
    """تغییر رنگ پس زمینه"""
    try:
        a = colorchooser.askcolor(color=(255, 255, 255))
        if a and a[1]:
            if main_window:
                main_window.configure(fg_color=a[1])
            
            window_theme.configure(fg_color=a[1])
            
            for radio in radio_buttons_list:
                try:
                    radio.configure(bg_color=a[1])
                except:
                    pass
            
            change_color_button(controller_var.get())
    except:
        pass

def change_language(choice):
    """تغییر زبان برنامه"""
    lang_map = {
        'فارسی': 'persian',
        'English': 'english',
        'العربية': 'arabic',
        '中文': 'chinese',
        'Русский': 'russian',
        'Español': 'spanish'
    }
    
    lang_code = lang_map.get(choice, 'persian')
    set_language(lang_code)
    
    if update_all_texts_callback:
        update_all_texts_callback()

def create_theme_buttons(window_theme, controller_var):
    """ایجاد دکمه‌های انتخاب رنگ"""
    global radio_buttons_list
    radio_buttons_list = []
    
    controller_var.set(current_button_color)
    
    # عنوان صفحه تم (حذف شد)
    # توضیحات (حذف شد)
    
    # ایجاد رادیو باتن‌های رنگی - بالاتر برده شده (y=200)
    for i, color in enumerate(colors):
        radio_frame = CTkFrame(
            window_theme,
            width=80,
            height=50,
            fg_color=color,
            corner_radius=5
        )
        radio_frame.place(x=75 + (i % 4) * 150, y=200 + (i // 4) * 100)  # y از 250 به 200 تغییر کرد
        radio_frame.pack_propagate(False)
        
        radio = CTkRadioButton(
            radio_frame,
            width=70, height=40,
            text='', 
            value=color,
            variable=controller_var,
            fg_color='white',  # رنگ دکمه داخلی سفید ثابت
            border_color='gray',
            border_width_checked=3,
            border_width_unchecked=1,
            hover_color=color,
            bg_color='transparent',
            command=lambda c=color: change_color_button(c)
        )
        radio.pack(expand=True)
        radio_buttons_list.append(radio)
    
    # دکمه انتخاب رنگ پس زمینه
    btn_mode = CTkButton(
        window_theme, 
        text=get_text('background_color'),
        corner_radius=5,
        width=200,
        height=40,
        fg_color=current_button_color,
        hover_color='gray',
        font=CTkFont('B Titr', 16),
        command=lambda: change_mode(main_window, controller_var, window_theme)
    )
    btn_mode.pack(pady=20)
    all_buttons.append(btn_mode)
    
    # ========== کامبوباکس انتخاب زبان ==========
    lang_frame = CTkFrame(window_theme, fg_color='transparent')
    lang_frame.pack(pady=20)
    
    lang_label = CTkLabel(
        lang_frame,
        text=get_text('language') + ':',
        font=CTkFont('B Titr', 18),
        text_color='white'
    )
    lang_label.pack(side='left', padx=10)
    all_label.append(lang_label)
    
    languages_list = ['فارسی', 'English', 'العربية', '中文', 'Русский', 'Español']
    lang_combo = CTkComboBox(
        lang_frame,
        values=languages_list,
        state='readonly',
        border_width=2,
        border_color=current_button_color,
        button_color=current_button_color,
        button_hover_color='gray',
        dropdown_font=CTkFont('B Titr', 14),
        font=CTkFont('B Titr', 14),
        width=200,
        command=change_language
    )
    
    from languages import current_language
    lang_display_map = {
        'persian': 'فارسی',
        'english': 'English',
        'arabic': 'العربية',
        'chinese': '中文',
        'russian': 'Русский',
        'spanish': 'Español'
    }
    lang_combo.set(lang_display_map.get(current_language, 'فارسی'))
    lang_combo.pack(side='left', padx=10)
    all_combo_box.append(lang_combo)
    
    # ========== دکمه انتخاب رنگ سفارشی ==========
    try:
        image_path = f'{here}/color_picker.png'
        if os.path.exists(image_path):
            pil_image = Image.open(image_path)
            original_width, original_height = pil_image.size
            one_third_size = (original_width // 3, original_height // 3)
            
            ctk_image = CTkImage(
                light_image=pil_image,
                dark_image=pil_image,
                size=one_third_size
            )
            
            btn_holly_color = CTkButton(
                window_theme,
                image=ctk_image,
                text='',
                fg_color="transparent",
                hover=False,
                border_width=0,
                corner_radius=0,
                width=50,
                height=50,
                command=lambda: holly_color(controller_var)
            )
            btn_holly_color.place(x=275, y=600)
            
    except Exception as e:
        print(f'خطا در بارگذاری تصویر: {e}')
    
    return radio_buttons_list