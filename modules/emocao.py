emocao = "neutra"

def analisar_emocao(texto):
    global emocao

    texto = texto.lower()

    if "amo" in texto or "gosto" in texto:
        emocao = "feliz"
    elif "odeio" in texto or "chato" in texto:
        emocao = "irritada"
    elif "tchau" in texto:
        emocao = "triste"
    else:
        emocao = "neutra"

    return emocao