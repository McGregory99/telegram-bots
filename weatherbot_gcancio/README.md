# WeatherBot de Telegram

Este repositorio contiene el código para crear un bot de Telegram que proporciona información meteorológica utilizando la API de OpenWeatherMap y la biblioteca Telebot de Python.

## Configuración

1. Clona este repositorio.
2. Instala las dependencias usando `pip install -r requirements.txt`.
3. Crea un bot en Telegram a través de BotFather y obtén tu token.
4. Obtén una clave de API de OpenWeatherMap.
5. Crea un archivo `.env` en el directorio raíz y añade las siguientes líneas, reemplazando `'TU_TELEGRAM_TOKEN'` y `'TU_API_KEY'` con tus credenciales:
   ```
   TELEGRAM_TOKEN='TU_TELEGRAM_TOKEN'
   API_KEY='TU_API_KEY'
   ```
6. Ejecuta el bot usando `python main.py`.

## Funcionalidades:

- Responde al comando `/start` con un mensaje de bienvenida.
- Proporciona ayuda con el comando `/help`.
- Ofrece información meteorológica actual para una ciudad especificada con el comando `/clima <ciudad>`. 