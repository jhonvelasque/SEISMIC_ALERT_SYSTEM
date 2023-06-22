from flask import Flask, render_template
import pymysql
from telegram import Bot

app = Flask(__name__)

    # Configura el token de acceso del bot de Telegram
TELEGRAM_TOKEN = '5434888778:AAFfhdNS9i9P4Iv1tKlFX5SXSuSlMjfFIxI'
bot = Bot(TELEGRAM_TOKEN)



    # Ruta principal
@app.route('/')
def index():
        return render_template('index.html')

    # Ruta para mostrar los datos más recientes de cada tabla
@app.route('/datos_recientes')
def datos_recientes():
        # Establecer la conexión a la base de datos
        conexion = pymysql.connect(
            host='database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com',
            user='luis'
            password='1234'
            database='alertasSismicas'
        )

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Lista de nombres de las tablas
        tablas = ['JAPAN', 'CHILE', 'USA']

        # Diccionario para almacenar los datos más recientes de cada tabla
        datos_recientes = {}

    

        # Enviar mensajes al bot de Telegram según el país
        for tabla, resultados in datos_recientes.items():
            for fila in resultados:
                idcountry = fila[1]
                mensaje = f"Nuevo sismo registrado:\n\nID Sismo: {fila[0]}\nMagnitud: {fila[2]}\nLugar: {fila[3]}\nFecha y Hora: {fila[4]}\nTsunami: {fila[5]}\nLongitud: {fila[6]}\nLatitud: {fila[7]}\nProfundidad: {fila[8]}\nPeligro: {fila[9]}"

            # Enviar el mensaje al bot de Telegram
                bot.send_message(chat_id=1589638921, text=mensaje)

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        # Renderizar la plantilla HTML y pasar los datos más recientes como contexto
        return render_template('datos_recientes.html', datos_recientes=datos_recientes)

if __name__ == '__main__':
    app.run()