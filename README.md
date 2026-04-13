# 🌸 IA do Sushi (Reisa AI)

Uma IA estilo anime que conversa, fala e lembra de você.(TSUNDERE)

## Funcionalidades

- Conversa com IA local (Ollama)
- Voz em português (Coqui TTS)
- Memória de conversas
- Personalidade estilo anime

## Como rodar

## 1. Clone o repositório

```bash
git clone https://github.com/AmoSushi2602/IA-Sushi.git
cd IA-Sushi
```

## 2. Crie o ambiente virtual
```Bash
python - m venv tts_env
```

## 3. ative o ambiente 
```
tts_env\Scripts\activate
```
no caminho!

## 4. Instale as dependências

```
pip install -r requirements.txt
```

## 5. Instale e inicie o Ollama

Baixe: https://ollama.com/

Depois rode:
```
ollama serve
```

## 6. Execute a IA
```
python IA_Companheira.py

```

Você pode personalizar sua IA no arquivo:
  config.py

Estrutura do projeto
IA-Sushi/
│
├── IA_Companheira.py
├── config.py
├── requirements.txt
│
├── modules/
│   ├── ia.py
│   ├── voz.py
│   ├── memoria.py
│
└── data/
    └── memoria.txt

Tecnologias utilizadas
.Python
.Ollama (LLM local)
.Coqui TTS (voz)

Ideias futuras
.Avatar 3D animado
.Emoções dinâmicas
.Interface gráfica (janela)
.Controle do computador
.Integração com jogos

Observações:
.O projeto roda 100% local (sem depender de APIs externas)
.O desempenho depende do seu computador
.Modelos mais leves (ex: phi3) são mais rápidos

Contribuição
  Sinta-se livre para contribuir com melhorias!

