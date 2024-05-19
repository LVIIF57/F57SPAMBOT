# F57SPAMBOT
FUCKSCAMMERS
import logging
import random
from telegram import Bot
from telegram.error import TelegramError

# Imposta il bot Telegram con il tuo token
bot = Bot(token=YOUR BOT TOKEN

# ID della chat di destinazione
target_chat_id = CHAD ID TO SPAMMING

# Lista di messaggi da inviare
messages = [
    'FUCK THE SCAMMERS CLEAN THE HAT FROM THIS SHIT' for _ in range(50)
]

# Funzione per inviare un messaggio nella chat di destinazione
def send_message(chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print(f'Messaggio inviato con successo alla chat {chat_id}: {message}')
    except TelegramError as e:
        print(f'Impossibile inviare il messaggio: {e}')

# Invia messaggi in modo concorrente
with concurrent.futures.ThreadPoolExecutor() as executor:
    for message in messages:
        executor.submit(send_message, target_chat_id, message)
