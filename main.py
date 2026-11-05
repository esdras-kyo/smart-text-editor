from ollama import chat

resposta = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explique por que o comando CTRL+Z é tão importante para a humanidade.",
        }
    ],
)

print(resposta.message.content)