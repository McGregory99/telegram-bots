# Bots de Telegram con Telebot

Este repositorio contiene el código para crear dos bots de Telegram utilizando la biblioteca Telebot de Python. Uno de los bots proporciona información meteorológica, mientras que el otro ofrece funcionalidades interactivas como selección de pizzas y gestión de cuentas.

## Configuración General

1. Clona este repositorio.
2. Instala las dependencias usando `pip install -r requirements.txt`.
3. Crea un bot en Telegram a través de BotFather y obtén tu token.
4. Crea un archivo `.env` en el directorio raíz y añade las siguientes líneas, reemplazando `'TU_TELEGRAM_TOKEN'` y `'TU_API_KEY'` (si es necesario) con tus credenciales:
   ```
   TELEGRAM_TOKEN='TU_TELEGRAM_TOKEN'
   API_KEY='TU_API_KEY'  # Solo necesario para el WeatherBot
   ```
5. Ejecuta el bot correspondiente usando `python main.py` en el directorio del bot que desees iniciar.

## Bots Disponibles

### WeatherBot

- **Descripción**: Proporciona información meteorológica utilizando la API de OpenWeatherMap.
- **Funcionalidades**:
  - Responde al comando `/start` con un mensaje de bienvenida.
  - Proporciona ayuda con el comando `/help`.
  - Ofrece información meteorológica actual para una ciudad especificada con el comando `/clima <ciudad>`.

### Mi Primer Bot

- **Descripción**: Un bot básico con funcionalidades interactivas.
- **Funcionalidades**:
  - Responde a los comandos `/start` y `/help` con un mensaje de bienvenida.
  - Ofrece opciones de pizza con el comando `/pizza`, mostrando un teclado con diferentes tipos de pizza.
  - Pregunta si deseas crear una cuenta con el comando `/cuentas`, utilizando botones inline para responder.
  - Maneja las respuestas a la pregunta de creación de cuenta, proporcionando feedback inmediato al usuario.

## Requisitos

- Python 3.x
- Bibliotecas especificadas en `requirements.txt`:
  - pyTelegramBotAPI
  - requests
  - python-dotenv
  - python-decouple

## Notas

- Asegúrate de tener un entorno virtual configurado para evitar conflictos de dependencias.
- Los archivos `.env` y `.venv/` están incluidos en `.gitignore` para proteger la información sensible y evitar subir entornos virtuales al repositorio.
