class GroupManager:
    def __init__(self):
        self.groups = {}  # gruppenname → [usernames]

    def create_group(self, name):
        if name in self.groups:
            return "❌ Gruppe existiert bereits"
        self.groups[name] = []
        return "✅ Gruppe erstellt"

    def add_member(self, group, username):
        if group not in self.groups:
            return "❌ Gruppe nicht gefunden"
        if username in self.groups[group]:
            return "❌ Nutzer bereits in Gruppe"
        self.groups[group].append(username)
        return "✅ Nutzer hinzugefügt"

    def remove_member(self, group, username):
        if group not in self.groups:
            return "❌ Gruppe nicht gefunden"
        if username not in self.groups[group]:
            return "❌ Nutzer nicht in Gruppe"
        self.groups[group].remove(username)
        return "✅ Nutzer entfernt"

    def list_groups(self):
        return list(self.groups.keys())

    def list_members(self, group):
        if group not in self.groups:
            return "❌ Gruppe nicht gefunden"
        return self.groups[group]
