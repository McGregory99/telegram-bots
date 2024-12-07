import telebot
from decouple import config
from datetime import datetime
from spreadsheet import escribir_en_hoja_de_calculo, obtener_ultima_fila_con_datos_columna, obtener_gastos_del_mes

TOKEN = config('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Dictionary to store user states
user_states = {}

class UserState:
    def __init__(self):
        self.fecha = None
        self.monto = None
        self.descripcion = None
        self.tipo_gasto = None
        self.step = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy tu bot de gastos. Usa /help para ver los comandos disponibles.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Comandos disponibles:\n"
        "/start - Inicia el bot\n"
        "/help - Muestra esta ayuda\n"
        "/gasto - Comienza el proceso de registro de un nuevo gasto\n"
        "/cancelar - Cancela el proceso actual de registro"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['cancelar'])
def cancel_expense(message):
    user_id = message.from_user.id
    if user_id in user_states:
        del user_states[user_id]
        bot.reply_to(message, "Proceso de registro cancelado.")
    else:
        bot.reply_to(message, "No hay ningún proceso activo para cancelar.")

@bot.message_handler(commands=['gasto'])
def start_expense_registration(message):
    user_id = message.from_user.id
    user_states[user_id] = UserState()
    bot.reply_to(message, "Por favor, ingresa la fecha del gasto (DD/MM/YYYY) o 'hoy':")

@bot.message_handler(func=lambda message: message.from_user.id in user_states)
def handle_expense_input(message):
    user_id = message.from_user.id
    state = user_states[user_id]
    
    try:
        if state.step == 0:  # Fecha
            if message.text.lower() == "hoy":
                # Set today's date in the correct format
                state.fecha = datetime.now().strftime("%d/%m/%Y")
            else:
                # Validate date format
                datetime.strptime(message.text, "%d/%m/%Y")
                state.fecha = message.text
            state.step = 1
            bot.reply_to(message, "Ingresa el monto del gasto:")
        
        elif state.step == 1:  # Monto
            monto = float(message.text.replace(',', '.'))
            state.monto = monto
            state.step = 2
            bot.reply_to(message, "Ingresa la descripción del gasto:")
        
        elif state.step == 2:  # Descripción
            state.descripcion = message.text
            state.step = 3
            bot.reply_to(message, "Ingresa el tipo de gasto:")
        
        elif state.step == 3:  # Tipo de gasto
            state.tipo_gasto = message.text
            # Get next available row
            next_row = obtener_ultima_fila_con_datos_columna(1) + 1
            # Save to spreadsheet
            escribir_en_hoja_de_calculo(
                state.fecha,
                state.monto,
                state.descripcion,
                state.tipo_gasto,
                next_row
            )
            
            # Confirmation message with details
            confirmation_message = (
                f"✅ Gasto registrado correctamente!\n"
                f"┌───────────────────────────────┐\n"
                f" Fecha: {state.fecha}\n"
                f" Monto: {state.monto}\n"
                f" Descripción: {state.descripcion}\n"
                f" Tipo de gasto: {state.tipo_gasto}\n"
                f"└───────────────────────────────┘"
            )
            print(confirmation_message)
            bot.reply_to(message, confirmation_message)
            del user_states[user_id]
    
    except ValueError as e:
        if state.step == 0:
            bot.reply_to(message, "❌ Formato de fecha incorrecto. Usa DD/MM/YYYY o 'hoy':")
        elif state.step == 1:
            bot.reply_to(message, "❌ El monto debe ser un número. Intenta nuevamente:")
        else:
            bot.reply_to(message, "❌ Error en el formato. Intenta nuevamente.")

@bot.message_handler(commands=['gastos_mes'])
def show_monthly_expenses(message):
    user_id = message.from_user.id
    try:
        # Obtener los gastos del mes
        gastos = obtener_gastos_del_mes()
        if not gastos:
            bot.reply_to(message, "No hay gastos registrados para este mes.")
            return
        
        # Formatear los gastos para el mensaje
        gastos_mensaje = "Gastos del mes:\n"
        for gasto in gastos:
            gastos_mensaje += (
                f"Fecha: {gasto['fecha']}, "
                f"Monto: {gasto['monto']}, "
                f"Descripción: {gasto['descripcion']}, "
                f"Tipo: {gasto['tipo_gasto']}\n"
            )
        
        bot.reply_to(message, gastos_mensaje)
    except Exception as e:
        bot.reply_to(message, "Hubo un error al obtener los gastos del mes. Intenta nuevamente más tarde.")
        print(f"Error al obtener los gastos del mes: {e}")

if __name__ == '__main__':
    bot.infinity_polling()