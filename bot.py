import telebot
import time

bot = telebot.TeleBot('TOKEN')# Токен для бота
print(bot.get_me())

@bot.message_handler(content_types=['text'])
def handler_message(message):
    # Ответ на сообщения
    if message.text.lower() == 'пидора ответ':
        bot.reply_to(message,'Шлюхи аргумент!')
    elif message.text.lower() == 'амогус' or message.text.lower() == 'amogus':
        bot.send_photo(message.from_user.id, 'https://ibb.co/L0yGXxM')
    elif message.text.lower() == 'нет':
        bot.send_photo(message.from_user.id,'Пидора ответ!')
    elif message.text.lower() == 'пока':
        bot.send_photo(message.from_user.id,'https://ibb.co/sJJtZ47')
    elif message.text.lower() == 'да':
        bot.send_photo(message.from_user.id,'https://ibb.co/Bcjp91d')
    elif 'артём' in message.text.lower():
        bot.reply_to(message,'Назвать ребëнка "Артëм" - \nПочти такая же ошибка, Как пойти в детдом, \nИ не сдать Артëма слишком быстро')
    elif message.text.lower() == 'минет':
        bot.reply_to(message,'Какой минет нахуй?Тебе хоть 18 есть?')
    elif message.text.lower() == 'нихуя':
        bot.reply_to(message,'СЕБЕ?')
    elif message.text.lower() == 'боже яке':
        bot.reply_to(message,'Воно кончене!')
    elif message.text.lower() == 'антон':
        bot.reply_to(message,'Гандон!')
    elif message.text.lower() == 'эдик':
        bot.reply_to(message,'Педик!')
    elif message.text.lower() == 'шлюхи аргумент не нужен,пидор обнаружен' or message.text.lower() == 'шлюхи аргумент не нужен пидор обнаружен':
        bot.reply_to(message,'Слышь,чё дохуя умный?\nВот когда разраб мне прикрутит базу на такие слова,будешь у меня нюхать бебру!')
    elif message.text.lower() == 'бот расскажи анекдот' or message.text.lower() == 'бот раскажи анекдот' :
        bot.reply_to(message,'Пупа и Лупа были соседями в Советском общежитии.\nОднажды Пупа назвал товарища Сталина "Предателем революции",\nпосле чего Пупу забрали, обвинили в " Антисоветской пропаганде ".\nПытками из него выбили признание а потом расстреляли.\nКак оказалось причиной расстрела стал донос Лупы. Выходит Пупу расстреляли из-за Лупы')
    elif message.text.lower() == 'а':
        bot.reply_to(message,'Б')   
    elif message.text.lower() == 'в':
        bot.reply_to(message,'г')
    elif message.text.lower() == 'д':
        bot.reply_to(message,'е')
    elif message.text.lower() == 'ё':
        bot.reply_to(message,'ж')
    elif message.text.lower() == 'з':
        bot.reply_to(message,'Пишов нахуй,заебал!')
    elif message.text.lower() == 'блэт':
        bot.reply_to(message,'Блэт,хует,заебали блять.')
    elif message.text.lower() == 'чек мать' or message.text.lower() == 'чекни мать' or message.text.lower() == 'где мать' :
        bot.reply_to(message,'Свою мать чекни,дебил блять')
    elif message.text.lower() == 'блять'or message.text.lower() =='сука'or message.text.lower() =='ебать'or message.text.lower() =='уебан'or message.text.lower() =='ёбанный рот'or message.text.lower() =='ёбаный'or message.text.lower() =='ебаный'or message.text.lower() =='хуя'or message.text.lower() =='пизда'or message.text.lower() =='пиздец':
        bot.reply_to(message,'Сука,хули материшься блять?Совсем ахуел?Кто тебя этому научил?')
    # Логи
    time_message = time.ctime(message.date) 
    print('Дата лога:{', time_message, '}\nСодержимое:{', message.text, '}\nАвтор:{(Никнейм -', message.from_user.username, ') -','(Имя -', message.from_user.first_name,')}\n','##########')

bot.polling() 