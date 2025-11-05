from modules.groups import GroupManager

gm = GroupManager()

print(gm.create_group("Entwickler"))
print(gm.add_member("Entwickler", "marek"))
print(gm.add_member("Entwickler", "lisa"))
print(gm.list_members("Entwickler"))
print(gm.remove_member("Entwickler", "lisa"))
print(gm.list_members("Entwickler"))
print(gm.create_group("Entwickler"))  # doppelt
print(gm.list_groups())
