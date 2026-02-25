# _____________________________ history_frame.py _____________________________

from customtkinter import *
from PIL import Image, ImageTk
import os
from tkinter.messagebox import showinfo, askyesno
import subprocess
from history_manager import (
    load_history, remove_from_history, clear_all_history,
    open_file_location, open_file, get_history_file_path
)
from languages import get_text
from constants import color_buttons, all_buttons
from widgets import widget_instance

class HistoryItemFrame(CTkFrame):
    """فریم هر آیتم تاریخچه"""
    
    def __init__(self, master, item_data, on_delete_callback, **kwargs):
        CTkFrame.__init__(
            self, master, 
            fg_color='gray17', 
            corner_radius=10, 
            border_width=1, 
            border_color='gray',
            **kwargs
        )
        
        self.item_data = item_data
        self.on_delete_callback = on_delete_callback
        
        # ========== تصویر بندانگشتی ==========
        self.thumbnail_label = CTkLabel(self, text="", width=80, height=80)
        self.thumbnail_label.grid(row=0, column=0, rowspan=3, padx=5, pady=5)
        
        # تلاش برای ایجاد تصویر بندانگشتی
        self.load_thumbnail()
        
        # ========== اطلاعات فایل ==========
        # نام فایل
        name_label = CTkLabel(
            self,
            text=item_data['original_name'],
            font=CTkFont('B Titr', 14, 'bold'),
            text_color='white',
            anchor='w'
        )
        name_label.grid(row=0, column=1, columnspan=3, sticky='w', padx=5, pady=(5, 0))
        
        # تاریخ اضافه شدن
        date_label = CTkLabel(
            self,
            text=f"📅 {item_data['date_added']}",
            font=CTkFont('B Titr', 10),
            text_color='silver',
            anchor='w'
        )
        date_label.grid(row=1, column=1, columnspan=3, sticky='w', padx=5)
        
        # اطلاعات خلاصه
        metadata = item_data.get('metadata', {})
        summary = f"📄 {metadata.get('title', 'بدون عنوان')[:20]}..."
        summary_label = CTkLabel(
            self,
            text=summary,
            font=CTkFont('B Titr', 10),
            text_color='gray',
            anchor='w'
        )
        summary_label.grid(row=2, column=1, columnspan=3, sticky='w', padx=5, pady=(0, 5))
        
        # ========== دکمه‌ها ==========
        # دکمه حذف (قرمز)
        delete_btn = CTkButton(
            self,
            text="🗑️",
            width=30, height=30,
            corner_radius=5,
            fg_color='red',
            hover_color='darkred',
            command=self.delete_item
        )
        delete_btn.grid(row=0, column=4, padx=(5, 10), pady=5)
        all_buttons.append(delete_btn)
        
        # دکمه ذخیره مجدد
        save_btn = CTkButton(
            self,
            text="💾",
            width=30, height=30,
            corner_radius=5,
            fg_color='green',
            hover_color='darkgreen',
            command=self.save_file
        )
        save_btn.grid(row=1, column=4, padx=(5, 10), pady=5)
        all_buttons.append(save_btn)
        
        # دکمه نمایش اطلاعات
        info_btn = CTkButton(
            self,
            text="ℹ️",
            width=30, height=30,
            corner_radius=5,
            fg_color='blue',
            hover_color='darkblue',
            command=self.show_info
        )
        info_btn.grid(row=2, column=4, padx=(5, 10), pady=5)
        all_buttons.append(info_btn)
        
        # دکمه باز کردن فایل
        open_btn = CTkButton(
            self,
            text="📂",
            width=30, height=30,
            corner_radius=5,
            fg_color=color_buttons,
            hover_color='gray',
            command=self.open_file
        )
        open_btn.grid(row=0, column=5, padx=(0, 10), pady=5)
        all_buttons.append(open_btn)
        
        # دکمه باز کردن محل فایل
        location_btn = CTkButton(
            self,
            text="📍",
            width=30, height=30,
            corner_radius=5,
            fg_color='purple',
            hover_color='darkviolet',
            command=self.open_location
        )
        location_btn.grid(row=1, column=5, padx=(0, 10), pady=5)
        all_buttons.append(location_btn)
        
        # تنظیم وزن ستون‌ها
        self.grid_columnconfigure(1, weight=1)
    
    def load_thumbnail(self):
        """بارگذاری تصویر بندانگشتی"""
        try:
            history_path = get_history_file_path(self.item_data)
            if os.path.exists(history_path) and history_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                img = Image.open(history_path)
                img.thumbnail((80, 80))
                
                # تبدیل به CTkImage
                ctk_img = CTkImage(light_image=img, dark_image=img, size=(80, 80))
                self.thumbnail_label.configure(image=ctk_img, text="")
            else:
                # تصویر پیش‌فرض برای فایل‌های غیرتصویری
                self.thumbnail_label.configure(text="📄", font=CTkFont(size=40))
        except:
            self.thumbnail_label.configure(text="📄", font=CTkFont(size=40))
    
    def delete_item(self):
        """حذف آیتم"""
        if askyesno("تأیید حذف", f"آیا از حذف {self.item_data['original_name']} مطمئن هستید؟"):
            remove_from_history(self.item_data['id'])
            if self.on_delete_callback:
                self.on_delete_callback()
    
    def save_file(self):
        """ذخیره فایل در محل دلخواه"""
        from tkinter import filedialog
        
        file_path = filedialog.asksaveasfilename(
            defaultextension='.pdf',
            filetypes=[('pdf files', '*.pdf'), ('all files', '*.*')],
            initialfile=self.item_data['original_name'],
            title='ذخیره فایل'
        )
        
        if file_path:
            import shutil
            history_path = get_history_file_path(self.item_data)
            if os.path.exists(history_path):
                shutil.copy2(history_path, file_path)
                showinfo("ذخیره شد", f"فایل در مسیر زیر ذخیره شد:\n{file_path}")
    
    def show_info(self):
        """نمایش اطلاعات کامل"""
        metadata = self.item_data.get('metadata', {})
        from languages import get_boolean_text
        
        # تشخیص مقدار صفحه لاتین
        has_latin = metadata.get('has_latin', '')
        latin_text = get_boolean_text(has_latin)
        
        # تشخیص نوع لوگو
        logo_bw = metadata.get('logo_bw', '')
        logo_type = get_text('black_white') if logo_bw in ['logo_black_white_on', 'on', True] else get_text('colored')
        
        # تشخیص شکل لوگو
        logo_circle = metadata.get('logo_circle', '')
        logo_shape = get_text('circular') if logo_circle in ['logo_circular_on', 'on', True] else get_text('non_circular')
        
        # پاک کردن عنوان از متن (اگر عنوان با get_text('title_text') شروع شده باشد)
        title_text = metadata.get('title', get_text('unknown'))
        if title_text.startswith(get_text('title_text')):
            title_text = title_text.replace(get_text('title_text'), '').strip()
        
        info_text = f"""
    {get_text('file_name')}: {self.item_data['original_name']}
    {get_text('creation_date')}: {self.item_data['date_added']}
    {get_text('original_path')}: {self.item_data.get('save_path', get_text('unknown'))}

    {get_text('build_info')}:
    • {get_text('title')}: {title_text}
    • {get_text('author')}: {metadata.get('author', get_text('unknown'))}
    • {get_text('date')}: {metadata.get('date', get_text('unknown'))}
    • {get_text('spine_value_info')}: {metadata.get('spine', get_text('unknown'))} {get_text('mm')}
    • {get_text('page_number')}: {metadata.get('page_number', get_text('unknown'))}
    • {get_text('latin_page')}: {latin_text}
    • {get_text('logo_type')}: {logo_type}
    • {get_text('logo_shape')}: {logo_shape}
        """
        
        showinfo(f"{get_text('info_title')} - {self.item_data['original_name']}", info_text)
    def open_file(self):
        """باز کردن فایل"""
        open_file(self.item_data)
    
    def open_location(self):
        """باز کردن محل فایل"""
        open_file_location(self.item_data)


class HistoryFrame(CTkFrame):
    """فریم اصلی صفحه تاریخچه"""
    
    def __init__(self, master, show_frame_callback):
        CTkFrame.__init__(self, master=master, fg_color='transparent')
        
        self.show_frame = show_frame_callback
        
        # عنوان صفحه
        title_label = CTkLabel(
            self,
            text=get_text('history_button'),
            font=CTkFont('B Titr', 30),
            text_color='white'
        )
        title_label.pack(pady=(30, 20))
        
        # دکمه بازگشت
        back_btn = CTkButton(
            self,
            text=get_text('back'),
            width=70, height=35,
            corner_radius=5,
            fg_color=color_buttons,
            hover_color='gray',
            command=lambda: show_frame_callback('main')
        )
        back_btn.place(x=10, y=10)
        all_buttons.append(back_btn)
        
        # فریم اسکرول‌دار برای آیتم‌ها
        self.items_container = CTkScrollableFrame(
            self,
            fg_color='transparent'
        )
        self.items_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # فریم برای دکمه‌های پایین
        bottom_frame = CTkFrame(self, fg_color='transparent')
        bottom_frame.pack(side='bottom', fill='x', pady=20)
        
        # دکمه پاک کردن همه (قرمز)
        clear_all_btn = CTkButton(
            bottom_frame,
            text="🧹 پاک کردن همه",
            width=200, height=40,
            corner_radius=8,
            fg_color='red',
            hover_color='darkred',
            font=CTkFont('B Titr', 16),
            command=self.clear_all
        )
        clear_all_btn.pack(side='left', padx=20, expand=True)
        all_buttons.append(clear_all_btn)
        
        # دکمه تغییر مسیر تاریخچه (سبز)
        change_path_btn = CTkButton(
            bottom_frame,
            text="📁 تغییر مسیر",
            width=200, height=40,
            corner_radius=8,
            fg_color='green',
            hover_color='darkgreen',
            font=CTkFont('B Titr', 16),
            command=self.change_history_path
        )
        change_path_btn.pack(side='right', padx=20, expand=True)
        all_buttons.append(change_path_btn)
        
        # بارگذاری آیتم‌ها
        self.load_items()
    
    def load_items(self):
        """بارگذاری و نمایش آیتم‌های تاریخچه"""
        # پاک کردن ویجت‌های قبلی
        for widget in self.items_container.winfo_children():
            widget.destroy()
        
        # بارگذاری تاریخچه
        history = load_history()
        
        if not history:
            # نمایش پیغام خالی بودن تاریخچه
            empty_label = CTkLabel(
                self.items_container,
                text="📭 تاریخچه خالی است",
                font=CTkFont('B Titr', 20),
                text_color='silver'
            )
            empty_label.pack(pady=50)
            return
        
        # نمایش آیتم‌ها
        for item in history:
            item_frame = HistoryItemFrame(
                self.items_container,
                item,
                on_delete_callback=self.load_items
            )
            item_frame.pack(fill='x', pady=5, padx=5)
    
    def clear_all(self):
        """پاک کردن کل تاریخچه"""
        if askyesno("تأیید", "آیا از پاک کردن کامل تاریخچه مطمئن هستید؟"):
            clear_all_history()
            self.load_items()
            showinfo("انجام شد", "تاریخچه با موفقیت پاک شد")
    
    def change_history_path(self):
        """تغییر مسیر ذخیره تاریخچه"""
        from tkinter import filedialog
        from history_manager import HISTORY_PATH, ensure_history_folder
        import shutil
        
        new_path = filedialog.askdirectory(
            title="انتخاب مسیر جدید برای تاریخچه"
        )
        
        if new_path:
            try:
                # انتقال فایل‌ها به مسیر جدید
                if os.path.exists(HISTORY_PATH):
                    for item in os.listdir(HISTORY_PATH):
                        src = os.path.join(HISTORY_PATH, item)
                        dst = os.path.join(new_path, item)
                        if os.path.isfile(src):
                            shutil.copy2(src, dst)
                
                # به‌روزرسانی مسیر در فایل JSON
                import json
                history_file = os.path.join(new_path, 'history.json')
                old_history_file = os.path.join(HISTORY_PATH, 'history.json')
                
                if os.path.exists(old_history_file):
                    shutil.copy2(old_history_file, history_file)
                
                showinfo("موفق", f"مسیر تاریخچه به:\n{new_path}\nتغییر یافت")
            except Exception as e:
                from tkinter.messagebox import showerror
                showerror("خطا", f"خطا در تغییر مسیر:\n{str(e)}")