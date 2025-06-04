from telegram.ext import Updater, MessageHandler, Filters
from deep_translator import GoogleTranslator

# Токен у лапках
TOKEN = '7911165186:AAEHFfxvlitKeGMXQSxC1qQphqejN7lLFZA'

def translate_message(update, context):
    message_text = update.message.text
    chat_id = update.message.chat_id

    try:
        # Переклад на 4 мови
        translations = {
            'English': GoogleTranslator(source='auto', target='en').translate(message_text),
            'Russian': GoogleTranslator(source='auto', target='ru').translate(message_text),
            'French': GoogleTranslator(source='auto', target='fr').translate(message_text),
            'Italian': GoogleTranslator(source='auto', target='it').translate(message_text),
            'Japanese': GoogleTranslator(source='auto', target='ja').translate(message_text)
        }

        # Формуємо одне повідомлення з усіма перекладами
        reply_text = "🫡\n\n"
        for lang, text in translations.items():
            reply_text += f"{lang}: {text}\n"

        # Відправляємо одне повідомлення
        update.message.reply_text(reply_text)

    except Exception as e:
        update.message.reply_text(f"Помилка перекладу: {str(e)}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Обробка всіх текстових повідомлень (крім команд)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    # Запуск бота
    updater.start_polling()
    print("Бот запущено! Натисни Ctrl+C для зупинки.")
    updater.idle()

if __name__ == '__main__':
    main()
