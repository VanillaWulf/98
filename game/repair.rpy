# label repair_menu:
#     if actions > 0:
#         menu:
#             "[clients['nonni']['name']] - [clients['nonni']['order_name']]" if clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:
#                 jump repair_nonni
#             "[clients['linh']['name']] - [clients['linh']['order_name']]" if clients["linh"]["order_active"] and not clients["linh"]["order_completed"]:
#                 jump repair_linchi
#             "[clients['bekker']['name']] - [clients['bekker']['order_name']]" if clients["bekker"]["order_active"] and not clients["bekker"]["order_completed"]:
#                 jump repair_becker
#             "[clients['ivo']['name']] - [clients['ivo']['order_name']]" if clients["ivo"]["order_active"] and not clients["ivo"]["order_completed"]:
#                 jump repair_ivo
#             "Назад":
#                 jump evening_menu
#     else:
#         "Квист очень устал, ему бы поспать"
#         jump evening_menu

# label repair_nonni:
#     if wires >= 1 and chips >= 1:
#         play sound "repair.mp3" noloop
#         $ wires -= 1
#         $ chips -= 1
#         $ actions -= 1
#         $ clients["nonni"]["order_completed"] = True
#         "Минус схема, минус провод, зато заказ для Нонни готов"
#     else:
#         "Не хватает деталей (нужен провод и микросхема)."
#     jump evening_menu

# label repair_linchi:
#     if wires >= 1 and chips >= 1:
#         play sound "repair.mp3" noloop
#         $ chips -= 1
#         $ wires -= 1
#         $ actions -= 1
#         $ clients["linh"]["order_completed"] = True
#         "Минус схема, минус провод, зато заказ для бабушки Линь готов"
#     else:
#         "Не хватает деталей (нужен провод и микросхема).."
#     jump evening_menu

# label repair_becker:
#     if wires >= 1 and chips >= 1:
#         play sound "repair.mp3" noloop
#         $ wires -= 1
#         $ chips -= 1
#         $ actions -= 1
#         $ clients["bekker"]["order_completed"] = True
#         "Минус схема, минус провод, зато заказ для Беккера готов"
#     else:
#         "Не хватает деталей (нужен провод и микросхема)."
#     jump evening_menu

# label repair_ivo:
#     if wires >= 1 and chips >= 1:
#         play sound "repair.mp3" noloop
#         $ wires -= 1
#         $ chips -= 1
#         $ actions -= 1
#         $ clients["ivo"]["order_completed"] = True
#         "Минус схема, минус провод, зато заказ для Иво готов"
#     else:
#         "Не хватает деталей (нужен провод и микросхема)."
#     jump evening_menu

label repair_menu:
    if actions > 0:
        menu:
            "[tr('nonni', 'name')] - [tr('nonni', 'order_name')]" if clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:
                jump repair_nonni
            "[tr('linh', 'name')] - [tr('linh', 'order_name')]" if clients["linh"]["order_active"] and not clients["linh"]["order_completed"]:
                jump repair_linchi
            "[tr('bekker', 'name')] - [tr('bekker', 'order_name')]" if clients["bekker"]["order_active"] and not clients["bekker"]["order_completed"]:
                jump repair_becker
            "[tr('ivo', 'name')] - [tr('ivo', 'order_name')]" if clients["ivo"]["order_active"] and not clients["ivo"]["order_completed"]:
                jump repair_ivo
            "Назад":
                jump evening_menu
    else:
        "Квист очень устал, ему бы поспать"
        jump evening_menu

label repair_nonni:
    if wires >= 1 and chips >= 1:
        play sound "repair.mp3" noloop
        $ wires -= 1
        $ chips -= 1
        $ actions -= 1
        $ clients["nonni"]["order_completed"] = True
        "Минус схема, минус провод, зато заказ для [tr('nonni', 'name')] готов"
    else:
        "Не хватает деталей (нужен провод и микросхема)."
    jump evening_menu

label repair_linchi:
    if wires >= 1 and chips >= 1:
        play sound "repair.mp3" noloop
        $ chips -= 1
        $ wires -= 1
        $ actions -= 1
        $ clients["linh"]["order_completed"] = True
        "Минус схема, минус провод, зато заказ для [tr('linh', 'name')] готов"
    else:
        "Не хватает деталей (нужен провод и микросхема).."
    jump evening_menu

label repair_becker:
    if wires >= 1 and chips >= 1:
        play sound "repair.mp3" noloop
        $ wires -= 1
        $ chips -= 1
        $ actions -= 1
        $ clients["bekker"]["order_completed"] = True
        "Минус схема, минус провод, зато заказ для [tr('bekker', 'name')] готов"
    else:
        "Не хватает деталей (нужен провод и микросхема)."
    jump evening_menu

label repair_ivo:
    if wires >= 1 and chips >= 1:
        play sound "repair.mp3" noloop
        $ wires -= 1
        $ chips -= 1
        $ actions -= 1
        $ clients["ivo"]["order_completed"] = True
        "Минус схема, минус провод, зато заказ для [tr('ivo', 'name')] готов"
    else:
        "Не хватает деталей (нужен провод и микросхема)."
    jump evening_menu