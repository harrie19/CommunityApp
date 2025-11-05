from modules.chat import ChatManager

chat = ChatManager()

print(chat.send_message("marek", "lisa", "Hey Lisa!"))
print(chat.send_message("lisa", "marek", "Hi Marek, alles klar?"))
print(chat.send_message("marek", "lisa", "Läuft bei mir!"))

for msg in chat.get_chat("marek", "lisa"):
    print(f"[{msg['timestamp']}] {msg['from']} → {msg['to']}: {msg['text']}")
