from ollama import chat

response = chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'What are the minimum specs to run ollama?'}],
)
print(response.message.content)