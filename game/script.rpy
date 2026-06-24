
label start:

    menu:
        "Choose language"

        "Русский":
            $ renpy.change_language(None)

        "English":
            $ renpy.change_language("english")

    jump day1_intro

    return