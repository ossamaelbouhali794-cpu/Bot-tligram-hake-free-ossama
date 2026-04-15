import telebot
from telebot import types
import random
import time
import os

# --- بياناتك الخاصة ---
TOKEN = '8634952552:AAEScRhjNavfndt040Gj_Z37ywSkki9Rb-U '
MY_ID =  8562589105
bot = telebot.TeleBot(TOKEN)

# --- الإعدادات والروابط ---
PHOTO_NAME = '40793.jpg' 
APP_URL = 'https://www.appcreator24.com/app3889713-psr68g'
PYDROID_URL = 'https://play.google.com/store/apps/details?id=ru.iiec.pydroid3'

# --- أسماء الملفات (تأكد من وجودها بجانب ملف البوت) ---
FILES = {
    "script": "safum_accot._.py",
    "php_insta": "insta.php",
    "ban_tele": "@تبنيد حسابات تيليجرام.py",
    "pubg_hunt1": "أداة صـيـد بـبـجـي [ @N_Q_P ].py",
    "visa_hunt": "اداة صيد فيزات وهـميـه.py",
    "tiktok": "رشق تيك توك مجاني.py",
    "enc_file": "ك-enc.py",
    "pubg_paid": "اداة 5ببجي مدفوعه  (1).py",
    "ff_hunt": "تم تحويل دائمي صيد فري فاير.py"
}

def main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('📥 صيد SafeUM'),
        types.KeyboardButton('🔥 بوت فري فاير'),
        types.KeyboardButton('📸 رشق إنستا PHP'),
        types.KeyboardButton('🚫 تبنيد تيليجرام'),
        types.KeyboardButton('🎮 صيد ببجي (مدفوع)'),
        types.KeyboardButton('💳 صيد فيزات'),
        types.KeyboardButton('🎵 رشق تيك توك'),
        types.KeyboardButton('🔐 أداة التشفير'),
        types.KeyboardButton('🐍 تحميل Pydroid 3'),
        types.KeyboardButton('👨‍💻 الدعم الفني')
    )
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    intro_text = (
        "🃏 **مرحباً بك في لوحة تحكم الجيكو النهائية..**\n\n"
        "تم تحديث جميع الأدوات وإضافة المكاتب المطلوبة لكل أداة.\n"
        "🛡 **اختر القسم الذي تريده:**"
    )
    if os.path.exists(PHOTO_NAME):
        with open(PHOTO_NAME, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=intro_text, parse_mode="Markdown", reply_markup=main_keyboard())
    else:
        bot.send_message(message.chat.id, intro_text, parse_mode="Markdown", reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    chat_id = message.chat.id
    msg = message.text

    # دالة إرسال الملفات مع المكاتب المطلوبة
    def send_tool(file_key, description, requirements):
        full_desc = f"{description}\n\n📚 **المكتبات المطلوبة:**\n`{requirements}`\n\n⏳ جاري إرسال الملف..."
        bot.send_message(chat_id, full_desc, parse_mode="Markdown")
        
        file_path = FILES.get(file_key)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id, f, caption=f"🚀 ملف {msg} - جيكو")
        else:
            bot.send_message(chat_id, f"⚠️ خطأ: الملف {file_path} غير موجود.")

    if msg == '🔥 بوت فري فاير':
        send_tool("ff_hunt", 
                  "🔥 **أداة صيد فري فاير (دائمي):**\nسكربت متطور لفحص وصيد الحسابات المتاحة.",
                  "pip install requests requests user_agent")

    elif msg == '📥 صيد SafeUM':
        send_tool("script", 
                  "🎯 **أداة صيد SafeUM:** لإنشاء حسابات وأرقام لاتفية.",
                  "pip install requests websocket-client")

    elif msg == '🚫 تبنيد تيليجرام':
        send_tool("ban_tele", 
                  "🚫 **أداة تبنيد الحسابات:** لإرسال تقارير سبام مكثفة.",
                  "pip install telethon requests")

    elif msg == '📸 رشق إنستا PHP':
        send_tool("php_insta", 
                  "📸 **سورس رشق إنستا (PHP):** يحتاج استضافة ويب وليس Pydroid.",
                  "لا يحتاج مكتبات بايثون (PHP Script)")

    elif msg == '💳 صيد فيزات':
        send_tool("visa_hunt", 
                  "💳 **أداة صيد فيزات وهمية:** فحص وتوليد بطاقات.",
                  "pip install requests")

    elif msg == '🎵 رشق تيك توك':
        send_tool("tiktok", 
                  "🎵 **رشق تيك توك مجاني:** زيادة متابعين وتفاعل.",
                  "pip install requests colorama prettytable")

    elif msg == '🔐 أداة التشفير':
        send_tool("enc_file", 
                  "🔐 **أداة تشفير الملفات:** لحماية سورس كود بايثون.",
                  "pip install requests colorama")

    elif msg == '🎮 صيد ببجي (مدفوع)':
        send_tool("pubg_paid", 
                  "🔥 **أداة صيد ببجي VIP:** النسخة المدفوعة مجاناً.",
                  "pip install requests user_agent")

    elif msg == '🐍 تحميل Pydroid 3':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📥 رابط المتجر", url=PYDROID_URL))
        bot.send_message(chat_id, "ℹ️ لتحميل تطبيق Pydroid 3 لتشغيل الأدوات:", reply_markup=markup)

    elif msg == '👨‍💻 الدعم الفني':
        bot.send_message(chat_id, "للتواصل مع المطور: @Cufatuka")

# --- نظام الاستمرارية ---
if __name__ == "__main__":
    while True:
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            time.sleep(5)
