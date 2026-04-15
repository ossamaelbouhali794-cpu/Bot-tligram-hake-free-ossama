from flask import Flask, request, render_template_string
import subprocess
import os
import sys

app = Flask(__name__)

# المسار الحالي للمجلد
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    try:
        with open(os.path.join(BASE_DIR, 'bot.html'), 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "<h1>❌ خطأ: تأكد من وجود ملف bot.html في نفس المجلد</h1>"

@app.route('/run', methods=['POST'])
def run_bot():
    token = request.form.get('token')
    my_id = request.form.get('my_id')
    
    # قراءة محتوى ملفك الأصلي
    original_file = os.path.join(BASE_DIR, 'jjjjjjjjjjj.py')
    if not os.path.exists(original_file):
        return "<h1>❌ خطأ: ملف jjjjjjjjjjj.py غير موجود بجانبي!</h1>"

    with open(original_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # استبدال التوكن والأيدي داخل نص الكود
    # سنبحث عن الأسطر التي تبدأ بـ TOKEN = و MY_ID = ونستبدلها
    import re
    content = re.sub(r"TOKEN\s*=\s*'.*?'", f"TOKEN = '{token}'", content)
    content = re.sub(r"MY_ID\s*=\s*\d+", f"MY_ID = {my_id}", content)

    # حفظ الكود المحدث في ملف جديد للتشغيل
    active_path = os.path.join(BASE_DIR, "active_user_bot.py")
    with open(active_path, "w", encoding="utf-8") as f:
        f.write(content)

    # تشغيل البوت المحدث في الخلفية
    try:
        subprocess.Popen([sys.executable, active_path])
        return f"<h1>✅ تم التحديث! البوت يعمل الآن بتوكن: {token[:10]}...</h1>"
    except Exception as e:
        return f"<h1>❌ فشل التشغيل: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
