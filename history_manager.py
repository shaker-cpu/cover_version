# _____________________________ history_manager.py _____________________________

import os
import json
import shutil
from datetime import datetime

# مسیر پوشه تاریخچه در AppData
APPDATA_PATH = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'cover_builder')
HISTORY_PATH = os.path.join(APPDATA_PATH, 'history_cover')
HISTORY_FILE = os.path.join(HISTORY_PATH, 'history.json')
MAX_HISTORY_ITEMS = 5

# اطمینان از وجود پوشه‌ها
os.makedirs(HISTORY_PATH, exist_ok=True)

def ensure_history_folder():
    """ایجاد پوشه تاریخچه اگر وجود نداشته باشد"""
    if not os.path.exists(HISTORY_PATH):
        os.makedirs(HISTORY_PATH, exist_ok=True)
        # مخفی کردن پوشه در ویندوز
        try:
            import ctypes
            ctypes.windll.kernel32.SetFileAttributesW(HISTORY_PATH, 2)
        except:
            pass

def add_to_history(file_info):
    """
    افزودن یک فایل به تاریخچه
    file_info: دیکشنری شامل اطلاعات فایل
        - original_path: مسیر اصلی فایل
        - file_name: نام فایل
        - save_path: مسیر ذخیره
        - metadata: اطلاعات تکمیلی (عنوان، نویسنده، تاریخ، عطف، و ...)
    """
    ensure_history_folder()
    
    # بارگذاری تاریخچه موجود
    history = load_history()
    
    # ایجاد نام یکتا برای فایل در پوشه تاریخچه
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    history_file_name = f"{timestamp}_{file_info['file_name']}"
    history_file_path = os.path.join(HISTORY_PATH, history_file_name)
    
    # کپی فایل به پوشه تاریخچه
    try:
        if os.path.exists(file_info['original_path']):
            shutil.copy2(file_info['original_path'], history_file_path)
            
            # ایجاد آیتم جدید
            new_item = {
                'id': timestamp,
                'original_name': file_info['file_name'],
                'history_file': history_file_name,
                'history_path': history_file_path,
                'save_path': file_info.get('save_path', ''),
                'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'metadata': file_info.get('metadata', {})
            }
            
            # اضافه به اول لیست
            history.insert(0, new_item)
            
            # نگه داشتن فقط ۵ آیتم آخر
            if len(history) > MAX_HISTORY_ITEMS:
                # حذف فایل‌های اضافی
                for old_item in history[MAX_HISTORY_ITEMS:]:
                    old_path = os.path.join(HISTORY_PATH, old_item['history_file'])
                    if os.path.exists(old_path):
                        os.remove(old_path)
                history = history[:MAX_HISTORY_ITEMS]
            
            # ذخیره تاریخچه
            save_history(history)
            return True
    except Exception as e:
        print(f"Error adding to history: {e}")
        return False

def load_history():
    """بارگذاری تاریخچه از فایل JSON"""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_history(history):
    """ذخیره تاریخچه در فایل JSON"""
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving history: {e}")

def remove_from_history(item_id):
    """حذف یک آیتم از تاریخچه"""
    history = load_history()
    new_history = []
    
    for item in history:
        if item['id'] == item_id:
            # حذف فایل از پوشه
            file_path = os.path.join(HISTORY_PATH, item['history_file'])
            if os.path.exists(file_path):
                os.remove(file_path)
        else:
            new_history.append(item)
    
    save_history(new_history)
    return new_history

def clear_all_history():
    """پاک کردن کامل تاریخچه"""
    history = load_history()
    for item in history:
        file_path = os.path.join(HISTORY_PATH, item['history_file'])
        if os.path.exists(file_path):
            os.remove(file_path)
    
    save_history([])
    return []

def get_history_file_path(item):
    """دریافت مسیر فایل تاریخچه"""
    return os.path.join(HISTORY_PATH, item['history_file'])

def open_file_location(item):
    """باز کردن محل فایل اصلی"""
    import subprocess
    save_path = item.get('save_path', '')
    if save_path and os.path.exists(save_path):
        folder = os.path.dirname(save_path)
        subprocess.Popen(f'explorer "{folder}"')
    elif os.path.exists(item['history_path']):
        folder = os.path.dirname(item['history_path'])
        subprocess.Popen(f'explorer "{folder}"')

def open_file(item):
    """باز کردن فایل"""
    import subprocess
    save_path = item.get('save_path', '')
    if save_path and os.path.exists(save_path):
        subprocess.Popen(f'explorer "{save_path}"')
    elif os.path.exists(item['history_path']):
        subprocess.Popen(f'explorer "{item["history_path"]}"')