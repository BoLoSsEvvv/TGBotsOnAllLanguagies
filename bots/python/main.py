import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)

