def recortar_respuesta(texto):
    """
    Recorta la respuesta del modelo si detecta que intenta continuar la conversación 
    por sí mismo repitiendo palabras clave o el formato de respuesta.
    """
    if not texto:
        return ""
    
    # Lista de marcadores que indican que el modelo está intentando autocompletar
    marcadores = ["Respuesta:", "Pregunta:", "User:", "Bot:"]
    
    # Primero, si el texto empieza con "Respuesta:", lo quitamos para procesar el contenido real
    if texto.strip().startswith("Respuesta:"):
        texto = texto.strip()[len("Respuesta:"):].strip()
    
    # Buscamos si alguno de los marcadores aparece en el resto del texto
    puntos_de_corte = []
    for marcador in marcadores:
        idx = texto.find(marcador)
        if idx != -1:
            puntos_de_corte.append(idx)
    
    # Si encontramos algún marcador, recortamos en la posición del primero que aparezca
    if puntos_de_corte:
        texto = texto[:min(puntos_de_corte)]
            
    return texto.strip()
