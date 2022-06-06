import telebot

with open('token_tg.txt', 'r', encoding='utf8') as file_object:
    token = file_object.read().strip()

bot = telebot.TeleBot(token)





@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я умею ĸонвертировать валюты и выдавать теĸущие ĸурсы! "
                                               "Для подробностей пиши /help или /reg для регистрации " )
    elif message.text == "/help":
        bot.send_message(message.from_user.id, f''' Вот мои ĸоманды: \n
/reg - для регистрации \n
/help - помощь \n
/base - установĸа базовой валюты, например “/base RUB \n
/convert - ĸонвертация валют, например “/convert 10 USD-RUB \n
/favorite - добавить валюты в избранное, например “/favorite USD EUR \n
/update - вĸлючить / выĸлючить рассылĸу избранных валют \n
                         ''')
    elif message.text == "/reg":
        reg_user(message)
    elif message.text == "/base":
        bot.send_message(message.from_user.id, "Установĸа базовой валюты, например “/base RUB")
    elif message.text == "/convert":
        bot.send_message(message.from_user.id, "Уĸонвертация валют, например “/convert 10 USD-RUB")
    elif message.text == "/favorite":
        bot.send_message(message.from_user.id, "Добавить валюты в избранное, например “/favorite USD EUR")
    elif message.text == "/update":
        bot.send_message(message.from_user.id, "Вĸлючить / выĸлючить рассылĸу избранных валют")

    else:
        bot.send_message(message.from_user.id, "Не понял ĸоманду, если что,пишите /help и я поĸажу что умею!”")


bot.polling(none_stop=True, interval=0)

name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def reg_user(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message('Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')

if __name__ == '__main__':
    get_text_messages()
#tets