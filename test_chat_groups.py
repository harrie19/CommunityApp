from modules.chat import ChatManager

chat = ChatManager()

# Private Chat
chat.send_private_message("marek", "lisa", "Hi Lisa!")
chat.send_private_message("lisa", "marek", "Hey Marek!")

# Gruppennachrichten
chat.send_group_message("marek", "Entwickler", "Willkommen im Team!")
chat.send_group_message("lisa", "Entwickler", "Freu mich auf die Zusammenarbeit!")

# Ausgabe
print("🔒 Private Chat:")
for msg in chat.get_private_chat("marek", "lisa"):
    print(f"[{msg['timestamp']}] {msg['from']} → {msg['to']}: {msg['text']}")

print("\n👥 Gruppenchat Entwickler:")
for msg in chat.get_group_chat("Entwickler"):
    print(f"[{msg['timestamp']}] {msg['from']} → {msg['to']}: {msg['text']}")
