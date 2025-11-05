from modules.auth import AuthManager

auth = AuthManager()

print(auth.register("marek", "geheim123"))
print(auth.login("marek", "geheim123"))
print(auth.login("marek", "falsch"))
print(auth.register("marek", "neu"))
