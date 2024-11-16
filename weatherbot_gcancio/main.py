import telebot
from decouple import config
import requests

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
API_KEY = config('API_KEY')


bot = telebot.TeleBot(TELEGRAM_TOKEN)
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    complete_url = BASE_URL + "?q=" + city_name + "&appid=" + API_KEY
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != 404:
        main_data = data["main"]
        weather_data = data["weather"][0]
        temperature = main_data["temp"] - 273.15
        description = weather_data["description"]
        return f"Temperatura: {temperature:.2f}°C\nDescripción: {description.capitalize()}"
    else:
        return 'Ciudad no encontrada'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Bienvenido al WeatherBot! Estoy aquí para proporcionarte información meteorológica. Usa el comando /clima seguido del nombre de una ciudad para obtener el clima actual.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Comandos disponibles:\n"
        "/start - Muestra el mensaje de bienvenida.\n"
        "/help - Muestra esta ayuda.\n"
        "/clima <ciudad> - Proporciona el clima actual de la ciudad especificada.\n"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['clima'])
def send_weather(message):
    city_name = message.text.split()[1] if len(message.text.split()) > 1 else None
    if city_name:
        weather_info = get_weather(city_name)
        bot.reply_to(message, weather_info)
    else:
        bot.reply_to(message, "Por favor, proporciona el nombre de la ciudad. Ejemplo: /clima Madrid")

if __name__ == '__main__':
    bot.infinity_polling()
