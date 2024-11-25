# DatabaseBot de Telegram

Este repositorio contiene el código para crear un bot de Telegram que guarda la información de los usuarios en una base de datos SQLite utilizando la biblioteca Telebot de Python.

## Configuración

1. Clona este repositorio.
2. Instala las dependencias usando `pip install -r requirements.txt`.
3. Crea un bot en Telegram a través de BotFather y obtén tu token.
4. Crea un archivo `.env` en el directorio raíz y añade la siguiente línea, reemplazando `'TU_TELEGRAM_TOKEN'` con tu token:
   ```
   TELEGRAM_TOKEN='TU_TELEGRAM_TOKEN'
   ```
5. Ejecuta el bot usando `python main.py`.

## Funcionalidades

- Responde al comando `/start` con un mensaje de bienvenida.
- Proporciona ayuda con el comando `/help`.
- Guarda el ID de Telegram y el nombre del usuario en la base de datos con el comando `/save`.

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
