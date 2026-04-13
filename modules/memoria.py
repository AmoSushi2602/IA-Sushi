import os

CAMINHO_MEMORIA = "data/memoria.txt"

def salvar_memoria(texto):
    with open(CAMINHO_MEMORIA, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def ler_memoria():
    if not os.path.exists(CAMINHO_MEMORIA):
        return ""
    
    with open(CAMINHO_MEMORIA, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    # pega só as últimas 10 linhas (pra não ficar gigante)
    return "".join(linhas[-10:])