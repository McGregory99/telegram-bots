import telebot
from telebot import types

TOKEN = 'TU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, ¿cómo puedo ayudarte hoy?")
    
    
@bot.message_handler(commands=['pizza'])
def send_options(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('🍕 Hawaiana')
    itembtn2 = types.KeyboardButton('🍕 Pepperoni')
    itembtn3 = types.KeyboardButton('🍕 4 Quesos')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, 'Seleccione una opción', reply_markup=markup)
    
    
@bot.message_handler(commands=['cuentas'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Creando dos botones
    btn_si = types.InlineKeyboardButton('Si', callback_data='cuentas_si')
    btn_no = types.InlineKeyboardButton('No', callback_data='cuentas_no')
    
    # Agregamos los botones al markup
    markup.add(btn_si, btn_no)
    
    # Enviamos el mensaje con el markup al usuario
    bot.send_message(chat_id=message.chat.id, 
                     text='¿Desea crear una cuenta?', 
                     reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'cuentas_si':
        bot.answer_callback_query(callback_query_id=call.id, 
                                  text='¡Cuenta creada con éxito!')
    elif call.data == 'cuentas_no':
        bot.answer_callback_query(callback_query_id=call.id, 
                                  text='¡Gracias por usar nuestro servicio!')


if __name__ == '__main__':
    bot.infinity_polling()