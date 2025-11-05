from datetime import datetime

class ChatManager:
    def __init__(self):
        self.private_chats = {}  # (user1, user2) → list of messages
        self.group_chats = {}    # group_name → list of messages

    def send_private_message(self, sender, receiver, text):
        key = tuple(sorted([sender, receiver]))
        if key not in self.private_chats:
            self.private_chats[key] = []
        message = self._build_message(sender, receiver, text)
        self.private_chats[key].append(message)
        return "✅ Private Nachricht gesendet"

    def get_private_chat(self, user1, user2):
        key = tuple(sorted([user1, user2]))
        return self.private_chats.get(key, [])

    def send_group_message(self, sender, group, text):
        if group not in self.group_chats:
            self.group_chats[group] = []
        message = self._build_message(sender, group, text)
        self.group_chats[group].append(message)
        return "✅ Gruppennachricht gesendet"

    def get_group_chat(self, group):
        return self.group_chats.get(group, [])

    def _build_message(self, sender, target, text):
        return {
            "from": sender,
            "to": target,
            "text": text,
            "timestamp": datetime.now().isoformat()
        }
