import telebot
from flask import Flask, request
import os

    # ==============================
    # 🔑 التوكن
    # ==============================
TOKEN = ""

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

    # ==============================
    # أوامر البوت
    # ==============================

@bot.message_handler(commands=['start'])
def start(message):
        text = """👋 أهلاً بيك في Orion BIS Assistant

    📚 /subjects
    🎓 /study
    🚀 /development
    🎥 /lessons
    🛠 /support
    ❓ /help
    🏢 /admin

    اكتب الأمر وابدأ 👇
    """
        bot.reply_to(message, text)

@bot.message_handler(commands=['subjects'])
def subjects_section(message):
        bot.reply_to(message, "📚 اكتب سؤالك في أي مادة.")

@bot.message_handler(commands=['study'])
def study_section(message):
        bot.reply_to(message, "🎓 اسأل عن تنظيم الوقت أو الامتحانات.")

@bot.message_handler(commands=['development'])
def development_section(message):
        bot.reply_to(message, "🚀 اسأل عن مهارات أو كورسات.")

@bot.message_handler(commands=['lessons'])
def lessons_section(message):
        bot.reply_to(message, "🎥 ادخل المنصة وسجل دخولك بالرقم الجامعي.")

@bot.message_handler(commands=['support'])
def support_section(message):
        bot.reply_to(message, "🛠 اكتب مشكلتك وسيتم الرد عليك.")

@bot.message_handler(commands=['help'])
def help_section(message):
        bot.reply_to(message, "❓ استخدم /start لعرض الأقسام")

@bot.message_handler(commands=['admin'])
def admin_section(message):
        bot.reply_to(message, "🏢 اكتب رسالتك للإدارة وسيتم مراجعتها.")

@bot.message_handler(func=lambda message: True)
def smart_reply(message):
        msg = message.text.lower()

        if "محاسبة" in msg:
            bot.reply_to(message, "📊 ركز على المعادلة المحاسبية.")
        elif "ادارة" in msg or "إدارة" in msg:
            bot.reply_to(message, "📈 الإدارة = تخطيط + تنظيم + رقابة.")
        elif "تنظيم الوقت" in msg:
            bot.reply_to(message, "⏳ 25 دقيقة مذاكرة + 5 راحة.")
        elif "امتحان" in msg:
            bot.reply_to(message, "📝 راجع الملخصات وحل امتحانات سابقة.")
        elif "كورسات" in msg:
            bot.reply_to(message, "🎓 ابحث عن كورسات مجانية أونلاين.")
        elif "مشكلة" in msg:
            bot.reply_to(message, "🛠 وضّح المشكلة بالتفصيل.")
        else:
            bot.reply_to(message, "🤖 استخدم /start لعرض الأقسام.")

    # ==============================
    # Webhook Endpoint
    # ==============================

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
        json_str = request.get_data().decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "OK", 200

    # ==============================
    # الصفحة الرئيسية (للمونيتور)
    # ==============================

@app.route("/")
def home():
        return "Bot is running!", 200

    # ==============================
    # تشغيل السيرفر
    # ==============================

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
