# Mi primer Bot de Telegram con Telebot

Este repositorio contiene el código para crear un bot básico de Telegram utilizando la biblioteca Telebot de Python.

## Configuración

1. Clona este repositorio.
2. Instala las dependencias usando `pip install -r requirements.txt`
3. Crea un bot en Telegram a través de BotFather y obtén tu token.
4. Crea un archivo `.env` en el directorio raíz y añade la siguiente línea, reemplazando `'TU_TELEGRAM_TOKEN'` con tu token:
   ```
   TELEGRAM_TOKEN='TU_TELEGRAM_TOKEN'
   ```
5. Ejecuta el bot usando `python main.py`

## Funcionalidades:

- Responde a los comandos `/start` y `/help` con un mensaje de bienvenida.
- Ofrece opciones de pizza con el comando `/pizza`, mostrando un teclado con diferentes tipos de pizza.
- Pregunta si deseas crear una cuenta con el comando `/cuentas`, utilizando botones inline para responder.
- Maneja las respuestas a la pregunta de creación de cuenta, proporcionando feedback inmediato al usuario.