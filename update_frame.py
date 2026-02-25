# _____________________________ update_frame.py _____________________________
from customtkinter import *
from tkinter.messagebox import showinfo, showwarning, askyesno,showerror
from github_manager import (
    get_current_version, download_and_replace_files, 
    compare_versions_info, restart_program
)
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
        
        title_label = CTkLabel(
            self,
            text=get_text('update_title'),
            font=CTkFont('B Titr', 30),
            text_color='white'
        )
        title_label.pack(pady=(30, 20))
        
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
        
        main_frame = CTkFrame(self, fg_color='transparent')
        main_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        self.current_version_label = CTkLabel(
            main_frame,
            text=get_text('current_version_checking'),
            font=CTkFont('B Titr', 18),
            text_color='silver'
        )
        self.current_version_label.pack(pady=10)
        
        self.github_version_label = CTkLabel(
            main_frame,
            text=get_text('latest_version_checking'),
            font=CTkFont('B Titr', 18),
            text_color='silver'
        )
        self.github_version_label.pack(pady=10)
        
        self.status_label = CTkLabel(
            main_frame,
            text="",
            font=CTkFont('B Titr', 16),
            text_color='yellow'
        )
        self.status_label.pack(pady=10)
        
        self.progress_bar = CTkProgressBar(
            main_frame,
            width=400,
            height=20,
            progress_color=color_buttons
        )
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        self.progress_bar.pack_forget()
        
        button_frame = CTkFrame(main_frame, fg_color='transparent')
        button_frame.pack(pady=20)
        
        self.check_btn = CTkButton(
            button_frame,
            text=get_text('check_update'),
            width=200, height=40,
            corner_radius=8,
            fg_color=color_buttons,
            hover_color='gray',
            font=CTkFont('B Titr', 16),
            command=self.check_update_thread
        )
        self.check_btn.pack(side='left', padx=10)
        all_buttons.append(self.check_btn)
        
        self.update_btn = CTkButton(
            button_frame,
            text=get_text('start_update'),
            width=200, height=40,
            corner_radius=8,
            fg_color='green',
            hover_color='darkgreen',
            font=CTkFont('B Titr', 16),
            command=self.start_update_thread
        )
        all_buttons.append(self.update_btn)
        
        self.load_initial_info()
    
    def load_initial_info(self):
        current_version = get_current_version()
        if current_version:
            self.current_version_label.configure(
                text=f"{get_text('current_version')}: {current_version}",
                text_color='silver'
            )
        else:
            self.current_version_label.configure(
                text=get_text('current_version_unknown'),
                text_color='red'
            )
    
    def check_update_thread(self):
        if self.is_checking:
            return
        
        self.is_checking = True
        self.check_btn.configure(state='disabled', text=get_text('checking'))
        self.status_label.configure(text=get_text('connecting_github'), text_color='yellow')
        
        self.update_btn.pack_forget()
        
        thread = threading.Thread(target=self.check_update)
        thread.daemon = True
        thread.start()
    
    def check_update(self):
        version_info = compare_versions_info()
        
        # استفاده از winfo_toplevel برای دسترسی به پنجره اصلی
        root = self.winfo_toplevel()
        root.after_idle(lambda: self.show_update_result(version_info))
    
    def show_update_result(self, version_info):
        self.is_checking = False
        self.check_btn.configure(state='normal', text=get_text('check_again'))
        
        if version_info['github'] is None:
            self.status_label.configure(
                text=get_text('github_connection_error'),
                text_color='red'
            )
            return
        
        self.github_version_label.configure(
            text=f"{get_text('latest_version')}: {version_info['github']}",
            text_color='silver'
        )
        
        if version_info['is_up_to_date']:
            self.status_label.configure(
                text=f"{get_text('app_up_to_date')} ({version_info['local']})",
                text_color='green'
            )
            showinfo(
                get_text('update'), 
                f"{get_text('app_up_to_date')}\n{get_text('current_version')}: {version_info['local']}"
            )
        elif version_info['needs_downgrade']:
            self.status_label.configure(
                text=f"{get_text('latest_version')}: {version_info['github']}",
                text_color='orange'
            )
            showwarning(
                get_text('update'),
                f"{get_text('current_version')}: {version_info['local']}\n"
                f"{get_text('latest_version')}: {version_info['github']}\n\n"
                f"{get_text('app_up_to_date')}"
            )
        else:
            self.status_label.configure(
                text=get_text('new_version_available').format(version_info['github']),
                text_color='orange'
            )
            
            self.update_btn.pack(side='left', padx=10)
            
            if askyesno(
                get_text('update'), 
                f"{get_text('new_version_found')}: {version_info['github']}\n"
                f"{get_text('current_version')}: {version_info['local']}\n\n"
                f"{get_text('update_question')}\n"
                f"{get_text('update_note')}"
            ):
                self.start_update_thread()
    def start_update_thread(self):
        if self.is_updating:
            return
        
        self.is_updating = True
        self.check_btn.configure(state='disabled')
        self.update_btn.configure(state='disabled', text=get_text('updating'))
        
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        
        self.status_label.configure(text=get_text('downloading_updating'), text_color='yellow')
        
        thread = threading.Thread(target=self.perform_update)
        thread.daemon = True
        thread.start()
    
    def perform_update(self):
        def update_progress(percent):
            root = self.winfo_toplevel()
            root.after_idle(lambda: self.progress_bar.set(percent / 100))
        
        success = download_and_replace_files(update_progress)
        
        root = self.winfo_toplevel()
        root.after_idle(lambda: self.show_update_result_final(success))
    
    def show_update_result_final(self, success):
        self.is_updating = False
        self.progress_bar.pack_forget()
        
        if success:
            new_version = get_current_version()
            
            self.status_label.configure(
                text=get_text('update_successful').format(new_version),
                text_color='green'
            )
            
            if askyesno(
                get_text('update_successful_title'),
                f"{get_text('update_successful_message')} {new_version}\n\n"
                f"{get_text('restart_question')}"
            ):
                self.status_label.configure(text=get_text('restarting'))
                self.update_btn.configure(state='disabled')
                self.check_btn.configure(state='disabled')
                
                root = self.winfo_toplevel()
                root.after(1000, self.restart_application)
            else:
                self.current_version_label.configure(
                    text=f"{get_text('current_version')}: {new_version}",
                    text_color='silver'
                )
                
                self.github_version_label.configure(
                    text=f"{get_text('latest_version')}: {new_version}",
                    text_color='silver'
                )
                
                self.update_btn.pack_forget()
                
                if self.on_update_complete:
                    self.on_update_complete()
        else:
            self.status_label.configure(
                text=get_text('update_error'),
                text_color='red'
            )
            self.update_btn.configure(state='normal', text=get_text('start_update'))
        
        self.check_btn.configure(state='normal')
    
    def restart_application(self):
        try:
            restart_program()
        except Exception as e:
            showerror(get_text('erorr'), f"{get_text('restart_error')}: {str(e)}")