import telebot
from googletrans import Translator

bot = telebot.TeleBot('6192853255:AAFvdItAmhei8UO4nRMgV5baYgxsOR_b4v4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Вітаю {message.from_user.first_name}🤗, ти у перекладач боті, щоб перекласти текст тикай /translate')

@bot.message_handler(commands=['translate'])
def translare(message):
    bot.send_message(message.chat.id, 'Введіть текст для перекладу: ')
    bot.register_next_step_handler(message, translate)
@bot.message_handler()
def translate(message):
     translator = Translator()
     a = translator.translate(text=message.text, src='uk', dest='en')
     bot.send_message(message.chat.id, a.text)




bot.polling(none_stop=True)














