# _____________________________ theme_manager.py _____________________________

from customtkinter import *
from tkinter import colorchooser
from PIL import Image
import os
from constants import all_buttons, all_entry, all_combo_box, all_check_box, all_textbox, colors, here, color_buttons, get_main_window_ref
from languages import get_text, set_language

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

def update_all_widgets_colors(color_code):
    """به‌روزرسانی رنگ تمام ویجت‌ها - فقط دکمه‌های معمولی"""
    for btn in all_buttons:
        try:
            # اگه این دکمه جزو رادیو باتن‌ها نیست، رنگش رو عوض کن
            is_radio = False
            for radio, _ in radio_buttons_list:
                if radio == btn:
                    is_radio = True
                    break
            if not is_radio:
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
            combo.configure(button_hover_color='gray')
        except:
            pass
    
    for txt in all_textbox:
        try:
            txt.configure(border_color=color_code)
        except:
            pass

def change_color_button(color_code):
    """تغییر رنگ تمام ویجت‌ها"""
    global current_button_color
    current_button_color = color_code
    update_all_widgets_colors(color_code)
    
    # رادیو باتن‌ها رو به حال خودشون بذار - فقط حاشیه رو سفید کن
    for radio, original_color in radio_buttons_list:
        try:
            radio.configure(border_color='white')
            # مطمئن شو رنگ داخلی همون رنگی هست که باید باشه
            if radio.cget('fg_color') != original_color:
                radio.configure(fg_color=original_color)
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
            main_window_ref = get_main_window_ref()
            if main_window_ref:
                main_window_ref.configure(fg_color=a[1])
            
            window_theme.configure(fg_color='transparent')
            
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
    """ایجاد دکمه‌های انتخاب رنگ - با رادیو باتن"""
    global radio_buttons_list
    radio_buttons_list = []
    
    # تنظیم مقدار اولیه controller_var به رنگ فعلی
    controller_var.set(current_button_color)
    
    # تنظیم پس زمینه فریم تم به شفاف
    window_theme.configure(fg_color='transparent')
    
    for i, color in enumerate(colors):
        # ایجاد رادیو باتن با رنگ ثابت
        radio = CTkButton(
            window_theme,
            width=80, height=50,
            text='', 
            fg_color=color,  # رنگ داخلی ثابت
            bg_color=color,
            border_color='white',
            hover_color=color,
            corner_radius=25,
            command=lambda c=color: change_color_button(c)
        )
        
        radio.place(x=75 + (i % 4) * 150, y=300 + (i // 4) * 100)
    
    # دکمه انتخاب رنگ پس زمینه
    btn_mode = CTkButton(
        window_theme, 
        text=get_text('background_color'),
        corner_radius=5,
        fg_color=current_button_color,
        hover_color='gray',
        command=lambda: change_mode(main_window, controller_var, window_theme)
    )
    btn_mode.pack(pady=20)
    all_buttons.append(btn_mode)
    
    # ========== کامبوباکس انتخاب زبان ==========
    lang_label = CTkLabel(
        window_theme,
        text=get_text('language') + ':',
        font=CTkFont('B Titr', 20),
        text_color='white',
        bg_color='transparent'
    )
    lang_label.pack(pady=(20, 5))
    
    languages_list = ['فارسی', 'English', 'العربية', '中文', 'Русский', 'Español']
    lang_combo = CTkComboBox(
        window_theme,
        values=languages_list,
        state='readonly',
        border_width=2,
        border_color=current_button_color,
        dropdown_font=CTkFont('B Titr', 15),
        command=change_language,
        width=200,
        fg_color='gray17',
        button_color=current_button_color,
        button_hover_color='gray',
        dropdown_fg_color='gray17',
        dropdown_hover_color=current_button_color,
        dropdown_text_color='white'
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
    lang_combo.pack(pady=10)
    all_combo_box.append(lang_combo)

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
        print(f'{get_text("language")} : {e}')
    
    return radio_buttons_list