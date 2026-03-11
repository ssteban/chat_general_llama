from gradio_client import Client
from util.recortar import recortar_respuesta

try:
    client = Client("mendey123/psico-bot")
except Exception as e:
    print(f"Error al conectar con el cliente de Gradio: {e}")
    client = None

def responder(mensaje):
    if client is None:
        return "Lo siento, en este momento no puedo conectarme con mi cerebro de IA. Por favor, inténtalo más tarde."
    
    try:
        result = client.predict(
            mensaje=mensaje,
            api_name="/responder",
        )
        if isinstance(result, str):
            return recortar_respuesta(result)
        else:
            print(f"Resultado inesperado de Gradio: {type(result)}")
            return str(result)
    except Exception as e:
        print(f"Error durante la predicción: {e}")
        return "Hubo un error al procesar tu pregunta. Por favor, inténtalo de nuevo."
