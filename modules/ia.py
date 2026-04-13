import requests
from config import PERSONALIDADE, MODELO_IA, NOME_IA
from modules.memoria import ler_memoria
from modules.emocao import analisar_emocao

def perguntar_ia(pergunta):
    memoria = ler_memoria()
    emocao =  analisar_emocao(pergunta)


    prompt = f"""
{PERSONALIDADE}

Estado emocional atual: {emocao}

Usuário: {pergunta}
{NOME_IA}:
"""

    resposta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODELO_IA,
            "prompt": prompt,
            "stream": False
        }
    )

    data = resposta.json()
    return data.get("response", "Hmmm... não entendi 😅")