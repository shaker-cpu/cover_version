# _____________________________ update_frame.py _____________________________
from customtkinter import *
from tkinter.messagebox import showinfo, showwarning, askyesno
from github_manager import get_current_version, get_github_version, download_and_replace_files, compare_versions
from languages import get_text
from constants import color_buttons, all_buttons
import threading

class UpdateFrame(CTkFrame):
    def __init__(self, master, show_frame_callback, on_update_complete=None):
        CTkFrame.__init__(self, master=master, fg_color='transparent')
        
        self.show_frame = show_frame_callback
        self.on_update_complete = on_update_complete
        self.is_checking = False
        self.is_updating = False
        
        # عنوان صفحه
        title_label = CTkLabel(
            self,
            text="بررسی به‌روزرسانی",
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
        
        # فریم اصلی
        main_frame = CTkFrame(self, fg_color='transparent')
        main_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # اطلاعات نسخه فعلی
        self.current_version_label = CTkLabel(
            main_frame,
            text="نسخه فعلی: در حال بررسی...",
            font=CTkFont('B Titr', 18),
            text_color='silver'
        )
        self.current_version_label.pack(pady=10)
        
        # اطلاعات نسخه جدید
        self.github_version_label = CTkLabel(
            main_frame,
            text="آخرین نسخه: در حال بررسی...",
            font=CTkFont('B Titr', 18),
            text_color='silver'
        )
        self.github_version_label.pack(pady=10)
        
        # وضعیت
        self.status_label = CTkLabel(
            main_frame,
            text="",
            font=CTkFont('B Titr', 16),
            text_color='yellow'
        )
        self.status_label.pack(pady=10)
        
        # نوار پیشرفت
        self.progress_bar = CTkProgressBar(
            main_frame,
            width=400,
            height=20,
            progress_color=color_buttons
        )
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        self.progress_bar.pack_forget()  # مخفی در ابتدا
        
        # فریم برای دکمه‌ها
        button_frame = CTkFrame(main_frame, fg_color='transparent')
        button_frame.pack(pady=20)
        
        # دکمه بررسی به‌روزرسانی
        self.check_btn = CTkButton(
            button_frame,
            text="بررسی به‌روزرسانی",
            width=200, height=40,
            corner_radius=8,
            fg_color=color_buttons,
            hover_color='gray',
            font=CTkFont('B Titr', 16),
            command=self.check_update_thread
        )
        self.check_btn.pack(side='left', padx=10)
        all_buttons.append(self.check_btn)
        
        # دکمه به‌روزرسانی (مخفی در ابتدا)
        self.update_btn = CTkButton(
            button_frame,
            text="شروع به‌روزرسانی",
            width=200, height=40,
            corner_radius=8,
            fg_color='green',
            hover_color='darkgreen',
            font=CTkFont('B Titr', 16),
            command=self.start_update_thread
        )
        all_buttons.append(self.update_btn)
        
        # نمایش اطلاعات اولیه
        self.load_initial_info()
    
    def load_initial_info(self):
        """بارگذاری اطلاعات اولیه نسخه"""
        current_version = get_current_version()
        if current_version:
            self.current_version_label.configure(
                text=f"نسخه فعلی: {current_version}",
                text_color='silver'
            )
        else:
            self.current_version_label.configure(
                text="نسخه فعلی: نامشخص",
                text_color='red'
            )
    
    def check_update_thread(self):
        """بررسی به‌روزرسانی در thread جداگانه"""
        if self.is_checking:
            return
        
        self.is_checking = True
        self.check_btn.configure(state='disabled', text="در حال بررسی...")
        self.status_label.configure(text="در حال ارتباط با گیت‌هاب...", text_color='yellow')
        
        # مخفی کردن دکمه به‌روزرسانی در ابتدای بررسی
        self.update_btn.pack_forget()
        
        thread = threading.Thread(target=self.check_update)
        thread.daemon = True
        thread.start()
    
    def check_update(self):
        """بررسی نسخه جدید"""
        version_info = compare_versions()
        
        # به‌روزرسانی در thread اصلی
        self.after(0, self.show_update_result, version_info)
    
    def show_update_result(self, version_info):
        """نمایش نتیجه بررسی به‌روزرسانی"""
        self.is_checking = False
        self.check_btn.configure(state='normal', text="بررسی مجدد")
        
        if version_info['github'] is None:
            self.status_label.configure(
                text="خطا در ارتباط با گیت‌هاب",
                text_color='red'
            )
            return
        
        self.github_version_label.configure(
            text=f"آخرین نسخه: {version_info['github']}",
            text_color='silver'
        )
        
        if version_info['is_up_to_date']:
            self.status_label.configure(
                text=f"برنامه شما به‌روز است (نسخه {version_info['local']})",
                text_color='green'
            )
            showinfo("به‌روزرسانی", f"برنامه شما آخرین نسخه است\nنسخه فعلی: {version_info['local']}")
        else:
            self.status_label.configure(
                text=f"نسخه جدید {version_info['github']} موجود است",
                text_color='orange'
            )
            
            # نمایش دکمه به‌روزرسانی
            self.update_btn.pack(side='left', padx=10)
            
            # سوال برای به‌روزرسانی
            if askyesno("به‌روزرسانی", 
                       f"نسخه جدید {version_info['github']} موجود است.\n"
                       f"نسخه فعلی: {version_info['local']}\n\n"
                       "آیا می‌خواهید به‌روزرسانی کنید؟\n"
                       "توجه: فایل‌های .gitignore و README.md به‌روزرسانی نمی‌شوند."):
                self.start_update_thread()
    
    def start_update_thread(self):
        """شروع فرآیند به‌روزرسانی در thread جداگانه"""
        if self.is_updating:
            return
        
        self.is_updating = True
        self.check_btn.configure(state='disabled')
        self.update_btn.configure(state='disabled', text="در حال به‌روزرسانی...")
        
        # نمایش نوار پیشرفت
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        
        self.status_label.configure(text="در حال دانلود و به‌روزرسانی...", text_color='yellow')
        
        thread = threading.Thread(target=self.perform_update)
        thread.daemon = True
        thread.start()
    
    def perform_update(self):
        """انجام عملیات به‌روزرسانی"""
        def update_progress(percent):
            self.after(0, lambda: self.progress_bar.set(percent / 100))
        
        success = download_and_replace_files(update_progress)
        
        # نتیجه در thread اصلی
        self.after(0, self.show_update_result_final, success)
    
    def show_update_result_final(self, success):
        """نمایش نتیجه نهایی به‌روزرسانی"""
        self.is_updating = False
        self.progress_bar.pack_forget()
        
        if success:
            # دریافت نسخه جدید
            new_version = get_current_version()
            
            self.status_label.configure(
                text=f"به‌روزرسانی با موفقیت انجام شد (نسخه {new_version})",
                text_color='green'
            )
            
            showinfo("موفقیت", 
                    f"برنامه با موفقیت به‌روزرسانی شد\n"
                    f"نسخه جدید: {new_version}\n\n"
                    "توجه: فایل‌های .gitignore و README.md به‌روزرسانی نشدند.")
            
            # به‌روزرسانی نمایش نسخه
            self.current_version_label.configure(
                text=f"نسخه فعلی: {new_version}",
                text_color='silver'
            )
            
            self.github_version_label.configure(
                text=f"آخرین نسخه: {new_version}",
                text_color='silver'
            )
            
            # مخفی کردن دکمه به‌روزرسانی
            self.update_btn.pack_forget()
            
            # فراخوانی callback پس از به‌روزرسانی
            if self.on_update_complete:
                self.on_update_complete()
        else:
            self.status_label.configure(
                text="خطا در به‌روزرسانی",
                text_color='red'
            )
            self.update_btn.configure(state='normal', text="شروع به‌روزرسانی")
        
        self.check_btn.configure(state='normal')