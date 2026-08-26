label phone_menu:
    scene bg kvist
    menu:
        "[clients['nonni']['name_ru']] - [clients['nonni']['description_ru']]":
            jump expression "day" + str(current_day) + "_call_nonni"
        "[clients['bekker']['name_ru']] - [clients['bekker']['description_ru']]":
            jump expression "day" + str(current_day) + "_call_becker"
        "[clients['mikko']['name_ru']] - [clients['mikko']['description_ru']]":
            jump expression "day" + str(current_day) + "_call_mikko"
        "[clients['andrea']['name_ru']] - [clients['andrea']['description_ru']]":
            jump expression "day" + str(current_day) + "_call_andrea"
        "Назад":
            jump evening_menu