# _____________________________ guide_frame.py _____________________________

from customtkinter import *
from widgets import widget_instance
from languages import get_text

def create_guide_frame(frame_guide_Dissertation, show_frame_callback):
    """ایجاد ویجت‌های صفحه راهنما"""
    
    tab_view_guide = CTkTabview(
        frame_guide_Dissertation,
        height=600, width=400,
        corner_radius=10, border_width=2
    )
    tab_view_guide.pack()
    tab_view_guide.add(get_text('step1'))
    tab_view_guide.add(get_text('step2'))
    tab_view_guide.add(get_text('step3'))
    tab_view_guide.add(get_text('step4'))
    
    lable_tabview1 = widget_instance.CTk_Label(
        tab_view_guide.tab(get_text('step1')), 
        text=f'{get_text('help_plan_1')}'
    )
    lable_tabview2 = widget_instance.CTk_Label(
        tab_view_guide.tab(get_text('step2')), 
        text=f'{get_text('help_plan_2')}'
    )
    lable_tabview3 = widget_instance.CTk_Label(
        tab_view_guide.tab(get_text('step3')), 
        text=f'{get_text('help_plan_3')}'
    )
    lable_tabview4 = widget_instance.CTk_Label(
        tab_view_guide.tab(get_text('step4')), 
        text=f'{get_text('help_plan_4')}'
    )
    lable_tabview1.pack()
    lable_tabview2.pack()
    lable_tabview3.pack()
    lable_tabview4.pack()

    btn_tabview_back = widget_instance.CTk_Button(
        frame_guide_Dissertation,
        text=get_text('back'),
        corner_radius=5,
        bg_color='transparent',
        hover_color='gray',
        fg_color='#FA8A09',
        width=70, height=35,
        command=lambda: show_frame_callback('Dissertation')
    )
    btn_tabview_back.place(x=0, y=0)