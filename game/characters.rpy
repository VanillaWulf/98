# define k = Character(_("Kvist"), who_color="#c8c8ff")
# define n = Character(_("Nonni"), who_color="#90c8ff")
# define l = Character(_("Lin Chi"), who_color="#ffd8b0")
# define b = Character(_("Bekker"), who_color="#d0a0ff")
# define m = Character(_("Mikko"), who_color="#a0ffa0")
# define a = Character(_("Andrea"), who_color="#ffa0a0")
# define i = Character(_("Ivo"), who_color="#c0c0c0")
# define p = Character(_("Paul"), who_color="#c0c0c0")

# define k = Character("Квист", who_color="#c8c8ff")
# define n = Character("Нонни", who_color="#90c8ff")
# define l = Character("Линь Чи", who_color="#ffd8b0")
# define b = Character("Беккер", who_color="#d0a0ff")
# define m = Character("Микко", who_color="#a0ffa0")
# define a = Character("Андреа", who_color="#ffa0a0")
# define i = Character("Иво", who_color="#c0c0c0")
# define p = Character("Пол", who_color="#c0c0c0")

init python:
    def tr(client_id, field):
        lang = renpy.game.preferences.language
        if lang == "english":
            return clients[client_id][field + "_en"]
        return clients[client_id][field + "_ru"]

    def get_name(char_id):  # <--- ИСПРАВЛЕНО: chtr_id -> char_id
        lang = renpy.game.preferences.language
        if lang == "english":
            return clients[char_id]["name_en"]
        return clients[char_id]["name_ru"]

# Но DynamicCharacter не может принимать параметры напрямую,
# поэтому используем lambda:
define k = DynamicCharacter(lambda: get_name("kvist"), who_color="#c8c8ff")
define n = DynamicCharacter(lambda: get_name("nonni"), who_color="#90c8ff")
define l = DynamicCharacter(lambda: get_name("linh"), who_color="#ffd8b0")
define b = DynamicCharacter(lambda: get_name("bekker"), who_color="#d0a0ff")
define m = DynamicCharacter(lambda: get_name("mikko"), who_color="#a0ffa0")
define a = DynamicCharacter(lambda: get_name("andrea"), who_color="#ffa0a0")
define i = DynamicCharacter(lambda: get_name("ivo"), who_color="#c0c0c0")
define p = DynamicCharacter(lambda: get_name("pol"), who_color="#c0c0c0")