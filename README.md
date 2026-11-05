## Configuração da IA local no Windows

Este projeto utiliza o [Ollama](https://ollama.com/) para executar um modelo de linguagem localmente. Depois da configuração, não é necessário usar serviços de IA externos nem criar uma chave de API.

### 1. Instalar o Ollama

1. Acesse [ollama.com/download/windows](https://ollama.com/download/windows).
2. Baixe o instalador `OllamaSetup.exe`.
3. Execute o instalador.
4. Abra o Ollama pelo menu Iniciar.

O Ollama precisa continuar ativo em segundo plano enquanto o programa Python estiver sendo executado. A janela pode ser minimizada ou fechada, desde que o Ollama permaneça na bandeja do Windows.

### 2. Baixar o modelo local

Na tela de chat do Ollama:

1. Clique no seletor de modelos na parte inferior da janela.
2. Pesquise por:

```text
llama3.2:3b
```

3. Selecione a opção para baixar o modelo.
4. Aguarde o download, que possui aproximadamente 2 GB.
5. Selecione `llama3.2:3b` e envie uma mensagem para testar.

> Verifique se o modelo selecionado não possui o sufixo `:cloud`. Modelos com esse sufixo são executados na nuvem, e não localmente.

### 3. Instalar o Python

1. Acesse [python.org/downloads/windows](https://www.python.org/downloads/windows/).
2. Baixe e instale o Python.
3. Depois da instalação, feche e abra novamente o VS Code.

Também é possível instalar o Python pela Microsoft Store, desde que o aplicativo seja publicado pela **Python Software Foundation**.

### 4. Preparar o VS Code

Instale o [Visual Studio Code](https://code.visualstudio.com/) e abra a área de extensões.

Pesquise e instale:

```text
Python
```

Confira se o publicador da extensão é a **Microsoft**.

Não é necessário instalar extensões do Ollama, Jupyter, Docker, WSL ou Code Runner.


### 5. Instalar a biblioteca Python do Ollama

No VS Code, abra:

```text
Terminal → New Terminal
```

Execute:

```powershell
python -m pip install ollama
```

Se o comando `python` não for reconhecido, tente:

```powershell
py -m pip install ollama
```

Quando a instalação terminar, deverá aparecer uma mensagem semelhante a:

```text
Successfully installed ... ollama
```

Avisos informando que a pasta `Scripts` não está no `PATH` não impedem o funcionamento da biblioteca neste projeto.

### 6. Testar a conexão

Crie um arquivo chamado `teste_ia.py` com o seguinte conteúdo:

```python
from ollama import chat

resposta = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explique em uma frase o que é uma pilha.",
        }
    ],
)

print(resposta.message.content)
```

Certifique-se de que o Ollama esteja ativo e execute o arquivo pelo botão ▶ no canto superior direito do VS Code.

Se tudo estiver configurado corretamente, a resposta do modelo aparecerá no terminal integrado.

### Resolução de problemas

#### `Import "ollama" could not be resolved`

Se a biblioteca foi instalada, mas o VS Code continua mostrando esse aviso:

1. Feche e abra novamente o VS Code.

se continuar, algum passo anterior foi mal executado ou o vscode nao reconhece o python instalado no seu computador, busque auxilio para casos mais especificos.

#### Erro de conexão com o Ollama

Confira se:

- o aplicativo Ollama está aberto ou ativo na bandeja do Windows;
- o modelo `llama3.2:3b` terminou de baixar;
- o nome usado no código é exatamente `llama3.2:3b`;
- o modelo escolhido não possui o sufixo `:cloud`.

A API local do Ollama normalmente fica disponível em:

```text
http://localhost:11434
```

### Checklist

```text
[ ] Ollama instalado
[ ] llama3.2:3b baixado localmente
[ ] Ollama ativo em segundo plano
[ ] Python instalado
[ ] VS Code instalado
[ ] Extensão Python da Microsoft instalada
[ ] Biblioteca ollama instalada
[ ] teste_ia.py executado com sucesso
```


## Configuração da IA local no macOS

Abra o Terminal e confirme se o Homebrew está instalado:

```bash
brew --version
```

Caso não esteja, instale-o seguindo as instruções em [brew.sh](https://brew.sh/).

### 1. Instalar e iniciar o Ollama

```bash
brew install ollama
brew services start ollama
```

### 2. Baixar o modelo local

```bash
ollama pull llama3.2:3b
```

Confira se o modelo foi instalado:

```bash
ollama list
```

Teste conversando diretamente com ele:

```bash
ollama run llama3.2:3b
```

Para encerrar a conversa:

```text
/bye
```

### 3. Preparar o Python

Confira se o Python está instalado:

```bash
python3 --version
```

Caso não esteja:

```bash
brew install python
```

Dentro da pasta do projeto, crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale a biblioteca Python do Ollama:

```bash
python -m pip install ollama
```

### 4. Executar o projeto

Com o ambiente virtual ativo e o Ollama rodando:

```bash
python teste_ia.py
```

Nas próximas vezes, basta iniciar o Ollama e ativar o ambiente:

```bash
brew services start ollama
source .venv/bin/activate
python teste_ia.py
```

Para parar o serviço do Ollama:

```bash
brew services stop ollama
```
