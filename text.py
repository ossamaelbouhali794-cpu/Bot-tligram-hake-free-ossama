import os
import re
import subprocess
import sys
import telebot
from telebot import types

# --- إعدادات البوت الصانع ---
MASTER_TOKEN = "8421084551:AAEe-ekoZl3Iym2FffeMRI0p1fUXolZtZN0"
bot = telebot.TeleBot(MASTER_TOKEN)

# القائمة المحدثة بالملفات الجديدة
TOOLS = {
    "1": {"name": "تبنيد حسابات", "file": "@تبنيد حسابات تيليجرام.py", "libs": "telethon requests"},
    "2": {"name": "صيد ببجي مدفوع", "file": "اداة 5ببجي مدفوعه  (1).py", "libs": "requests"},
    "3": {"name": "صيد فيزات", "file": "اداة صيد فيزات وهـميـه.py", "libs": "requests pyTelegramBotAPI"},
    "4": {"name": "رشق تيك توك", "file": "رشق تيك توك مجاني.py", "libs": "requests"},
    "5": {"name": "صيد فري فاير", "file": "تم تحويل دائمي صيد فري فاير.py", "libs": "requests"},
    "6": {"name": "سافيوم الحسابات", "file": "safum_accot._.py", "libs": "requests"}, # الملف الجديد
    "7": {"name": "تيك توك المطور", "file": "Tik Tok.py", "libs": "requests"}, # الملف الجديد
    "8": {"name": "سكريبت PHP انستا", "file": "insta.php", "libs": ""}, # ملف PHP
    "9": {"name": "بوت الجوكر", "file": "jjjjjjjjjjj.py", "libs": "pyTelegramBotAPI"} # الملف الأساسي
}

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for key, tool in TOOLS.items():
        markup.add(types.InlineKeyboardButton(tool['name'], callback_data=f"select_{key}"))
    
    bot.send_message(message.chat.id, "🛠 **أهلاً بك في مصنع الأدوات المطور**\nإختر الأداة التي تريد تجهيزها وتشغيلها:", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith("select_"))
def handle_selection(call):
    tool_id = call.data.split("_")[1]
    user_data[call.message.chat.id] = {'tool_id': tool_id}
    bot.edit_message_text("✅ تم اختيار الأداة.\nارسل الآن التوكن والأيدي بهذا الشكل:\n`TOKEN:ID`", call.message.chat.id, call.message.message_id, parse_mode="Markdown")

@bot.message_handler(func=lambda message: ":" in message.text)
def process_creation(message):
    chat_id = message.chat.id
    if chat_id not in user_data:
        return

    try:
        data = message.text.split(':')
        token = f"{data[0]}:{data[1]}"
        my_id = data[2]
        
        tool = TOOLS[user_data[chat_id]['tool_id']]
        original_file = tool['file']
        
        if not os.path.exists(original_file):
            bot.reply_to(message, f"❌ الملف `{original_file}` غير موجود في المجلد الحالي!")
            return

        # التعامل مع ملفات Python
        if original_file.endswith('.py'):
            if tool['libs']:
                bot.send_message(chat_id, f"⏳ جاري تثبيت المكتبات: ({tool['libs']})...")
                os.system(f"pip install {tool['libs']}")

            with open(original_file, 'r', encoding='utf-8') as f:
                content = f.read()

            content = re.sub(r"TOKEN\s*=\s*['\"].*?['\"]", f"TOKEN = '{token}'", content)
            content = re.sub(r"MY_ID\s*=\s*\d+", f"MY_ID = {my_id}", content)

            new_filename = f"run_{my_id}_{original_file}"
            with open(new_filename, "w", encoding="utf-8") as f:
                f.write(content)

            subprocess.Popen([sys.executable, new_filename])
            bot.reply_to(message, f"✅ تم تشغيل بوت البايثون بنجاح!\nالملف: `{new_filename}`")

        # التعامل مع ملفات PHP (إذا كان لديك مفسر php مثبت)
        elif original_file.endswith('.php'):
            bot.reply_to(message, "⚠️ ملفات PHP تحتاج إلى تعديل يدوي أو إعداد سيرفر Apache/Nginx لتشغيلها، تم حفظ الملف فقط.")

        del user_data[chat_id]

    except Exception as e:
        bot.reply_to(message, f"❌ حدث خطأ: {str(e)}")

print("📡 البوت الصانع المطور يعمل الآن...")
bot.infinity_polling()
