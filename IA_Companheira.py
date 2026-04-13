from modules.ia import perguntar_ia
from modules.voz import falar
from modules.memoria import salvar_memoria
from config import NOME_IA, MENSAGEM_INICIAL, COMANDOS_SAIR

print(f"🌸 {NOME_IA}: {MENSAGEM_INICIAL}\n")

while True:
    pergunta = input("🧑 Você: ")

    if pergunta.lower() in COMANDOS_SAIR:
        print(f"{NOME_IA}: Até mais... ")
        break

    resposta = perguntar_ia(pergunta)

    print(f"🌸 {NOME_IA}:", resposta)
    falar(resposta)

    # salva memória
    salvar_memoria(f"Usuário: {pergunta}")
    salvar_memoria(f"{NOME_IA}: {resposta}")