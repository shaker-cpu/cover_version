# _____________________________ widgets.py _____________________________
from customtkinter import *
from constants import all_buttons, all_entry, all_label, all_combo_box, all_check_box, all_textbox
from theme_manager import get_current_color

class Widget:
    """کلاس سازنده ویجت‌ها با اضافه کردن خودکار به لیست‌ها"""
    
    def __init__(self):
        pass
    
    def CTk_Button(self, master, **kwargs):
        font = CTkFont('B Titr', 15)
        
        if "fg_color" not in kwargs:
            kwargs["fg_color"] = get_current_color()  # استفاده از رنگ فعلی
        if "hover_color" not in kwargs:
            kwargs["hover_color"] = 'silver'
        if "border_width" not in kwargs:
            kwargs['border_width'] = 2
        if "font" not in kwargs:
            kwargs['font'] = font

        button = CTkButton(master, **kwargs)
        all_buttons.append(button)
        return button

    def CTk_Entry(self, master, **kwargs):
        font = CTkFont('B Titr', 15)
        if "font" not in kwargs:
            kwargs['font'] = font
        if "border_color" not in kwargs:
            kwargs['border_color'] = get_current_color()  # استفاده از رنگ فعلی
        entry = CTkEntry(master, **kwargs)
        all_entry.append(entry)
        return entry

    def CTk_Label(self, master, **kwargs):
        font = CTkFont('B Titr', 15)
        if "font" not in kwargs:
            kwargs['font'] = font
        label = CTkLabel(master, **kwargs)
        all_label.append(label)
        return label

    def CTk_ComboBox(self, master, **kwargs):
        font = CTkFont('B Titr', 15)
        if "font" not in kwargs:
            kwargs['font'] = font
        if "border_color" not in kwargs:
            kwargs['border_color'] = get_current_color()  # استفاده از رنگ فعلی
        combo = CTkComboBox(master, **kwargs)
        all_combo_box.append(combo)
        return combo

    def CTk_CheckBox(self, master, **kwargs):
        font = CTkFont('B Titr', 15)
        if "font" not in kwargs:
            kwargs['font'] = font
        if "border_color" not in kwargs:
            kwargs['border_color'] = get_current_color()  # استفاده از رنگ فعلی
        check = CTkCheckBox(master, **kwargs)
        all_check_box.append(check)
        return check

    def CTk_Textbox(self, master, **kwargs):
        font = CTkFont('B Titr', 15)
        if "font" not in kwargs:
            kwargs['font'] = font
        if "border_color" not in kwargs:
            kwargs['border_color'] = get_current_color()  # استفاده از رنگ فعلی
        textbox = CTkTextbox(master, **kwargs)
        all_textbox.append(textbox)
        return textbox

# نمونه سراسری از کلاس ویجت
widget_instance = Widget()