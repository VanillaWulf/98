# default clients = {
#     "nonni": {
#         "name": "Нонни",
#         "description": "Держит больницу в городе",
#         "phone": True,
#         "order_name": "Аппарат диагностики",
#         "order_active": True,
#         "order_completed": False,
#         "repair_day": None,
#         "repair_price": None,
#         "called": 0,
#         "wine_offered": False,     
#         "wine_accepted": False,  
#         "wine_complete": False,
#         "banned": False,
#         "foreverbanned": False,
#     },
#     "linh": {
#         "name": "Линь Чи",
#         "description": "Пожилая женщина.",
#         "phone": False,
#         "order_name": "Плеер",
#         "order_active": False,
#         "order_completed": False,
#         "repair_day": None,
#         "repair_price": None,
#         "called": 0,
#         "burned" : False
#     },
#     "bekker": {
#         "name": "Беккер",
#         "description": "Поставщик деталей",
#         "phone": True,
#         "order_name": "Модуль магнитного самоката",  
#         "order_active": False,
#         "order_completed": False,
#         "repair_day": None,
#         "repair_price": None,
#         "ordered_part": None,   
#         "called": 0,
#         "base_price": 7,
#         "banned": False,
#         "foreverbanned": False
#     },
#     "mikko": {
#         "name": "Микко",
#         "description": "Старый друг.",
#         "phone": True,
#         "called": 0,         
#         "hangouts": 0,
#         "hangouts_day_1": False,
#         "hangouts_day_2": False,
#         "hangouts_day_3": False,
#         "calls_per_week": 0,
#         "banned": False,
#         "is_called": False
#     },
#     "ivo": {
#         "name": "Иво",
#         "description": "Специалист по взлому компов",
#         "phone": False,
#         "order_name": "Браслет комуникатора",  
#         "order_active": False,
#         "order_completed": False,
#         "repair_day": None,
#         "repair_price": None,
#         "banned": False,
#         "called": 0, 
#     },
#      "andrea": {
#         "name": "Андреа",
#         "description": "Дочь Квиста...",
#         "called": 0,
#         "takeaway": False,
#         "cure_price": 20,
#         "nonni_delivered": False,
#         "medicine_bought": False
#     },
#     "pol": {
#         "name": "Пол",
#         "made_raid": False,
#         "base_price": 20,
#         "hacked": False,
#         "get_jailed": False
#     },
# }
default clients = {
    "nonni": {
        "name_ru": "Нонни",
        "name_en": "Nonni",

        "description_ru": "Держит больницу в городе",
        "description_en": "Runs a hospital in the city",

        "order_name_ru": "Аппарат диагностики",
        "order_name_en": "Diagnostic Device",

        "phone": True,
        "order_active": True,
        "order_completed": False,
        "repair_day": None,
        "repair_price": None,
        "called": 0,
        "wine_offered": False,
        "wine_accepted": False,
        "wine_complete": False,
        "banned": False,
        "foreverbanned": False,
    },

    "linh": {
        "name_ru": "Линь Чи",
        "name_en": "Lin Chi",

        "description_ru": "Пожилая женщина.",
        "description_en": "An elderly woman.",

        "order_name_ru": "Плеер",
        "order_name_en": "Music Player",

        "phone": False,
        "order_active": False,
        "order_completed": False,
        "repair_day": None,
        "repair_price": None,
        "called": 0,
        "burned": False,
    },

    "bekker": {
        "name_ru": "Беккер",
        "name_en": "Bekker",

        "description_ru": "Поставщик деталей",
        "description_en": "Parts Supplier",

        "order_name_ru": "Модуль магнитного самоката",
        "order_name_en": "Mag-Scooter Module",

        "phone": True,
        "order_active": False,
        "order_completed": False,
        "repair_day": None,
        "repair_price": None,
        "ordered_part": None,
        "called": 0,
        "base_price": 7,
        "banned": False,
        "foreverbanned": False,
    },

    "mikko": {
        "name_ru": "Микко",
        "name_en": "Mikko",

        "description_ru": "Старый друг.",
        "description_en": "Old Friend",

        "phone": True,
        "called": 0,
        "hangouts": 0,
        "hangouts_day_1": False,
        "hangouts_day_2": False,
        "hangouts_day_3": False,
        "calls_per_week": 0,
        "banned": False,
        "is_called": False,
    },

    "ivo": {
        "name_ru": "Иво",
        "name_en": "Ivo",

        "description_ru": "Специалист по взлому компов",
        "description_en": "Security Researcher",

        "order_name_ru": "Браслет коммуникатора",
        "order_name_en": "Communicator Bracelet",

        "phone": False,
        "order_active": False,
        "order_completed": False,
        "repair_day": None,
        "repair_price": None,
        "banned": False,
        "called": 0,
    },

    "andrea": {
        "name_ru": "Андреа",
        "name_en": "Andrea",

        "description_ru": "Дочь Квиста...",
        "description_en": "Kvist's Daughter...",

        "called": 0,
        "takeaway": False,
        "cure_price": 20,
        "nonni_delivered": False,
        "medicine_bought": False,
    },

    "pol": {
        "name_ru": "Пол",
        "name_en": "Paul",

        "description_ru": "Сотрудник ОКБР",
        "description_en": "OKBR Officer",

        "made_raid": False,
        "base_price": 20,
        "hacked": False,
        "get_jailed": False,
    },
}

init python:

    def tr(client_id, field):
        lang = renpy.game.preferences.language

        if lang == "english":
            return clients[client_id][field + "_en"]

        return clients[client_id][field + "_ru"]