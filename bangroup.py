import requests
from urllib.parse import urlparse

def banna_gruppo_per_link(link_gruppo):
    token = "7186653711:AAGKDyG-G9MZw0SS4dTW2x0DzUf_SC9KB5s"
    url = f"https://api.telegram.org/bot{token}/kickChatMember"
    
    parsed_link = urlparse(link_gruppo)
    chat_id = parsed_link.path.replace("/", "")
    
    data = {
        'chat_id': chat_id,
        'user_id': 0
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("Gruppo bannato con successo!")
    else:
        print("Impossibile bannare il gruppo")

link_gruppo = "https://t.me/tbt_family"
banna_gruppo_per_link(link_gruppo)