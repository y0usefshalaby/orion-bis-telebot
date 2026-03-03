import telebot
import os
TOKEN = os.environ.get("TOKEN")

TOKEN = "7256432256:AAF0aMabmwy50kLTAoOkWuQjcYId4XOhRrI"

bot = telebot.TeleBot(TOKEN)

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
# الأقسام الأساسية
# ==============================


@bot.message_handler(commands=['subjects'])
def subjects_section(message):
    bot.reply_to(
        message, "📚 قسم أسئلة المواد\n"
        "اكتب سؤالك في أي مادة مثل:\n"
        "- محاسبة\n"
        "- إدارة\n"
        "- نظم معلومات\n"
        "- تسويق")


@bot.message_handler(commands=['study'])
def study_section(message):
    bot.reply_to(
        message, "🎓 قسم الدراسة\n"
        "اسأل عن:\n"
        "- تنظيم الوقت\n"
        "- المذاكرة الصح\n"
        "- التحضير للامتحانات")


@bot.message_handler(commands=['development'])
def development_section(message):
    bot.reply_to(
        message, "🚀 تطوير الذات والكورسات\n"
        "اسأل عن:\n"
        "- كورسات مجانية\n"
        "- مهارات مطلوبة\n"
        "- العمل الحر")


@bot.message_handler(commands=['lessons'])
def lessons_section(message):
    bot.reply_to(
        message, "🎥 للوصول إلى الدروس:\n"
        "1- ادخل على المنصة التعليمية.\n"
        "2- سجل دخولك بالرقم الجامعي.\n"
        "3- اختر المادة المطلوبة.\n"
        "لو عندك مشكلة استخدم /support")


@bot.message_handler(commands=['support'])
def support_section(message):
    bot.reply_to(
        message, "🛠 الدعم الفني:\n"
        "لو عندك مشكلة تقنية اكتب تفاصيل المشكلة\n"
        "وسيتم الرد عليك في أقرب وقت.")


@bot.message_handler(commands=['help'])
def help_section(message):
    bot.reply_to(
        message, "❓ طريقة استخدام البوت:\n"
        "- استخدم الأوامر من القائمة.\n"
        "- اكتب سؤالك بشكل واضح.\n"
        "- تقدر تبدأ دايمًا بـ /start")


@bot.message_handler(commands=['admin'])
def admin_section(message):
    bot.reply_to(
        message, "🏢 للتحدث مع الإدارة:\n"
        "يرجى كتابة رسالتك وسيتم مراجعتها.\n"
        "أو تواصل عبر البريد الرسمي للجامعة.")


# ==============================
# الرد الذكي
# ==============================


@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    msg = message.text.lower()

    if "محاسبة" in msg:
        bot.reply_to(
            message,
            "📊 في المحاسبة ركز على المعادلة المحاسبية والقيود اليومية.")

    elif "ادارة" in msg or "إدارة" in msg:
        bot.reply_to(message, "📈 الإدارة تعتمد على التخطيط والتنظيم والرقابة.")

    elif "تنظيم الوقت" in msg:
        bot.reply_to(message,
                     "⏳ جرب تقنية Pomodoro: 25 دقيقة مذاكرة + 5 دقائق راحة.")

    elif "امتحان" in msg:
        bot.reply_to(message, "📝 راجع الملخصات وحل نماذج امتحانات سابقة.")

    elif "كورسات" in msg:
        bot.reply_to(message,
                     "🎓 ابحث عن كورسات مجانية على منصات التعليم الأونلاين.")

    elif "فريلانس" in msg:
        bot.reply_to(message,
                     "💻 ابدأ بمهارة بسيطة واشتغل على منصات العمل الحر.")

    elif "مشكلة" in msg:
        bot.reply_to(message, "🛠 من فضلك وضّح المشكلة بالتفصيل وسيتم مساعدتك.")

    else:
        bot.reply_to(
            message, "🤖 لم أفهم سؤالك بالكامل.\n"
            "استخدم /start لعرض الأقسام.")


# ==============================
# تشغيل البوت
# ==============================

print("🤖 Bot is running...")
bot.infinity_polling(skip_pending=True)
