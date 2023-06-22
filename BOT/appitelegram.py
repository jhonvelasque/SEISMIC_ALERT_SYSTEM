import telegram
import pymysql  
from telegram.ext import Updater, CommandHandler
from queue import Queue
import folium 
import emoji

    # Token del bot proporcionado por BotFather
TOKENS = '5434888778:AAFfhdNS9i9P4Iv1tKlFX5SXSuSlMjfFIxI'



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='¡Hola! Utiliza los comandos /japan, /chile o /usa para obtener información sobre los últimos sismos registrados.')

    # Resto del código para los comandos 'japan', 'chile' y 'usa'

def japan(update, context):
    # Establecer la conexión a la base de datos
    conexion = pymysql.connect(
        host='database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com',
        user='luis',
        password='1234',
        database='alertasSismicas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Obtener el último sismo registrado en la tabla JAPAN
    cursor.execute("SELECT * FROM JAPAN ORDER BY time DESC LIMIT 1")
    resultado = cursor.fetchone()

    if resultado:
        # Verificar si el dato ya ha sido enviado anteriormente
        ultimo_dato_enviado = context.bot_data.get('ultimo_dato_japan')
        if ultimo_dato_enviado and ultimo_dato_enviado == resultado:
            mensaje = "No hay actualizaciones en los sismos de JAPAN."
        else:
            magnitud = resultado[2]
            if magnitud < 6:
                peligro_emoji = "⚪️ Nivel Bajo ⚪️"
            elif magnitud < 7.8:
                peligro_emoji = "🟡 Nivel Medio 🟡"
            else:
                peligro_emoji = "🔴 Nivel Peligroso 🔴"
            fecha_hora = resultado[4].strftime("%Y-%m-%d %H:%M:%S")

            mensaje = f"Último sismo registrado en JAPAN:\n\nFecha y Hora: {fecha_hora}\nLatitud: {resultado[7]}\nLongitud: {resultado[6]}\nProfundidad: {resultado[8]}\nMagnitud: {magnitud} {peligro_emoji}"
            
            # Actualizar el último dato enviado
            context.bot_data['ultimo_dato_japan'] = resultado
    else:
        mensaje = "No se encontraron sismos registrados en JAPAN."

    # Enviar el mensaje al chat
    context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()


def chile(update, context):
    # Establecer la conexión a la base de datos
    conexion = pymysql.connect(
        host='database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com',
        user='luis',
        password='1234',
        database='alertasSismicas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Obtener el último sismo registrado en la tabla CHILE
    cursor.execute("SELECT * FROM CHILE ORDER BY time DESC LIMIT 1")
    resultado = cursor.fetchone()

    if resultado:
        # Verificar si el dato ya ha sido enviado anteriormente
        ultimo_dato_enviado = context.bot_data.get('ultimo_dato_chile')
        if ultimo_dato_enviado and ultimo_dato_enviado == resultado:
            mensaje = "No hay actualizaciones en los sismos de CHILE."
        else:
            magnitud = resultado[2]
            if magnitud < 6:
                peligro_emoji = "⚪️ Nivel Bajo ⚪️"
            elif magnitud < 7.8:
                peligro_emoji = "🟡 Nivel Medio 🟡"
            else:
                peligro_emoji = "🔴 Nivel Peligroso 🔴"
            fecha_hora = resultado[4].strftime("%Y-%m-%d %H:%M:%S")

            mensaje = f"Último sismo registrado en CHILE:\n\nFecha y Hora: {fecha_hora}\nLatitud: {resultado[7]}\nLongitud: {resultado[6]}\nProfundidad: {resultado[8]}\nMagnitud: {magnitud} {peligro_emoji}"
            
            # Actualizar el último dato enviado
            context.bot_data['ultimo_dato_chile'] = resultado
    else:
        mensaje = "No se encontraron sismos registrados en CHILE."

    # Enviar el mensaje al chat
    context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

def usa(update, context):
    # Establecer la conexión a la base de datos
    conexion = pymysql.connect(
        host='database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com',
        user='luis',
        password='1234',
        database='alertasSismicas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Obtener el último sismo registrado en la tabla USA
    cursor.execute("SELECT * FROM USA ORDER BY time DESC LIMIT 1")
    resultado = cursor.fetchone()

    if resultado:
        # Verificar si el dato ya ha sido enviado anteriormente
        ultimo_dato_enviado = context.bot_data.get('ultimo_dato_usa')
        if ultimo_dato_enviado and ultimo_dato_enviado == resultado:
            mensaje = "No hay actualizaciones en los sismos de USA."
        else:
            pais = "JAPAN"
            if resultado[1] == 1:
                pais = "CHILE"
            elif resultado[1] == 2:
                pais = "EE. UU."
            elif resultado[1] == 3:
                pais = "JAPÓN"

            magnitud = resultado[2]
            if magnitud < 6:
                peligro_emoji = "⚪️ Nivel Bajo ⚪️"
            elif magnitud < 7.8:
                peligro_emoji = "🟡 Nivel Medio 🟡"
            else:
                peligro_emoji = "🔴 Nivel Peligroso 🔴"
            fecha_hora = resultado[4].strftime("%Y-%m-%d %H:%M:%S")

            mensaje = f"Último sismo registrado en USA:\n\nFecha y Hora: {fecha_hora}\nLatitud: {resultado[7]}\nLongitud: {resultado[6]}\nPaís: {pais}\nProfundidad: {resultado[8]}\nMagnitud: {magnitud} {peligro_emoji}"
            
            # Actualizar el último dato enviado
            context.bot_data['ultimo_dato_usa'] = resultado
    else:
        mensaje = "No se encontraron sismos registrados en USA."

    # Enviar el mensaje al chat
    context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()


def main():
        updater = Updater(token=TOKENS, use_context=True)
        dispatcher = updater.dispatcher

        # Manejador para el comando /start
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        # Manejador para el comando /japan
        japan_handler = CommandHandler('japan', japan)
        dispatcher.add_handler(japan_handler)

        # Manejador para el comando /chile
        chile_handler = CommandHandler('chile', chile)
        dispatcher.add_handler(chile_handler)

        # Manejador para el comando /usa
        usa_handler = CommandHandler('usa', usa)
        dispatcher.add_handler(usa_handler)

            # Iniciar el bot
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    main()