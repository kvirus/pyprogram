from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import openai

# Установите свой токен от BotFather
TELEGRAM_TOKEN = "5800064216:AAFWd0BnsgM9MH94ppPZKU9plisU0L9K_2k"

# Установите свой API-ключ от OpenAI
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

ALLOWED_CHAT_IDS = [32949476, 987654321]

def start(update, context):
    chat_id = update.message.chat_id
    if chat_id in ALLOWED_CHAT_IDS:
        keyboard = [[InlineKeyboardButton("ChatGPT", callback_data='enable_chatgpt')],[InlineKeyboardButton("2", callback_data='button2')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Выберите действие:', reply_markup=reply_markup)
    else:
        update.message.reply_text("Идите в жопу")
def hello(update, context):
    update.message.reply_text("Привет привет")

def stopbot(update, context):
    chat_id = update.message.chat_id
    print(chat_id)
    context.user_data[chat_id] = {"chatgpt_enabled": False}
    print(context.user_data[chat_id])
    # query = update.callback_query
    # user_id = query.from_user.id
    # keyboard = [[InlineKeyboardButton("disable", callback_data='dis_chatgpt')]]
    # if query.data == 'dis_chatgpt':
    #     context.user_data[user_id] = {"chatgpt_enabled": False}
    #     print(user_id)
    #     print(context.user_data[user_id])
    #     query.edit_message_text(text="ChatGPT включен")
    # print(user_id)
    # print(context.user_data[user_id])
    # query.edit_message_text(text="ChatGPT включен")
    update.message.reply_text("Пока пока")

def button_click(update, context):
    query = update.callback_query
    #button_data = query.data
    user_id = query.from_user.id
    if query.data == 'enable_chatgpt':
        context.user_data[user_id] = {"chatgpt_enabled": True}
        print(user_id)
        print(context.user_data)
        query.edit_message_text(text="ChatGPT включен")
    # elif button_data == 'button2':
    #     query.edit_message_text(text="Вы нажали на Кнопку 2!")



def handle_message(update, context):
    user_input = update.message.text
    user_id = update.message.from_user.id
    chatgpt_enabled = context.user_data.get(user_id, {}).get("chatgpt_enabled", False)
    # Используйте GPT для генерации ответа
    if chatgpt_enabled:
        response = generate_response(user_input)
        # Отправьте ответ пользователю
        update.message.reply_text(response)
    else:
        update.message.reply_text("Функция ChatGPT не включена. Воспользуйтесь командой /start для включения.")

def generate_response(input_text):
    # # Используйте OpenAI GPT-3 для генерации ответа
    # prompt = f"User: {input_text}\nBot:"
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     max_tokens=1000,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    # return response.choices[0].text.strip()
    prompt = R"User: {input_text}\nBot:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text},
        ],
    )
    return response['choices'][0]['message']['content']


def main():
    updater = Updater(token=TELEGRAM_TOKEN,use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("hello", hello))
    dp.add_handler(CommandHandler("stopbot", stopbot))

    dp.add_handler(CallbackQueryHandler(button_click))
    dp.add_handler(MessageHandler(filters.Filters.text & ~filters.Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

main()