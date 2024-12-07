# Bot de Telegram para Registro de Gastos

Este proyecto es un bot de Telegram que permite a los usuarios registrar sus gastos en una hoja de cálculo de Google Sheets. El bot guía al usuario a través de un proceso paso a paso para ingresar la fecha, el monto, la descripción y el tipo de gasto.

## Características

- **Registro de Gastos**: Los usuarios pueden registrar un nuevo gasto usando el comando `/gasto`.
- **Cancelación de Registro**: Los usuarios pueden cancelar el proceso de registro en cualquier momento usando el comando `/cancelar`.
- **Ayuda**: El bot proporciona una lista de comandos disponibles con el comando `/help`.
- **Fecha Automática**: Los usuarios pueden ingresar "hoy" para usar la fecha actual automáticamente.

## Requisitos

- Python 3.13 o superior
- Paquetes de Python: `telebot`, `decouple`, `gspread`
- Credenciales de Google API para acceder a Google Sheets

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows usa: .venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env`:

   ```
   TELEGRAM_TOKEN=tu_token_de_telegram
   SHEETS_ID=tu_id_de_hoja_de_calculo
   ```

5. Asegúrate de que la hoja de cálculo de Google Sheets esté compartida con la cuenta de servicio de Google. Para más información sobre cómo realizar este paso, puedes consultar este [video](https://www.youtube.com/watch?v=zCEJurLGFRk).

## Uso

Ejecuta el bot con el siguiente comando:

```bash
python main.py
```

## Comandos Disponibles

- `/start`: Inicia el bot y muestra un mensaje de bienvenida.
- `/help`: Muestra la lista de comandos disponibles.
- `/gasto`: Comienza el proceso de registro de un nuevo gasto.
- `/cancelar`: Cancela el proceso actual de registro de gasto.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
