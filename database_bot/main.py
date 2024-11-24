import sqlite3
import telebot
from decouple import config

TOKEN = config('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

    
def insert_user(telegram_id: int, name: str):
    conn = sqlite3.connect('database_bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (telegram_id, name) 
        VALUES (?, ?)
    ''', (telegram_id, name))
    
    conn.commit()
    cursor.close()
    conn.close()
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola, ¿cómo puedo ayudarte hoy? Usa /help para ver los comandos disponibles.")
    
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Comandos disponibles:\n"
        "/start - Muestra el mensaje de bienvenida.\n"
        "/help - Muestra esta ayuda.\n"
        "/save - Guarda tu información en la base de datos.\n"
    )
    bot.reply_to(message, help_text)
    
@bot.message_handler(commands=['save'])
def save_user(message):
    telegram_id = message.from_user.id
    name = message.from_user.first_name
    insert_user(telegram_id, name)
    
    bot.reply_to(message, f"Bienvenido {name}, te has guardado correctamente en nuestra BBDD")

if __name__ == '__main__':
    bot.infinity_polling()