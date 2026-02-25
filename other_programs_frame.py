# _____________________________ other_programs_frame.py _____________________________
from customtkinter import *
import webbrowser
from tkinter.messagebox import showinfo, showerror
from github_manager import get_github_repos, get_repo_info, GITHUB_PROFILE_URL
from languages import get_text
from constants import color_buttons, all_buttons
import threading
import time

class OtherProgramsFrame(CTkFrame):
    def __init__(self, master, show_frame_callback):
        CTkFrame.__init__(self, master=master, fg_color='transparent')
        
        self.show_frame = show_frame_callback
        self.repos_list = []
        self._loading = False
        
        # عنوان صفحه
        title_label = CTkLabel(
            self,
            text=get_text('other_programs_title'),
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
            text=get_text('loading_repos'),
            font=CTkFont('B Titr', 16),
            text_color='silver'
        )
        self.status_label.pack(pady=50)
        
        # دکمه بررسی مجدد
        self.refresh_btn = CTkButton(
            self,
            text=get_text('refresh'),
            width=150, height=35,
            corner_radius=5,
            fg_color=color_buttons,
            hover_color='gray',
            command=self.load_repos_thread
        )
        self.refresh_btn.pack(pady=10)
        all_buttons.append(self.refresh_btn)
        
        # بارگذاری اطلاعات
        self.after(100, self.load_repos_thread)  # تاخیر برای اطمینان
    
    def load_repos_thread(self):
        """بارگذاری ریپوزیتوری‌ها در thread جداگانه"""
        if self._loading:
            return
        
        self._loading = True
        self.status_label.configure(text=get_text('loading_repos'))
        self.status_label.pack(pady=50)
        
        # پاک کردن ویجت‌های قبلی
        for widget in self.repos_frame.winfo_children():
            if widget != self.status_label:
                widget.destroy()
        
        # اجرای thread
        thread = threading.Thread(target=self._load_repos_worker)
        thread.daemon = True
        thread.start()
    
    def _load_repos_worker(self):
        """کارگر thread برای بارگذاری ریپوزیتوری‌ها"""
        try:
            # این عملیات سنگین در thread انجام می‌شه
            repos = get_github_repos()
            
            # برگشت به thread اصلی برای به‌روزرسانی UI
            if self.winfo_exists():
                self.after(0, lambda: self._display_repos_result(repos))
        except Exception as e:
            print(f"Error in load_repos thread: {e}")
            if self.winfo_exists():
                self.after(0, lambda: self._show_error_result(str(e)))
        finally:
            self._loading = False
    
    def _display_repos_result(self, repos):
        """نمایش نتیجه در thread اصلی"""
        try:
            self.status_label.pack_forget()
            
            if repos is None:
                error_label = CTkLabel(
                    self.repos_frame,
                    text=get_text('github_error'),
                    font=CTkFont('B Titr', 18),
                    text_color='red'
                )
                error_label.pack(pady=50)
                return
            
            if len(repos) == 0:
                empty_label = CTkLabel(
                    self.repos_frame,
                    text=get_text('no_other_programs'),
                    font=CTkFont('B Titr', 18),
                    text_color='silver'
                )
                empty_label.pack(pady=50)
                return
            
            # نمایش هر ریپوزیتوری
            for i, repo in enumerate(repos):
                self._create_repo_widget(repo, i)
        except Exception as e:
            print(f"Error in display_repos: {e}")
    
    def _show_error_result(self, error_msg):
        """نمایش خطا در thread اصلی"""
        try:
            self.status_label.pack_forget()
            error_label = CTkLabel(
                self.repos_frame,
                text=f"{get_text('github_error')}\n{error_msg}",
                font=CTkFont('B Titr', 18),
                text_color='red'
            )
            error_label.pack(pady=50)
        except:
            pass
    
    def _create_repo_widget(self, repo, index):
        """ایجاد ویجت برای نمایش یک ریپوزیتوری"""
        try:
            repo_frame = CTkFrame(
                self.repos_frame,
                fg_color=color_buttons,
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
            description = repo['description'] or get_text('no_description')
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
                text=get_text('view_on_github'),
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
                text=get_text('more_info'),
                width=100, height=25,
                corner_radius=5,
                fg_color=color_buttons,
                hover_color='darkgray',
                command=lambda r=repo: self._show_repo_info(r)
            )
            info_btn.pack(side='right', padx=5)
            all_buttons.append(info_btn)
            
            # دکمه دانلود
            download_btn = CTkButton(
                btn_frame,
                text='📥 ' + get_text('download'),
                width=100, height=25,
                corner_radius=5,
                fg_color=color_buttons,
                hover_color=color_buttons,
                command=lambda r=repo: self._download_repo(r)
            )
            download_btn.pack(side='right', padx=5)
            all_buttons.append(download_btn)
        except Exception as e:
            print(f"Error creating repo widget: {e}")
    
    def _download_repo(self, repo):
        """دانلود ریپوزیتوری به صورت ZIP"""
        import requests
        from tkinter import filedialog
        
        try:
            save_path = filedialog.asksaveasfilename(
                defaultextension='.zip',
                initialfile=f"{repo['name']}.zip",
                filetypes=[('ZIP files', '*.zip'), ('All files', '*.*')],
                title=get_text('select_folder')
            )
            
            if save_path:
                download_url = f"{repo['html_url']}/archive/refs/heads/main.zip"
                response = requests.get(download_url, stream=True)
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                showinfo(get_text('download'), f"{get_text('file_selected')}: {save_path}")
        except Exception as e:
            showerror(get_text('error'), f"{get_text('download_error')}: {str(e)}")
    
    def _show_repo_info(self, repo):
        """نمایش اطلاعات بیشتر ریپوزیتوری"""
        try:
            info_text = f"""
{get_text('description')}: {repo['description'] or get_text('no_description')}
{get_text('language_colon')}: {repo['language'] or get_text('unknown')}
{get_text('stars')}: {repo['stargazers_count']}
{get_text('created_at')}: {repo['created_at'][:10]}
{get_text('updated_at')}: {repo['updated_at'][:10]}
{get_text('link')}: {repo['html_url']}
            """
            
            showinfo(f"{get_text('more_info')} {repo['name']}", info_text)
        except Exception as e:
            showerror(get_text('error'), str(e))