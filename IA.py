import requests

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer rp-rO4osnsysQi3R5HPpqaYwIvXLgDdgdGJWjGC3Y61EeR4E6d9"
}

def get_input_response(input_text):
    data = {
        "model": "text-davinci-003",
        "messages": [
            {"role": "user", "content": input_text}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error accessing the AI model"

def get_my_response(user_input):
    response = get_input_response(user_input)
    if "choices" in response:
        for choice in response["choices"]:
            if choice["role"] == "assistant":
                return choice['message']['content']
    return "Error processing the response."

print("Benvenuto nella chat di Anarchy🖤! Digita 'exit' per uscire.")
while True:
    question = input("You: ")
    
    if question.lower() == 'exit':
        print("Grazie per il caos creato insieme! Arrivederci! 🖤🔥")
        break
    
    response = get_my_response(question)
    print("Anarchy🖤:", response)