label start:

    $ clients = get_initial_clients()
    $ vars = get_initial_variables()
    $ current_day = vars["current_day"]
    $ money = vars["money"]
    $ actions = vars["actions"]
    $ wires = vars["wires"]
    $ chips = vars["chips"]

    menu:
        "Выберите языка"

        "Русский":
            $ renpy.change_language(None)

        "English":
            $ renpy.change_language("english")

    jump day1_intro

    return