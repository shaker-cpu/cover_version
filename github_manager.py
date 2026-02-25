# _____________________________ github_manager.py _____________________________
import requests
import os
import shutil
import zipfile
import subprocess
import sys
from tkinter.messagebox import showerror
from constants import here
from languages import get_text
import tempfile

# آدرس‌های گیت‌هاب
GITHUB_USERNAME = 'shaker-cpu'
REPO_NAME = 'cover_version'
VERSION_FILE = 'ver.txt'
GITHUB_API = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents'
RAW_CONTENT_URL = f'https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main'
REPO_URL = f'https://github.com/{GITHUB_USERNAME}'

# لیست فایل‌ها و پوشه‌هایی که نباید کپی شوند
EXCLUDED_FILES = [
    '.gitignore',
    'README.md',
    'README',
    '.git',
    '.github',
    '.vscode',
    '.idea',
    '__pycache__',
    '*.pyc',
    '*.pyo',
    '*.pyd',
    '.DS_Store',
    'Thumbs.db',
    '*.log',
    '*.tmp',
    '*.temp',
    'venv',
    'env',
    '.env',
    'dist',
    'build',
    '*.egg-info'
]

def should_exclude_file(filename):
    """بررسی اینکه آیا فایل باید نادیده گرفته شود"""
    if filename in EXCLUDED_FILES:
        return True
    
    for pattern in EXCLUDED_FILES:
        if pattern.startswith('*') and filename.endswith(pattern[1:]):
            return True
    
    return False

def should_exclude_dir(dirname):
    """بررسی اینکه آیا پوشه باید نادیده گرفته شود"""
    return dirname in EXCLUDED_FILES

def get_github_repos():
    """دریافت لیست ریپوزیتوری‌های کاربر از گیت‌هاب"""
    try:
        url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            repos = response.json()
            other_repos = [repo for repo in repos if repo['name'] != REPO_NAME]
            return other_repos
        else:
            return None
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return None

def get_current_version():
    """دریافت نسخه فعلی برنامه از فایل ver.txt محلی"""
    try:
        version_file_path = os.path.join(here, VERSION_FILE)
        if os.path.exists(version_file_path):
            with open(version_file_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        return None
    except Exception as e:
        print(f"Error reading local version: {e}")
        return None

def get_github_version():
    """دریافت نسخه از گیت‌هاب"""
    try:
        url = f'{RAW_CONTENT_URL}/{VERSION_FILE}'
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.text.strip()
        else:
            return None
    except Exception as e:
        print(f"Error fetching github version: {e}")
        return None

def compare_versions(version1, version2):
    """
    مقایسه دو نسخه به صورت عددی
    returns:
        1 اگر version1 > version2
        0 اگر version1 == version2
        -1 اگر version1 < version2
    """
    if version1 is None or version2 is None:
        return None
    
    try:
        # تبدیل نسخه‌ها به لیست اعداد
        v1_parts = [int(x) for x in version1.split('.')]
        v2_parts = [int(x) for x in version2.split('.')]
        
        # هم‌اندازه کردن لیست‌ها
        max_len = max(len(v1_parts), len(v2_parts))
        v1_parts.extend([0] * (max_len - len(v1_parts)))
        v2_parts.extend([0] * (max_len - len(v2_parts)))
        
        # مقایسه جزء به جزء
        for i in range(max_len):
            if v1_parts[i] > v2_parts[i]:
                return 1
            elif v1_parts[i] < v2_parts[i]:
                return -1
        
        return 0
    except Exception as e:
        print(f"Error comparing versions: {e}")
        # اگر خطایی رخ داد، مقایسه رشته‌ای انجام بده
        if version1 > version2:
            return 1
        elif version1 < version2:
            return -1
        else:
            return 0

def download_and_replace_files(progress_callback=None):
    """دانلود تمام فایل‌های ریپوزیتوری و جایگزینی با فایل‌های فعلی"""
    try:
        api_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/zipball/main'
        response = requests.get(api_url, stream=True, timeout=30)
        
        if response.status_code != 200:
            showerror(get_text('erorr'), "خطا در دانلود فایل‌ها")
            return False
        
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_path = os.path.join(temp_dir, 'update.zip')
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if progress_callback and total_size:
                            progress = (downloaded / total_size) * 100
                            progress_callback(progress)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            
            extracted_dirs = [d for d in os.listdir(temp_dir) 
                            if os.path.isdir(os.path.join(temp_dir, d))]
            source_dir = None
            for d in extracted_dirs:
                if d.startswith(f'{GITHUB_USERNAME}-{REPO_NAME}') or d.startswith(f'{REPO_NAME}'):
                    source_dir = os.path.join(temp_dir, d)
                    break
            
            if not source_dir:
                showerror(get_text('erorr'), "خطا در استخراج فایل‌ها")
                return False
            
            copied_files_count = 0
            skipped_files_count = 0
            
            for root, dirs, files in os.walk(source_dir):
                dirs[:] = [d for d in dirs if not should_exclude_dir(d)]
                
                rel_path = os.path.relpath(root, source_dir)
                
                if any(should_exclude_dir(part) for part in rel_path.split(os.sep)):
                    continue
                
                dest_dir = os.path.join(here, rel_path) if rel_path != '.' else here
                if not os.path.exists(dest_dir) and rel_path != '.':
                    os.makedirs(dest_dir, exist_ok=True)
                
                for file in files:
                    if should_exclude_file(file):
                        skipped_files_count += 1
                        continue
                    
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_dir, file)
                    
                    try:
                        shutil.copy2(src_file, dest_file)
                        copied_files_count += 1
                    except Exception as e:
                        print(f"Error copying {file}: {e}")
                        skipped_files_count += 1
            
            github_version = get_github_version()
            if github_version:
                try:
                    with open(os.path.join(here, VERSION_FILE), 'w', encoding='utf-8') as f:
                        f.write(github_version)
                    print(f"Version file updated to: {github_version}")
                except Exception as e:
                    print(f"Error updating version file: {e}")
            
            print(f"Update completed: {copied_files_count} files copied, {skipped_files_count} files skipped")
            return True
            
    except Exception as e:
        print(f"Error updating files: {e}")
        showerror(get_text('erorr'), f"خطا در به‌روزرسانی: {str(e)}")
        return False

def get_repo_info(repo_name):
    """دریافت اطلاعات یک ریپوزیتوری خاص"""
    try:
        url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}'
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching repo info: {e}")
        return None
def compare_versions_info():
    """مقایسه نسخه محلی با نسخه گیت‌هاب با استفاده از مقایسه عددی"""
    
    
    local_version = get_current_version()
    github_version = get_github_version()
    
    if local_version is None or github_version is None:
        return {
            'local': local_version,
            'github': github_version,
            'is_up_to_date': False,
            'update_available': False,
            'needs_downgrade': False,
            'comparison_result': None
        }
    
    comparison = compare_versions(github_version, local_version)
    
    return {
        'local': local_version,
        'github': github_version,
        'is_up_to_date': comparison == 0,
        'update_available': comparison > 0,
        'needs_downgrade': comparison < 0,
        'comparison_result': comparison
    }
def restart_program():
    """بستن برنامه فعلی و راه‌اندازی مجدد آن"""
    try:
        python = sys.executable
        script = os.path.join(here, 'main.py')
        
        subprocess.Popen([python, script])
        
        sys.exit(0)
    except Exception as e:
        print(f"Error restarting program: {e}")
        showerror(get_text('erorr'), f"خطا در راه‌اندازی مجدد: {str(e)}")