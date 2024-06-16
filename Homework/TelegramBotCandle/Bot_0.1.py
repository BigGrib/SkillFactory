
import telebot
from config import keys,TOKEN
from extensions import ConvertCurrency,ConvertionExeption
bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Для начала работы введите команду боту в следующем формате: \n <имя валюты> <количество> <в какую валюту перевести>\
например:  рубль 10000 доллар\n \
Чтобы увидеть все доступные валюты введите /values'
    bot.reply_to(message,text)
# Обрабатывается все документы и аудиозаписи
@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = 'доступные валюты:'
    for key in keys.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message,text)
@bot.message_handler(content_types=['text',])
def exchange(message: telebot.types.Message):
    try:
        values = message.text.lower().split(" ")

        if len(values) != 3:
            raise ConvertionExeption('Введено неверное количество параметров')

        quote, amount, base = values
        total = ConvertCurrency.convert(quote, amount, base)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать запрос\n{e}')
    else:
        text = f'При обмене {amount} {keys[quote]} вы получите {total[0]} {keys[base]} \nДата обновления курса - {total[2]}\nКурс обмена  составил : {total[1]} {keys[quote]} за 1 {keys[base]}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)