import hashlib

class AuthManager:
    def __init__(self):
        self.users = {}  # username → hashed password

    def register(self, username, password):
        if username in self.users:
            return "❌ Benutzername existiert bereits"
        self.users[username] = self._hash(password)
        return "✅ Registrierung erfolgreich"

    def login(self, username, password):
        if username not in self.users:
            return "❌ Benutzer nicht gefunden"
        if self.users[username] != self._hash(password):
            return "❌ Passwort falsch"
        return "✅ Login erfolgreich"

    def _hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
