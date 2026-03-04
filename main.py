import telebot
from flask import Flask, request
import os


    # ==============================
    # 🔑 حط التوكن هنا
    # ==============================
TOKEN = "7256432256:AAHClOtJ3nUUG0tPHk8LbQ59dE-R3IIYGOQ"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

    # ==============================
    # أمر البداية
    # ==============================

@bot.message_handler(commands=['start'])
def start(message):
        text = """👋 أهلاً بيك في Orion BIS Assistant

    الأقسام المتاحة:

    📚 /subjects        - أسئلة في المواد
    🎓 /study           - أسئلة في الدراسة
    🚀 /development     - تطوير الذات والكورسات
    🎥 /lessons         - طريقة الوصول للدروس
    🛠 /support         - الدعم الفني
    ❓ /help            - مساعدة في استخدام البوت
    🏢 /admin           - التحدث مع الإدارة

    اكتب الأمر وابدأ 👇
    """
        bot.reply_to(message, text)

    # ==============================
    # الأقسام
    # ==============================

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
        bot.reply_to(message, "❓ استخدم الأوامر أو ابدأ بـ /start")

@bot.message_handler(commands=['admin'])
def admin_section(message):
        bot.reply_to(message, "🏢 اكتب رسالتك للإدارة وسيتم مراجعتها.")

    # ==============================
    # الرد الذكي
    # ==============================

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
    # Webhook
    # ==============================

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
        json_str = request.get_data().decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "OK", 200

@app.route("/")
def home():
        return "Bot is running!", 200

    # ==============================
    # تشغيل السيرفر
    # ==============================

if __name__ == "__main__":
        bot.remove_webhook()
        bot.set_webhook(url=f"https://qand-a-orion-bis-telebot--yovexevilghost.replit.app/{TOKEN}")
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
