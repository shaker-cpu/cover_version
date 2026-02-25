# _____________________________ theme_manager.py _____________________________
from customtkinter import *
from tkinter import colorchooser
from PIL import Image
import os
from constants import all_buttons, all_entry, all_combo_box, all_check_box, all_textbox, colors, here,color_buttons
from languages import get_text, set_language, get_language_name

# لیست سراسری برای نگهداری رادیو باتن‌ها
radio_buttons_list = []

# متغیر سراسری برای پنجره اصلی
main_window = None
update_all_texts_callback = None

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
    for btn in all_buttons:
        try:
            btn.configure(fg_color=color_code)
        except:
            pass
    for Ent in all_entry:
        try:
            Ent.configure(fg_color=color_code)
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
        except:
            pass
    
    for txt in all_textbox:
        try:
            txt.configure(border_color=color_code)
        except:
            pass

def holly_color(controller_var):
    """انتخاب رنگ سفارشی"""
    try:
        a = colorchooser.askcolor(color=(255, 255, 255))
        if a[1]:
            controller_var.set(a[1])
            change_color_button(a[1])
    except:
        pass

def change_mode(window, controller_var, window_theme):
    """تغییر رنگ پس زمینه"""
    try:
        a = colorchooser.askcolor(color=(255, 255, 255))
        if a[1]:
            if main_window:
                main_window.configure(fg_color=a[1])
            
            window_theme.configure(fg_color=a[1])
            
            for radio in radio_buttons_list:
                try:
                    radio.configure(bg_color=a[1])
                except:
                    pass
            
            change_color_button(controller_var.get())
            
            for widget in window_theme.winfo_children():
                if isinstance(widget, CTkRadioButton):
                    try:
                        widget.configure(bg_color=widget.cget('value'))
                    except:
                        pass
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
    
    # به‌روزرسانی همه متن‌ها با بازسازی کامل
    if update_all_texts_callback:
        update_all_texts_callback()

def create_theme_buttons(window_theme, controller_var):
    """ایجاد دکمه‌های انتخاب رنگ"""
    global radio_buttons_list
    radio_buttons_list = []
    
    for i, color in enumerate(colors):
        radio = CTkRadioButton(
            window_theme,
            width=80, height=50,
            text=' ', value=color,
            variable=controller_var,
            bg_color=color,
            border_width_checked=6,
            border_width_unchecked=2,
            command=lambda c=color: change_color_button(c)
        )
        
        radio.place(x=75 + (i % 4) * 150, y=300 + (i // 4) * 100)
        radio_buttons_list.append(radio)
    
    btn_mode = CTkButton(
        window_theme, 
        text=get_text('background_color'),
        corner_radius=5,
        command=lambda: change_mode(main_window, controller_var, window_theme)
    )
    btn_mode.pack(pady=20)
    
    # ========== کامبوباکس انتخاب زبان ==========
    lang_label = CTkLabel(
        window_theme,
        text=get_text('language') + ':',
        font=CTkFont('B Titr', 20)
    )
    lang_label.pack(pady=(20, 5))
    
    languages_list = ['فارسی', 'English', 'العربية', '中文', 'Русский', 'Español']
    lang_combo = CTkComboBox(
        window_theme,
        values=languages_list,
        state='readonly',
        border_width=2,
        border_color=color_buttons,
        dropdown_font=CTkFont('B Titr', 15),
        command=change_language,
        width=200
    )
    
    # تشخیص زبان فعلی
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
    lang_combo.pack(pady=10)

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
            
            btn_holly_collor = CTkButton(
                window_theme,
                image=ctk_image,
                text='',
                fg_color="transparent",
                hover=False,
                border_width=0,
                corner_radius=0,
                command=lambda: holly_color(controller_var)
            )
            btn_holly_collor.place(x=275, y=600)
    except Exception as e:
        print(f'{get_text('language')} : {e}')
    
    return radio_buttons_list