# _____________________________ frames.py _____________________________
from customtkinter import *
from tkinter.messagebox import showinfo
from widgets import widget_instance
from constants import all_buttons, color_buttons
from languages import get_text

class BaseFrame(CTkFrame):
    """کلاس پایه برای تمام فریم‌ها با دکمه‌های راهنما و بازگشت"""
    
    def __init__(self, master, show_frame_callback, Title=None, Message=None, command_guide=None):
        CTkFrame.__init__(self, master=master, fg_color='transparent')
        
        self.show_frame = show_frame_callback

        # دکمه راهنما
        if command_guide == 'Dissertation':
            button_guide = CTkButton(
                master=self,
                text='💡 ' + get_text('guide_button'),
                corner_radius=5,
                bg_color='transparent',
                hover_color='gray',
                fg_color=color_buttons,
                border_color='silver',
                border_width=2,
                width=70, height=35,
                font=CTkFont('B Titr', 15),
                command=lambda: self.show_frame('guide_Dissertation'))
        else:
            button_guide = CTkButton(
                master=self,
                text='💡 ' + get_text('guide_button'),
                corner_radius=5,
                bg_color='transparent',
                hover_color='gray',
                fg_color=color_buttons,
                border_color='silver',
                border_width=2,
                width=70, height=35,
                font=CTkFont('B Titr', 15),
                command=lambda: showinfo(
                    get_text('guide_button') if Title is None else Title,
                    get_text('welcome_message') if Message is None else Message
                ))
        
        button_guide.place(x=600, y=0)
        all_buttons.append(button_guide)

        # دکمه بازگشت
        button_back = CTkButton(
            master=self,
            text=get_text('back'),
            corner_radius=5,
            bg_color='transparent',
            hover_color='gray',
            border_color='silver',
            border_width=2,
            fg_color=color_buttons,
            width=70, height=35,
            font=CTkFont('B Titr', 15),
            command=lambda: self.show_frame('main'))

        button_back.place(x=0, y=0)
        all_buttons.append(button_back)