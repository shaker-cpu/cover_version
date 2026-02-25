# _____________________________ languages.py _____________________________
# دیکشنری چند زبانه برای برنامه

languages = {
    'persian': {
        # ========== عناوین اصلی ==========
        'app_title': 'برنامه ساخت جلد',
        'theme_button': '🎨 تم ها',
        'history_button': 'تاریخچه',
        'guide_button': ' راهنما',
        'language': 'زبان',
        "erorr":"خطا",
        
        # ========== کلمات جدید برای دکمه درباره ما ==========
        'about_button': '📋 درباره ما',
        'about_title': 'درباره برنامه',
        'about_message': '''📱 برنامه ساخت جلد

توسعه دهندگان : آقایان مقیسه و شاکر

📅 نسخه: {}
📧 پشتیبانی: support@example.com
📞 تلفن: ۰۲۱-۱۲۳۴۵۶۷۸

⭐ این برنامه برای ساخت انواع جلد طراحی شده است.
❤️ با تشکر از انتخاب شما''',
        
        # ========== کلمات جدید برای صفحه برنامه‌های دیگر ==========
        'other_programs': '📦 برنامه‌های دیگر',
        'other_programs_title': 'سایر برنامه‌های من',
        'loading_repos': 'در حال بارگذاری اطلاعات...',
        'github_error': 'خطا در ارتباط با گیت‌هاب',
        'no_other_programs': 'هیچ برنامه دیگری یافت نشد',
        'view_on_github': 'مشاهده در گیت‌هاب',
        'more_info': 'اطلاعات بیشتر',
        'refresh': 'بررسی مجدد',
        'description': 'توضیحات',
        'no_description': 'بدون توضیحات',
        'unknown': 'نامشخص',
        'language_colon': 'زبان',
        'stars': 'ستاره‌ها',
        'created_at': 'تاریخ ایجاد',
        'updated_at': 'آخرین به‌روزرسانی',
        'link': 'لینک',
        
        # ========== کلمات جدید برای صفحه به‌روزرسانی ==========
        'update_title': 'بررسی به‌روزرسانی',
        'current_version_checking': 'نسخه فعلی: در حال بررسی...',
        'latest_version_checking': 'آخرین نسخه: در حال بررسی...',
        'current_version': 'نسخه فعلی',
        'current_version_unknown': 'نسخه فعلی: نامشخص',
        'latest_version': 'آخرین نسخه',
        'check_update': 'بررسی به‌روزرسانی',
        'check_again': 'بررسی مجدد',
        'start_update': 'شروع به‌روزرسانی',
        'checking': 'در حال بررسی...',
        'connecting_github': 'در حال ارتباط با گیت‌هاب...',
        'github_connection_error': 'خطا در ارتباط با گیت‌هاب',
        'app_up_to_date': 'برنامه شما به‌روز است',
        'new_version_available': 'نسخه جدید {} موجود است',
        'new_version_found': 'نسخه جدید',
        'update_question': 'آیا می‌خواهید به‌روزرسانی کنید؟',
        'update_note': 'توجه: فایل‌های .gitignore و README.md به‌روزرسانی نمی‌شوند.',
        'updating': 'در حال به‌روزرسانی...',
        'downloading_updating': 'در حال دانلود و به‌روزرسانی...',
        'update_successful': 'به‌روزرسانی با موفقیت انجام شد (نسخه {})',
        'update_successful_title': 'به‌روزرسانی موفق',
        'update_successful_message': 'برنامه با موفقیت به نسخه',
        'restart_question': 'برای اعمال تغییرات، برنامه باید مجدداً راه‌اندازی شود. آیا می‌خواهید اکنون راه‌اندازی مجدد شود؟',
        'restarting': 'در حال راه‌اندازی مجدد...',
        'update_error': 'خطا در به‌روزرسانی',
        'restart_error': 'خطا در راه‌اندازی مجدد',
        'update': 'به‌روزرسانی',
        
        # ========== دکمه‌های ساخت جلد ==========
        'dissertation_cover': 'ساخت جلد\n پایان نامه',
        'notebook_cover': 'ساخت جلد\n  دفتر مدارس یا\n  قراردادها',
        'book_cover': 'ساخت جلد\n  کتاب ها',
        'gilded_book_cover': 'ساخت جلد\n  کتاب های \n  تذهیب دار',
        
        # ========== صفحه تم ==========
        'theme_guide_title': 'راهنمای تنظیم تم برنامه',
        'theme_guide_message': 'یکی از رنگ ها را انتخاب کنید تا رنگ تمام دکمه های برنامه عوض شود',
        'background_color': 'رنگ پس زمینه',
        
        # ========== صفحه تاریخچه ==========
        'history_guide_title': 'راهنمای صفحه تاریخچه',
        'history_guide_message': 'در این صفحه شما می توانید آخرین ۵ فایل ساخته شده را ببینید',
        
        # ========== صفحه راهنمای پایان‌نامه ==========
        'step1': 'مرحله ۱',
        'step2': 'مرحله ۲',
        'step3': 'مرحله ۳',
        'step4': 'مرحله ۴',
        'help_plan_1':'راهنمای مرحله اول',
        'help_plan_2':'راهنمای مرحله دوم',
        'help_plan_3':'راهنمای مرحله سوم',
        'help_plan_4':'راهنمای مرحله چهارم',
        
        # ========== صفحه ساخت جلد پایان‌نامه ==========
        'spine_value': ':(mm)مقدار عطف ',
        'title_text': ':عنوان ',
        'author_name': ':نام نویسنده ',
        'date': ':تاریخ ',
        'title_page_number': ': شماره صفحه عنوان ',
        'output_file_name': ':نام فایل خروجی ',
        'select_file': 'انتخاب فایل ',
        'save_location': 'محل ذخیره ',
        'no_file_selected': 'فایلی انتخاب نشده است',
        'no_folder_selected': 'پوشه ای انتخاب نشده است',
        'no_logo_selected': 'لوگو انتخاب نشده است',
        'file_selected': 'فایل انتخاب شد',
        'folder_selected': 'پوشه انتخاب شد',
        'logo_selected': 'لوگو انتخاب شد',
        
        # ========== چک باکس‌ها ==========
        'has_latin_page': 'پایان نامه صفحه لاتین دارد',
        'has_latin_page_on': 'دارای صفحه لاتین',
        'has_latin_page_off': 'بدون صفحه لاتین',
        'logo_black_white': 'لوگوی پایان نامه سیاه و سفید است',
        'logo_black_white_on': 'سیاه و سفید',
        'logo_black_white_off': 'رنگی',
        'logo_circular': 'لوگوی پایان نامه دایره ای است',
        'logo_circular_on': 'دایره ای',
        'logo_circular_off': 'غیر دایره ای',
        
        # ========== دکمه‌های عملیاتی ==========
        'refresh': 'پاکسازی صفحه',
        'start_making': 'شروع ساخت',
        'load_logo': 'بارگذاری لوگو',
        'back': '🔙 بازگشت',
        'cancel': 'انصراف',
        'apply': 'اعمال',
        
        # ========== صفحه انتخاب تاریخ ==========
        'select_year': 'انتخاب سال',
        'select_month': 'انتخاب ماه',
        'selected_date': ':تاریخ انتخاب شده ',
        
        # ========== ماه‌ها ==========
        'months': ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
                   'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'],
        
        # ========== شماره صفحات ==========
        'pages': ['۱ صفحه', '۲ صفحه', '۳ صفحه', '۴ صفحه', '۵ صفحه'],
        
        # ========== راهنمای شروع ==========
        'welcome_message': '''بسم الله الرحمن الرحیم
سلام به برنامه ساخت جلد خوش آمدید
برای ساخت هر نوع جلد روی کلید مربوطه کلیک نمائید''',
        
        # ========== درباره ما ==========
        'about_us': '''📱 برنامه ساخت جلد

توسعه دهندگان : آقایان مقیسه و شاکر

📅 نسخه: {}
📧 پشتیبانی: support@example.com
📞 تلفن: ۰۲۱-۱۲۳۴۵۶۷۸

⭐ این برنامه برای ساخت انواع جلد طراحی شده است.

❤️ با تشکر از انتخاب شما''',
    },
    
    'english': {
        # ========== Main Titles ==========
        'app_title': 'Cover Builder',
        'theme_button': '🎨 Themes',
        'history_button': 'History',
        'guide_button': ' Guide',
        'language': 'Language',
        "erorr":'error',
        
        # ========== New words for About button ==========
        'about_button': '📋 About Us',
        'about_title': 'About App',
        'about_message': '''📱 Cover Builder

Developers: Moghiseh & Shaker

📅 Version: {}
📧 Support: support@example.com
📞 Phone: +98-21-12345678

⭐ Designed for creating various covers
❤️ Thank you for choosing us''',
        
        # ========== New words for Other Programs page ==========
        'other_programs': '📦 Other Programs',
        'other_programs_title': 'My Other Programs',
        'loading_repos': 'Loading information...',
        'github_error': 'Error connecting to GitHub',
        'no_other_programs': 'No other programs found',
        'view_on_github': 'View on GitHub',
        'more_info': 'More Info',
        'refresh': 'Refresh',
        'description': 'Description',
        'no_description': 'No description',
        'unknown': 'Unknown',
        'language_colon': 'Language',
        'stars': 'Stars',
        'created_at': 'Created at',
        'updated_at': 'Updated at',
        'link': 'Link',
        
        # ========== New words for Update page ==========
        'update_title': 'Check for Updates',
        'current_version_checking': 'Current version: Checking...',
        'latest_version_checking': 'Latest version: Checking...',
        'current_version': 'Current version',
        'current_version_unknown': 'Current version: Unknown',
        'latest_version': 'Latest version',
        'check_update': 'Check for Updates',
        'check_again': 'Check Again',
        'start_update': 'Start Update',
        'checking': 'Checking...',
        'connecting_github': 'Connecting to GitHub...',
        'github_connection_error': 'Error connecting to GitHub',
        'app_up_to_date': 'Your app is up to date',
        'new_version_available': 'New version {} available',
        'new_version_found': 'New version',
        'update_question': 'Do you want to update?',
        'update_note': 'Note: .gitignore and README.md files will not be updated.',
        'updating': 'Updating...',
        'downloading_updating': 'Downloading and updating...',
        'update_successful': 'Update successful (version {})',
        'update_successful_title': 'Update Successful',
        'update_successful_message': 'App successfully updated to version',
        'restart_question': 'To apply changes, the app needs to restart. Do you want to restart now?',
        'restarting': 'Restarting...',
        'update_error': 'Update error',
        'restart_error': 'Restart error',
        'update': 'Update',
        
        # ========== Cover Buttons ==========
        'dissertation_cover': 'Dissertation\n Cover',
        'notebook_cover': 'Notebook\n or Contract\n Cover',
        'book_cover': 'Book\n Cover',
        'gilded_book_cover': 'Gilded\n Book Cover',
        
        # ========== Theme Page ==========
        'theme_guide_title': 'Theme Settings Guide',
        'theme_guide_message': 'Select a color to change all button colors',
        'background_color': 'Background Color',
        
        # ========== History Page ==========
        'history_guide_title': 'History Guide',
        'history_guide_message': 'You can see the last 5 created files here',
        
        # ========== Dissertation Guide Page ==========
        'step1': 'Step 1',
        'step2': 'Step 2',
        'step3': 'Step 3',
        'step4': 'Step 4',
        'help_plan_1':'First step guide',
        'help_plan_2':'Second step guide',
        'help_plan_3':'Third step guide',
        'help_plan_4':'Fourth step guide',
        
        # ========== Dissertation Cover Page ==========
        'spine_value': 'Spine Value (mm):',
        'title_text': 'Title:',
        'author_name': 'Author Name:',
        'date': 'Date:',
        'title_page_number': 'Title Page Number:',
        'output_file_name': 'Output File Name:',
        'select_file': 'Select File',
        'save_location': 'Save Location',
        'no_file_selected': 'No file selected',
        'no_folder_selected': 'No folder selected',
        'no_logo_selected': 'No logo selected',
        'file_selected': 'File selected',
        'folder_selected': 'Folder selected',
        'logo_selected': 'Logo selected',
        
        # ========== Checkboxes ==========
        'has_latin_page': 'Dissertation has Latin page',
        'has_latin_page_on': 'Has Latin page',
        'has_latin_page_off': 'No Latin page',
        'logo_black_white': 'Logo is black and white',
        'logo_black_white_on': 'Black and White',
        'logo_black_white_off': 'Colored',
        'logo_circular': 'Logo is circular',
        'logo_circular_on': 'Circular',
        'logo_circular_off': 'Non-circular',
        
        # ========== Action Buttons ==========
        'refresh': 'Refresh Page',
        'start_making': 'Start Making',
        'load_logo': 'Load Logo',
        'back': '🔙 Back',
        'cancel': 'Cancel',
        'apply': 'Apply',
        
        # ========== Date Selection Page ==========
        'select_year': 'Select Year',
        'select_month': 'Select Month',
        'selected_date': 'Selected Date:',
        
        # ========== Pages ==========
        'pages': ['1 Page', '2 Pages', '3 Pages', '4 Pages', '5 Pages'],
        
        # ========== Welcome Message ==========
        'welcome_message': '''Welcome to Cover Builder
Click on any cover button to start''',
        
        # ========== About Us ==========
        'about_us': '''📱 Cover Builder

Developers: Moghiseh & Shaker

📅 Version: {}
📧 Support: support@example.com
📞 Phone: +98-21-12345678

⭐ Designed for creating various covers

❤️ Thank you for choosing us''',
    },
    
    'arabic': {
        # ========== عناوین اصلی ==========
        'app_title': 'بناء الغلاف',
        'theme_button': '🎨 السمات',
        'history_button': 'التاریخ',
        'guide_button': ' الدلیل',
        'language': 'اللغة',
        "erorr":'خطأ ',
        
        # ========== کلمات جدید برای دکمه درباره ما ==========
        'about_button': '📋 معلومات عنا',
        'about_title': 'حول البرنامج',
        'about_message': '''📱 بناء الغلاف

المطورون: مقیسة و شاکر

📅 الإصدار: {}
📧 الدعم: support@example.com
📞 الهاتف: ۹۸۲۱-۱۲۳۴۵۶۷۸+

⭐ تم تصمیم هذا البرنامج لإنشاء أنواع مختلفة من الأغلفة
❤️ شکرًا لاختیارکم لنا''',
        
        # ========== کلمات جدید برای صفحه برنامه‌های دیگر ==========
        'other_programs': '📦 برامج أخرى',
        'other_programs_title': 'برامجى الأخرى',
        'loading_repos': 'جاري تحميل المعلومات...',
        'github_error': 'خطأ في الاتصال بـ GitHub',
        'no_other_programs': 'لم يتم العثور على برامج أخرى',
        'view_on_github': 'عرض على GitHub',
        'more_info': 'مزيد من المعلومات',
        'refresh': 'تحديث',
        'description': 'الوصف',
        'no_description': 'لا يوجد وصف',
        'unknown': 'غير معروف',
        'language_colon': 'اللغة',
        'stars': 'النجوم',
        'created_at': 'تاريخ الإنشاء',
        'updated_at': 'آخر تحديث',
        'link': 'الرابط',
        
        # ========== کلمات جدید برای صفحه به‌روزرسانی ==========
        'update_title': 'التحقق من التحديثات',
        'current_version_checking': 'الإصدار الحالي: جاري التحقق...',
        'latest_version_checking': 'آخر إصدار: جاري التحقق...',
        'current_version': 'الإصدار الحالي',
        'current_version_unknown': 'الإصدار الحالي: غير معروف',
        'latest_version': 'آخر إصدار',
        'check_update': 'التحقق من التحديثات',
        'check_again': 'تحقق مرة أخرى',
        'start_update': 'بدء التحديث',
        'checking': 'جاري التحقق...',
        'connecting_github': 'جاري الاتصال بـ GitHub...',
        'github_connection_error': 'خطأ في الاتصال بـ GitHub',
        'app_up_to_date': 'برنامجك محدث',
        'new_version_available': 'الإصدار الجديد {} متوفر',
        'new_version_found': 'إصدار جديد',
        'update_question': 'هل تريد التحديث؟',
        'update_note': 'ملاحظة: لن يتم تحديث ملفات .gitignore و README.md.',
        'updating': 'جاري التحديث...',
        'downloading_updating': 'جاري التحميل والتحديث...',
        'update_successful': 'تم التحديث بنجاح (الإصدار {})',
        'update_successful_title': 'تحديث ناجح',
        'update_successful_message': 'تم تحديث البرنامج بنجاح إلى الإصدار',
        'restart_question': 'لتطبيق التغييرات، يجب إعادة تشغيل البرنامج. هل تريد إعادة التشغيل الآن؟',
        'restarting': 'جاري إعادة التشغيل...',
        'update_error': 'خطأ في التحديث',
        'restart_error': 'خطأ في إعادة التشغيل',
        'update': 'تحديث',
        
        # ========== أزرار بناء الغلاف ==========
        'dissertation_cover': 'بناء غلاف\n الرسالة',
        'notebook_cover': 'بناء غلاف\n دفتر المدرسة أو\n العقود',
        'book_cover': 'بناء غلاف\n الکتب',
        'gilded_book_cover': 'بناء غلاف\n الکتب المذهبة',
        
        # ========== صفحة السمة ==========
        'theme_guide_title': 'دلیل إعدادات السمة',
        'theme_guide_message': 'اختر لونًا لتغییر لون جمیع الأزرار',
        'background_color': 'لون الخلفیة',
        
        # ========== صفحة التاریخ ==========
        'history_guide_title': 'دلیل صفحة التاریخ',
        'history_guide_message': 'یمکنک رؤية آخر ۵ ملفات تم إنشاؤها هنا',
        
        # ========== صفحة دلیل الرسالة ==========
        'step1': 'الخطوة ۱',
        'step2': 'الخطوة ۲',
        'step3': 'الخطوة ۳',
        'step4': 'الخطوة ۴',
        'help_plan_1':" دليل الخطوة الأولى",
        'help_plan_2':" دليل الخطوة الثانية",
        'help_plan_3':' دليل الخطوة الثالثة',
        'help_plan_4':' دليل الخطوة الرابعة',
                
        # ========== صفحة بناء غلاف الرسالة ==========
        'spine_value': 'قیمة العمود الفقري (ملم):',
        'title_text': 'العنوان:',
        'author_name': 'اسم المؤلف:',
        'date': 'التاریخ:',
        'title_page_number': 'رقم صفحة العنوان:',
        'output_file_name': 'اسم ملف الإخراج:',
        'select_file': 'اختر ملف',
        'save_location': 'مکان الحفظ',
        'no_file_selected': 'لم يتم اختیار ملف',
        'no_folder_selected': 'لم يتم اختیار مجلد',
        'no_logo_selected': 'لم يتم اختیار شعار',
        'file_selected': 'تم اختیار الملف',
        'folder_selected': 'تم اختیار المجلد',
        'logo_selected': 'تم اختیار الشعار',
        
        # ========== مربعات الاختیار ==========
        'has_latin_page': 'الرسالة تحتوي على صفحة لاتینیة',
        'has_latin_page_on': 'تحتوي على صفحة لاتینیة',
        'has_latin_page_off': 'لا تحتوي على صفحة لاتینیة',
        'logo_black_white': 'الشعار أبيض وأسود',
        'logo_black_white_on': 'أبیض وأسود',
        'logo_black_white_off': 'ملون',
        'logo_circular': 'الشعار دائري',
        'logo_circular_on': 'دائري',
        'logo_circular_off': 'غیر دائري',
        
        # ========== أزرار العملیات ==========
        'refresh': 'تحدیث الصفحة',
        'start_making': 'بدء الإنشاء',
        'load_logo': 'تحمیل الشعار',
        'back': '🔙 رجوع',
        'cancel': 'إلغاء',
        'apply': 'تطبیق',
        
        # ========== صفحة اختیار التاریخ ==========
        'select_year': 'اختر السنة',
        'select_month': 'اختر الشهر',
        'selected_date': 'التاریخ المختار:',
        
        # ========== أرقام الصفحات ==========
        'pages': ['۱ صفحة', '۲ صفحتین', '۳ صفحات', '٤ صفحات', '٥ صفحات'],
        
        # ========== رسالة الترحيب ==========
        'welcome_message': '''مرحبًا بكم في بناء الغلاف
انقر على أي زر لبدء الإنشاء''',
        
        # ========== معلومات عنا ==========
        'about_us': '''📱 بناء الغلاف

المطورون: مقیسة و شاکر

📅 الإصدار: {}
📧 الدعم: support@example.com
📞 الهاتف: ۹۸۲۱-۱۲۳۴۵۶۷۸+

⭐ تم تصمیم هذا البرنامج لإنشاء أنواع مختلفة من الأغلفة

❤️ شکرًا لاختیارکم لنا''',
    },
    
    'chinese': {
        # ========== 主要标题 ==========
        'app_title': '封面制作器',
        'theme_button': '🎨 主题',
        'history_button': '历史',
        'guide_button': ' 指南',
        'language': '语言',
        "erorr":'错误 ',
        
        # ========== 关于按钮的新词 ==========
        'about_button': '📋 关于我们',
        'about_title': '关于应用程序',
        'about_message': '''📱 封面制作器

开发者: Moghiseh & Shaker

📅 版本: {}
📧 支持: support@example.com
📞 电话: +98-21-12345678

⭐ 专为创建各种封面而设计
❤️ 感谢您选择我们''',
        
        # ========== 其他程序页面的新词 ==========
        'other_programs': '📦 其他程序',
        'other_programs_title': '我的其他程序',
        'loading_repos': '正在加载信息...',
        'github_error': '连接到GitHub时出错',
        'no_other_programs': '未找到其他程序',
        'view_on_github': '在GitHub上查看',
        'more_info': '更多信息',
        'refresh': '刷新',
        'description': '描述',
        'no_description': '无描述',
        'unknown': '未知',
        'language_colon': '语言',
        'stars': '星标',
        'created_at': '创建于',
        'updated_at': '更新于',
        'link': '链接',
        
        # ========== 更新页面的新词 ==========
        'update_title': '检查更新',
        'current_version_checking': '当前版本: 正在检查...',
        'latest_version_checking': '最新版本: 正在检查...',
        'current_version': '当前版本',
        'current_version_unknown': '当前版本: 未知',
        'latest_version': '最新版本',
        'check_update': '检查更新',
        'check_again': '再次检查',
        'start_update': '开始更新',
        'checking': '正在检查...',
        'connecting_github': '正在连接GitHub...',
        'github_connection_error': '连接到GitHub时出错',
        'app_up_to_date': '您的应用程序已是最新',
        'new_version_available': '新版本 {} 可用',
        'new_version_found': '新版本',
        'update_question': '您想要更新吗？',
        'update_note': '注意：.gitignore 和 README.md 文件将不会被更新。',
        'updating': '正在更新...',
        'downloading_updating': '正在下载和更新...',
        'update_successful': '更新成功 (版本 {})',
        'update_successful_title': '更新成功',
        'update_successful_message': '应用程序成功更新到版本',
        'restart_question': '要应用更改，需要重新启动应用程序。您想现在重新启动吗？',
        'restarting': '正在重新启动...',
        'update_error': '更新错误',
        'restart_error': '重新启动错误',
        'update': '更新',
        
        # ========== 封面按钮 ==========
        'dissertation_cover': '论文\n封面',
        'notebook_cover': '笔记本\n或合同\n封面',
        'book_cover': '书籍\n封面',
        'gilded_book_cover': '烫金\n书籍封面',
        
        # ========== 主题页面 ==========
        'theme_guide_title': '主题设置指南',
        'theme_guide_message': '选择颜色以更改所有按钮颜色',
        'background_color': '背景颜色',
        
        # ========== 历史页面 ==========
        'history_guide_title': '历史指南',
        'history_guide_message': '您可以在这里查看最近创建的5个文件',
        
        # ========== 论文指南页面 ==========
        'step1': '步骤 1',
        'step2': '步骤 2',
        'step3': '步骤 3',
        'step4': '步骤 4',
        'help_plan_1':'第一步指南',
        'help_plan_2':'第二步指南',
        'help_plan_3':'第三步指南',
        'help_plan_4':'第四步指南',

        # ========== 论文封面页面 ==========
        'spine_value': '书脊值 (毫米):',
        'title_text': '标题:',
        'author_name': '作者姓名:',
        'date': '日期:',
        'title_page_number': '标题页数:',
        'output_file_name': '输出文件名:',
        'select_file': '选择文件',
        'save_location': '保存位置',
        'no_file_selected': '未选择文件',
        'no_folder_selected': '未选择文件夹',
        'no_logo_selected': '未选择徽标',
        'file_selected': '已选择文件',
        'folder_selected': '已选择文件夹',
        'logo_selected': '已选择徽标',
        
        # ========== 复选框 ==========
        'has_latin_page': '论文有拉丁页面',
        'has_latin_page_on': '有拉丁页面',
        'has_latin_page_off': '无拉丁页面',
        'logo_black_white': '徽标是黑白的',
        'logo_black_white_on': '黑白',
        'logo_black_white_off': '彩色',
        'logo_circular': '徽标是圆形的',
        'logo_circular_on': '圆形',
        'logo_circular_off': '非圆形',
        
        # ========== 操作按钮 ==========
        'refresh': '刷新页面',
        'start_making': '开始制作',
        'load_logo': '加载徽标',
        'back': '🔙 返回',
        'cancel': '取消',
        'apply': '应用',
        
        # ========== 日期选择页面 ==========
        'select_year': '选择年份',
        'select_month': '选择月份',
        'selected_date': '选择的日期:',
        
        # ========== 页数 ==========
        'pages': ['1 页', '2 页', '3 页', '4 页', '5 页'],
        
        # ========== 欢迎消息 ==========
        'welcome_message': '''欢迎使用封面制作器
点击任何封面按钮开始''',
        
        # ========== 关于我们 ==========
        'about_us': '''📱 封面制作器

开发者: Moghiseh & Shaker

📅 版本: {}
📧 支持: support@example.com
📞 电话: +98-21-12345678

⭐ 专为创建各种封面而设计

❤️ 感谢您选择我们''',
    },
    
    'russian': {
        # ========== Основные заголовки ==========
        'app_title': 'Создатель обложек',
        'theme_button': '🎨 Темы',
        'history_button': 'История',
        'guide_button': ' Руководство',
        'language': 'Язык',
        "erorr":'Ошибка',
        
        # ========== Новые слова для кнопки "О нас" ==========
        'about_button': '📋 О нас',
        'about_title': 'О приложении',
        'about_message': '''📱 Создатель обложек

Разработчики: Moghiseh & Shaker

📅 Версия: {}
📧 Поддержка: support@example.com
📞 Телефон: +98-21-12345678

⭐ Разработано для создания различных обложек
❤️ Спасибо, что выбрали нас''',
        
        # ========== Новые слова для страницы других программ ==========
        'other_programs': '📦 Другие программы',
        'other_programs_title': 'Мои другие программы',
        'loading_repos': 'Загрузка информации...',
        'github_error': 'Ошибка подключения к GitHub',
        'no_other_programs': 'Другие программы не найдены',
        'view_on_github': 'Смотреть на GitHub',
        'more_info': 'Подробнее',
        'refresh': 'Обновить',
        'description': 'Описание',
        'no_description': 'Нет описания',
        'unknown': 'Неизвестно',
        'language_colon': 'Язык',
        'stars': 'Звезды',
        'created_at': 'Создано',
        'updated_at': 'Обновлено',
        'link': 'Ссылка',
        
        # ========== Новые слова для страницы обновления ==========
        'update_title': 'Проверка обновлений',
        'current_version_checking': 'Текущая версия: Проверка...',
        'latest_version_checking': 'Последняя версия: Проверка...',
        'current_version': 'Текущая версия',
        'current_version_unknown': 'Текущая версия: Неизвестно',
        'latest_version': 'Последняя версия',
        'check_update': 'Проверить обновления',
        'check_again': 'Проверить снова',
        'start_update': 'Начать обновление',
        'checking': 'Проверка...',
        'connecting_github': 'Подключение к GitHub...',
        'github_connection_error': 'Ошибка подключения к GitHub',
        'app_up_to_date': 'Ваше приложение обновлено',
        'new_version_available': 'Доступна новая версия {}',
        'new_version_found': 'Новая версия',
        'update_question': 'Хотите обновить?',
        'update_note': 'Примечание: файлы .gitignore и README.md не будут обновлены.',
        'updating': 'Обновление...',
        'downloading_updating': 'Загрузка и обновление...',
        'update_successful': 'Обновление успешно (версия {})',
        'update_successful_title': 'Обновление успешно',
        'update_successful_message': 'Приложение успешно обновлено до версии',
        'restart_question': 'Для применения изменений необходимо перезапустить приложение. Хотите перезапустить сейчас?',
        'restarting': 'Перезапуск...',
        'update_error': 'Ошибка обновления',
        'restart_error': 'Ошибка перезапуска',
        'update': 'Обновление',
        
        # ========== Кнопки обложек ==========
        'dissertation_cover': 'Диссертация\n Обложка',
        'notebook_cover': 'Тетрадь\n или Договор\n Обложка',
        'book_cover': 'Книга\n Обложка',
        'gilded_book_cover': 'Позолоченная\n Обложка книги',
        
        # ========== Страница темы ==========
        'theme_guide_title': 'Руководство по настройке темы',
        'theme_guide_message': 'Выберите цвет, чтобы изменить цвет всех кнопок',
        'background_color': 'Цвет фона',
        
        # ========== Страница истории ==========
        'history_guide_title': 'Руководство по истории',
        'history_guide_message': 'Здесь вы можете увидеть последние 5 созданных файлов',
        
        # ========== Страница руководства по диссертации ==========
        'step1': 'Шаг 1',
        'step2': 'Шаг 2',
        'step3': 'Шаг 3',
        'step4': 'Шаг 4',
        'help_plan_1':'Руководство по первому шагу',
        'help_plan_2':'Руководство по второму шагу',
        'help_plan_3':'Руководство по третьему шагу',
        'help_plan_4':'Руководство по четвертому шагу',
        
        # ========== Страница обложки диссертации ==========
        'spine_value': 'Значение корешка (мм):',
        'title_text': 'Название:',
        'author_name': 'Имя автора:',
        'date': 'Дата:',
        'title_page_number': 'Номер титульной страницы:',
        'output_file_name': 'Имя выходного файла:',
        'select_file': 'Выбрать файл',
        'save_location': 'Место сохранения',
        'no_file_selected': 'Файл не выбран',
        'no_folder_selected': 'Папка не выбрана',
        'no_logo_selected': 'Логотип не выбран',
        'file_selected': 'Файл выбран',
        'folder_selected': 'Папка выбрана',
        'logo_selected': 'Логотип выбран',
        
        # ========== Флажки ==========
        'has_latin_page': 'Диссертация имеет латинскую страницу',
        'has_latin_page_on': 'Имеет латинскую страницу',
        'has_latin_page_off': 'Без латинской страницы',
        'logo_black_white': 'Логотип черно-белый',
        'logo_black_white_on': 'Черно-белый',
        'logo_black_white_off': 'Цветной',
        'logo_circular': 'Логотип круглый',
        'logo_circular_on': 'Круглый',
        'logo_circular_off': 'Некруглый',
        
        # ========== Кнопки действий ==========
        'refresh': 'Обновить страницу',
        'start_making': 'Начать создание',
        'load_logo': 'Загрузить логотип',
        'back': '🔙 Назад',
        'cancel': 'Отмена',
        'apply': 'Применить',
        
        # ========== Страница выбора даты ==========
        'select_year': 'Выберите год',
        'select_month': 'Выберите месяц',
        'selected_date': 'Выбранная дата:',
        
        # ========== Количество страниц ==========
        'pages': ['1 страница', '2 страницы', '3 страницы', '4 страницы', '5 страниц'],
        
        # ========== Приветственное сообщение ==========
        'welcome_message': '''Добро пожаловать в Создатель обложек
Нажмите любую кнопку обложки, чтобы начать''',
        
        # ========== О нас ==========
        'about_us': '''📱 Создатель обложек

Разработчики: Moghiseh & Shaker

📅 Версия: {}
📧 Поддержка: support@example.com
📞 Телефон: +98-21-12345678

⭐ Разработано для создания различных обложек

❤️ Спасибо, что выбрали нас''',
    },
    
    'spanish': {
        # ========== Títulos principales ==========
        'app_title': 'Creador de Portadas',
        'theme_button': '🎨 Temas',
        'history_button': 'Historial',
        'guide_button': ' Guía',
        'language': 'Idioma',
        "erorr":'Error',
        
        # ========== Nuevas palabras para el botón Acerca de ==========
        'about_button': '📋 Acerca de',
        'about_title': 'Acerca de la aplicación',
        'about_message': '''📱 Creador de Portadas

Desarrolladores: Moghiseh & Shaker

📅 Versión: {}
📧 Soporte: support@example.com
📞 Teléfono: +98-21-12345678

⭐ Diseñado para crear varios tipos de portadas
❤️ Gracias por elegirnos''',
        
        # ========== Nuevas palabras para la página de otros programas ==========
        'other_programs': '📦 Otros Programas',
        'other_programs_title': 'Mis Otros Programas',
        'loading_repos': 'Cargando información...',
        'github_error': 'Error al conectar con GitHub',
        'no_other_programs': 'No se encontraron otros programas',
        'view_on_github': 'Ver en GitHub',
        'more_info': 'Más información',
        'refresh': 'Actualizar',
        'description': 'Descripción',
        'no_description': 'Sin descripción',
        'unknown': 'Desconocido',
        'language_colon': 'Idioma',
        'stars': 'Estrellas',
        'created_at': 'Creado el',
        'updated_at': 'Actualizado el',
        'link': 'Enlace',
        
        # ========== Nuevas palabras para la página de actualización ==========
        'update_title': 'Buscar actualizaciones',
        'current_version_checking': 'Versión actual: Comprobando...',
        'latest_version_checking': 'Última versión: Comprobando...',
        'current_version': 'Versión actual',
        'current_version_unknown': 'Versión actual: Desconocida',
        'latest_version': 'Última versión',
        'check_update': 'Buscar actualizaciones',
        'check_again': 'Comprobar de nuevo',
        'start_update': 'Iniciar actualización',
        'checking': 'Comprobando...',
        'connecting_github': 'Conectando a GitHub...',
        'github_connection_error': 'Error al conectar con GitHub',
        'app_up_to_date': 'Tu aplicación está actualizada',
        'new_version_available': 'Nueva versión {} disponible',
        'new_version_found': 'Nueva versión',
        'update_question': '¿Quieres actualizar?',
        'update_note': 'Nota: Los archivos .gitignore y README.md no se actualizarán.',
        'updating': 'Actualizando...',
        'downloading_updating': 'Descargando y actualizando...',
        'update_successful': 'Actualización exitosa (versión {})',
        'update_successful_title': 'Actualización exitosa',
        'update_successful_message': 'Aplicación actualizada exitosamente a la versión',
        'restart_question': 'Para aplicar los cambios, la aplicación debe reiniciarse. ¿Quieres reiniciar ahora?',
        'restarting': 'Reiniciando...',
        'update_error': 'Error de actualización',
        'restart_error': 'Error al reiniciar',
        'update': 'Actualización',
        
        # ========== Botones de portada ==========
        'dissertation_cover': 'Portada de\n Tesis',
        'notebook_cover': 'Portada de\n Cuaderno o\n Contrato',
        'book_cover': 'Portada de\n Libro',
        'gilded_book_cover': 'Portada de\n Libro Dorado',
        
        # ========== Página de tema ==========
        'theme_guide_title': 'Guía de configuración de temas',
        'theme_guide_message': 'Seleccione un color para cambiar el color de todos los botones',
        'background_color': 'Color de fondo',
        
        # ========== Página de historial ==========
        'history_guide_title': 'Guía de historial',
        'history_guide_message': 'Aquí puede ver los últimos 5 archivos creados',
        
        # ========== Página de guía de tesis ==========
        'step1': 'Paso 1',
        'step2': 'Paso 2',
        'step3': 'Paso 3',
        'step4': 'Paso 4',
        'help_plan_1':'Guía del primer paso',
        'help_plan_2':'Guía del segundo paso',
        'help_plan_3':'Guía del tercer paso',
        'help_plan_4':'Guía del cuarto paso',
        
        # ========== Página de portada de tesis ==========
        'spine_value': 'Valor del lomo (mm):',
        'title_text': 'Título:',
        'author_name': 'Nombre del autor:',
        'date': 'Fecha:',
        'title_page_number': 'Número de página de título:',
        'output_file_name': 'Nombre del archivo de salida:',
        'select_file': 'Seleccionar archivo',
        'save_location': 'Ubicación de guardado',
        'no_file_selected': 'Ningún archivo seleccionado',
        'no_folder_selected': 'Ninguna carpeta seleccionada',
        'no_logo_selected': 'Ningún logotipo seleccionado',
        'file_selected': 'Archivo seleccionado',
        'folder_selected': 'Carpeta seleccionada',
        'logo_selected': 'Logotipo seleccionado',
        
        # ========== Casillas de verificación ==========
        'has_latin_page': 'La tesis tiene página latina',
        'has_latin_page_on': 'Tiene página latina',
        'has_latin_page_off': 'Sin página latina',
        'logo_black_white': 'El logotipo es blanco y negro',
        'logo_black_white_on': 'Blanco y negro',
        'logo_black_white_off': 'Color',
        'logo_circular': 'El logotipo es circular',
        'logo_circular_on': 'Circular',
        'logo_circular_off': 'No circular',
        
        # ========== Botones de acción ==========
        'refresh': 'Actualizar página',
        'start_making': 'Comenzar creación',
        'load_logo': 'Cargar logotipo',
        'back': '🔙 Atrás',
        'cancel': 'Cancelar',
        'apply': 'Aplicar',
        
        # ========== Página de selección de fecha ==========
        'select_year': 'Seleccionar año',
        'select_month': 'Seleccionar mes',
        'selected_date': 'Fecha seleccionada:',
        
        # ========== Números de páginas ==========
        'pages': ['1 página', '2 páginas', '3 páginas', '4 páginas', '5 páginas'],
        
        # ========== Mensaje de bienvenida ==========
        'welcome_message': '''Bienvenido a Creador de Portadas
Haga clic en cualquier botón de portada para comenzar''',
        
        # ========== Acerca de nosotros ==========
        'about_us': '''📱 Creador de Portadas

Desarrolladores: Moghiseh & Shaker

📅 Versión: {}
📧 Soporte: support@example.com
📞 Teléfono: +98-21-12345678

⭐ Diseñado para crear varios tipos de portadas

❤️ Gracias por elegirnos''',
    }
}

# زبان پیش‌فرض
current_language = 'persian'

def get_text(key):
    """دریافت متن بر اساس کلید و زبان فعلی"""
    try:
        return languages[current_language][key]
    except KeyError:
        return key

def set_language(lang):
    """تغییر زبان برنامه"""
    global current_language
    if lang in languages:
        current_language = lang
        return True
    return False

def get_months():
    """دریافت لیست ماه‌ها بر اساس زبان فعلی"""
    return languages['persian']['months']

def get_pages():
    """دریافت لیست صفحات بر اساس زبان فعلی"""
    return languages[current_language]['pages']

def get_language_name(lang_code):
    """دریافت نام زبان به زبان خودش"""
    language_names = {
        'persian': 'فارسی',
        'english': 'English',
        'arabic': 'العربية',
        'chinese': '中文',
        'russian': 'Русский',
        'spanish': 'Español'
    }
    return language_names.get(lang_code, lang_code)