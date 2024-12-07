import gspread # high level API on the top of google api
from google.oauth2.service_account import Credentials
from decouple import config

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheets_id = config('SHEETS_ID')
sheet = client.open_by_key(sheets_id)

try:
    api_worksheet = sheet.worksheet("API")
except gspread.exceptions.WorksheetNotFound:
    raise Exception("No se pudo acceder a la hoja 'API'. Verifique que exista y que tenga los permisos adecuados.")

# Function to write data to the spreadsheet
def escribir_en_hoja_de_calculo(fecha_str, monto_gasto, descripcion, tipo_gasto, row):
    """Writes expense data to the specified row in the spreadsheet.

    Args:
        fecha_str (str): The date of the expense in string format.
        monto_gasto (float): The amount of the expense.
        descripcion (str): The description of the expense.
        tipo_gasto (str): The type of the expense.
        row (int): The row number where the data will be written.
    """
    api_worksheet.update_cell(row, 1, fecha_str)
    api_worksheet.update_cell(row, 2, monto_gasto)
    api_worksheet.update_cell(row, 3, descripcion)
    api_worksheet.update_cell(row, 4, tipo_gasto)

def obtener_ultima_fila_con_datos_columna(columna):
    """Returns the last row number with data in the specified column of the spreadsheet.

    Args:
        columna (int): The column number to check for data.

    Returns:
        int: The last row number with data in the specified column.
    """
    col_data = api_worksheet.col_values(columna)
    return len(col_data)


def obtener_gastos_del_mes():
    pass #TODO: Implementar