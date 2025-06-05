from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes
from deep_translator import MyMemoryTranslator

TOKEN = '7911165186:AAEHFfxvlitKeGMXQSxC1qQphqejN7lLFZA'

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    try:
        translations = {
            'English': MyMemoryTranslator(source='auto', target='en').translate(message_text),
            'Russian': MyMemoryTranslator(source='auto', target='ru').translate(message_text),
            'French': MyMemoryTranslator(source='auto', target='fr').translate(message_text),
            'Italian': MyMemoryTranslator(source='auto', target='it').translate(message_text),
            'Japanese': MyMemoryTranslator(source='auto', target='ja').translate(message_text)
        }

        reply_text = "🫡 Переклад:\n\n"
        for lang, text in translations.items():
            reply_text += f"{lang}: {text}\n"

        await update.message.reply_text(reply_text)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
    print("Бот запущено.")
    app.run_polling()

if __name__ == '__main__':
    main()
