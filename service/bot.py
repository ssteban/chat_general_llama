import telebot
from dotenv import load_dotenv
import os
from service.bot_connect import responder

load_dotenv()

TOKEN = os.getenv("TOKEN_BOT")

def bot_init():
    if not TOKEN:
        print("ERROR: No se encontró el TOKEN_BOT en el archivo .env")
        return

    try:
        bot = telebot.TeleBot(TOKEN)
        print("Bot inicializado correctamente.")
    except Exception as e:
        print(f"Error al inicializar el bot: {e}")
        return

    @bot.message_handler(commands=['start'])
    def start(message):
        print(f"Comando /start recibido de {message.from_user.username}")
        texto = """
        Hola 👋 Soy un asistente de apoyo sobre aprendizaje y bienestar psicológico.

        ⚠️ Estoy diseñado para responder preguntas simples y generales.  
        No siempre puedo responder preguntas muy complejas o técnicas.

        Puedes empezar con preguntas como:

        1️⃣ ¿Qué es el TDAH?  
        2️⃣ ¿Qué es la dislexia?  
        3️⃣ ¿Qué actividades ayudan a un niño con dislexia? 
        4️⃣ ¿Cómo ayudar a un niño con TDAH?  
        5️⃣ Que es disgrafia? 


        💬 Escríbeme una pregunta para comenzar.
        """

        bot.reply_to(message, texto)

    @bot.message_handler(func=lambda message: True)
    def echo(message):
        user = message.from_user.username or message.from_user.first_name
        print(f"Mensaje de {user}: {message.text}")
        
        try:
            bot.send_message(message.chat.id, "Procesando tu pregunta...", reply_to_message_id=message.message_id)
            bot.send_chat_action(message.chat.id, 'typing')
            respuesta = responder(message.text)
            bot.reply_to(message, respuesta)
        except Exception as e:
            print(f"Error al responder: {e}")
            bot.reply_to(message, "Lo siento, tuve un problema interno. Inténtalo de nuevo más tarde.")

    print("Bot corriendo...")
    bot.infinity_polling()