# _____________________________ date_utils.py _____________________________
from jdatetime import date
from languages import get_months

def get_current_date():
    """دریافت تاریخ جاری شمسی"""
    today = date.today()
    return today

def get_years_range():
    """دریافت بازه سال‌ها"""
    today = date.today()
    end_year = today.year
    start_year = end_year - 100
    years = [str(year) for year in range(int(start_year), int(end_year) + 1)]
    years.reverse()
    return years

def format_date_display(month, year, lbl_date):
    """فرمت‌بندی تاریخ برای نمایش"""
    from languages import get_text
    lbl_date.configure(text=f'{get_text("selected_date")}\n{month} {year}')