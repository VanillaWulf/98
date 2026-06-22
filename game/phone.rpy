label phone_menu:
    scene bg kvist
    menu:
        "Нонни - [clients['nonni']['description']]":
            jump expression "day" + str(current_day) + "_call_nonni"
        "Беккер - [clients['bekker']['description']]":
            jump expression "day" + str(current_day) + "_call_becker"
        "Микко - [clients['mikko']['description']]":
            jump expression "day" + str(current_day) + "_call_mikko"
        "Андреа - [clients['andrea']['description']]":
            jump expression "day" + str(current_day) + "_call_andrea"
        "Назад":
            jump evening_menu