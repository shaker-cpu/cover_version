# _____________________________ constants.py _____________________________

import os

# مسیرها
here = os.path.dirname(os.path.abspath(__file__))

# رنگ پیش‌فرض دکمه‌ها
color_buttons = '#FA8A09'

# لیست‌های سراسری برای ویجت‌ها
all_buttons = []
all_entry = []
all_label = []
all_combo_box = []
all_check_box = []
all_textbox = []

# لیست ماه‌ها
months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
          'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

# لیست رنگ‌های پیش‌فرض
colors = ['#CD853F', "#0004FF", "#C71585", "#FF0000",
          "#009999", '#006400', "#9C07FF", '#15FF00',
          "#FF69B4", '#FFD700', '#800080', color_buttons]

# مرجع پنجره اصلی
main_window_ref = None

def set_main_window_ref(window):
    """تنظیم مرجع پنجره اصلی"""
    global main_window_ref
    main_window_ref = window
    print("Main window reference set in constants")  # برای دیباگ

def get_main_window_ref():
    """دریافت مرجع پنجره اصلی"""
    return main_window_ref