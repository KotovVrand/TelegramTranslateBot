from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests

TOKEN = '7911165186:AAEHFfxvlitKeGMXQSxC1qQphqejN7lLFZA'
LIBRETRANSLATE_URL = 'https://libretranslate.com/translate'

def start(update, context):
    update.message.reply_text("Привіт! Я бот для перекладу. Пиши повідомлення, і я перекладу його на 4 мови!")

def help_command(update, context):
    update.message.reply_text("Інструкція:\n- Пиши будь-яке повідомлення, і я перекладу його на англійську, російську, французьку та італійську.\n- Команди: /start, /help, /languages")

def languages(update, context):
    update.message.reply_text("Підтримувані мови: English, Russian, French, Italian")

def translate_message(update, context):
    message_text = update.message.text
    try:
        translations = {
            'English': requests.post(LIBRETRANSLATE_URL, json={
                'q': message_text, 'source': 'auto', 'target': 'en'
            }).json()['translatedText'],
            'Russian': requests.post(LIBRETRANSLATE_URL, json={
                'q': message_text, 'source': 'auto', 'target': 'ru'
            }).json()['translatedText'],
            'French': requests.post(LIBRETRANSLATE_URL, json={
                'q': message_text, 'source': 'auto', 'target': 'fr'
            }).json()['translatedText'],
            'Italian': requests.post(LIBRETRANSLATE_URL, json={
                'q': message_text, 'source': 'auto', 'target': 'it'
            }).json()['translatedText']
        }
        reply_text = "Переклади:\n\n"
        for lang, text in translations.items():
            reply_text += f"{lang}: {text}\n"
        update.message.reply_text(reply_text)
    except Exception as e:
        update.message.reply_text(f"Помилка перекладу: {str(e)}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("languages", languages))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))
    updater.start_polling()
    print("Бот запущено! Натисни Ctrl+C для зупинки.")
    updater.idle()

if __name__ == '__main__':
    main()
