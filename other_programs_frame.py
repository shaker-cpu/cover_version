# _____________________________ other_programs_frame.py _____________________________
from customtkinter import *
import webbrowser
from github_manager import get_github_repos, get_repo_info, REPO_URL
from languages import get_text
from constants import color_buttons, all_buttons
import threading
from tkinter.messagebox import showinfo
class OtherProgramsFrame(CTkFrame):
    def __init__(self, master, show_frame_callback):
        CTkFrame.__init__(self, master=master, fg_color='transparent')
        
        self.show_frame = show_frame_callback
        self.repos_list = []
        
        # عنوان صفحه
        title_label = CTkLabel(
            self,
            text="سایر برنامه‌های من",
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
        
        # فریم برای نمایش ریپوزیتوری‌ها
        self.repos_frame = CTkScrollableFrame(
            self,
            width=600, height=400,
            fg_color='transparent'
        )
        self.repos_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # پیام وضعیت
        self.status_label = CTkLabel(
            self.repos_frame,
            text="در حال بارگذاری اطلاعات...",
            font=CTkFont('B Titr', 16),
            text_color='silver'
        )
        self.status_label.pack(pady=50)
        
        # دکمه بررسی مجدد
        self.refresh_btn = CTkButton(
            self,
            text="بررسی مجدد",
            width=150, height=35,
            corner_radius=5,
            fg_color=color_buttons,
            hover_color='gray',
            command=self.load_repos_thread
        )
        self.refresh_btn.pack(pady=10)
        all_buttons.append(self.refresh_btn)
        
        # بارگذاری اطلاعات در thread جداگانه
        self.load_repos_thread()
    
    def load_repos_thread(self):
        """بارگذاری ریپوزیتوری‌ها در thread جداگانه"""
        self.status_label.configure(text="در حال بارگذاری اطلاعات...")
        self.status_label.pack(pady=50)
        
        # پاک کردن ویجت‌های قبلی
        for widget in self.repos_frame.winfo_children():
            if widget != self.status_label:
                widget.destroy()
        
        thread = threading.Thread(target=self.load_repos)
        thread.daemon = True
        thread.start()
    
    def load_repos(self):
        """بارگذاری لیست ریپوزیتوری‌ها"""
        repos = get_github_repos()
        
        # به‌روزرسانی در thread اصلی
        self.after(0, self.display_repos, repos)
    
    def display_repos(self, repos):
        """نمایش ریپوزیتوری‌ها در صفحه"""
        self.status_label.pack_forget()
        
        if repos is None:
            error_label = CTkLabel(
                self.repos_frame,
                text="خطا در ارتباط با گیت‌هاب",
                font=CTkFont('B Titr', 18),
                text_color='red'
            )
            error_label.pack(pady=50)
            return
        
        if len(repos) == 0:
            empty_label = CTkLabel(
                self.repos_frame,
                text="هیچ برنامه دیگری یافت نشد",
                font=CTkFont('B Titr', 18),
                text_color='silver'
            )
            empty_label.pack(pady=50)
            return
        
        # نمایش هر ریپوزیتوری
        for i, repo in enumerate(repos):
            self.create_repo_widget(repo, i)
    
    def create_repo_widget(self, repo, index):
        """ایجاد ویجت برای نمایش یک ریپوزیتوری"""
        repo_frame = CTkFrame(
            self.repos_frame,
            fg_color='gray17',
            corner_radius=10,
            border_width=1,
            border_color='gray'
        )
        repo_frame.pack(fill='x', pady=5, padx=10)
        
        # نام ریپوزیتوری
        name_label = CTkLabel(
            repo_frame,
            text=repo['name'],
            font=CTkFont('B Titr', 18, 'bold'),
            text_color=color_buttons,
            anchor='w'
        )
        name_label.pack(anchor='w', padx=10, pady=(5, 0))
        
        # توضیحات
        description = repo['description'] or 'بدون توضیحات'
        desc_label = CTkLabel(
            repo_frame,
            text=description,
            font=CTkFont('B Titr', 12),
            text_color='silver',
            anchor='w',
            wraplength=500
        )
        desc_label.pack(anchor='w', padx=10, pady=(0, 5))
        
        # فریم برای دکمه‌ها
        btn_frame = CTkFrame(repo_frame, fg_color='transparent')
        btn_frame.pack(anchor='e', padx=10, pady=5)
        
        # دکمه مشاهده در گیت‌هاب
        view_btn = CTkButton(
            btn_frame,
            text="مشاهده در گیت‌هاب",
            width=120, height=25,
            corner_radius=5,
            fg_color=color_buttons,
            hover_color='gray',
            command=lambda url=repo['html_url']: webbrowser.open(url)
        )
        view_btn.pack(side='right', padx=5)
        all_buttons.append(view_btn)
        
        # دکمه اطلاعات بیشتر
        info_btn = CTkButton(
            btn_frame,
            text="اطلاعات بیشتر",
            width=100, height=25,
            corner_radius=5,
            fg_color='gray',
            hover_color='darkgray',
            command=lambda r=repo: self.show_repo_info(r)
        )
        info_btn.pack(side='right', padx=5)
        all_buttons.append(info_btn)
    
    def show_repo_info(self, repo):
        """نمایش اطلاعات بیشتر ریپوزیتوری"""
        info_text = f"""
نام: {repo['name']}
توضیحات: {repo['description'] or 'بدون توضیحات'}
زبان: {repo['language'] or 'نامشخص'}
ستاره‌ها: {repo['stargazers_count']}
تاریخ ایجاد: {repo['created_at'][:10]}
آخرین به‌روزرسانی: {repo['updated_at'][:10]}
لینک: {repo['html_url']}
        """
        
        showinfo(f"اطلاعات {repo['name']}", info_text)