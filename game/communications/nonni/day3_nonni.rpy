label day3_call_nonni:

if clients["nonni"]["foreverbanned"]:
    scene bg call_no_answer
    play sound "call_no_answer.mp3" noloop
    n "..."
    "Нонни не отвечает."
    k "Я ее серьезно достал в этот раз"
    jump phone_menu

if clients["nonni"]["banned"]:
    scene bg call_no_answer
    play sound "call_no_answer.mp3" noloop
    n "..."
    "Нонни не отвечает."
    jump phone_menu

$ clients["nonni"]["called"] += 1

# ---------------- ПЕРВЫЙ ЗВОНОК ----------------

if clients["nonni"]["called"] == 1:

    # Андрею не забрали
    if not clients["andrea"]["takeaway"]:

        scene bg call_nonni_sad
        play sound "call_answer.mp3" noloop

        if clients["nonni"]["wine_accepted"] and clients["nonni"]["wine_complete"]:

            n "Квист, ты бросил Андрею лежать неизвестно где."
            n "Не звони мне больше."
            n "И жалею, что вообще пила вино с таким козлом."

        elif clients["nonni"]["wine_accepted"]:

            n "Квист, ты бросил Андрею."
            n "Честно говоря, я даже не удивлена."
            n "Не звони мне больше."

        else:

            n "Квист, ты бросил Андрею."
            n "Не звони мне больше."

        $ clients["nonni"]["foreverbanned"] = True
        jump phone_menu

    # Андрею помогли
    else:

        scene bg call_nonni_sad
        play sound "call_answer.mp3" noloop

        # Аппарат уже сдан
        if not clients["nonni"]["order_active"]:

            if clients["nonni"]["repair_day"] == 1:

                if clients["nonni"]["wine_complete"]:
                    n "Спасибо, Квист."
                    n "После вчерашнего тем более."
                    n "Своим людям я помогу всем, чем смогу."
                else:
                    n "Спасибо, что помог с Андреей."
                    n "Своим людям я помогу всем, чем смогу."

            elif clients["nonni"]["repair_day"] == 2:

                n "Спасибо, что привёз Андрею."
                n "Я сделаю всё, что в моих силах."

        # Аппарат не готов
        elif clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:

            n "Андреа сейчас спит. Пока всё стабильно."
            n "Но аппарат нужен."
            n "Постарайся закончить его максимум завтра."

        # Аппарат готов
        elif clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:

            n "Аппарат готов?"

            menu:
                extend ""

                "Отдать бесплатно":

                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    n "Спасибо."
                    n "Это хорошая новость."

                "15 кредитов":

                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    n "Сейчас не время торговаться."
                    n "Но ладно."

                "20 кредитов":

                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    n "Не лучший момент поднимать цены."
                    n "Но сейчас не до этого."

        jump phone_menu

# ---------------- ВТОРОЙ ЗВОНОК ----------------

elif clients["nonni"]["called"] == 2:

    scene bg call_nonni_sad
    play sound "call_answer.mp3" noloop

    # Аппарат уже сдан
    if not clients["nonni"]["order_active"]:

        n "Квист, я всё помню."
        n "Если будешь звонить каждые пять минут, работать я не смогу."

        $ clients["nonni"]["banned"] = True
        jump phone_menu

    # Аппарат не готов
    elif not clients["nonni"]["order_completed"]:

        n "Как аппарат?"

        k "Не готов."

        n "Тогда зачем ты звонишь?"
        n "Я серьёзно, Квист."

        $ clients["nonni"]["banned"] = True
        jump phone_menu

    # Аппарат готов
    else:

        n "Это уже второй звонок."
        n "Я надеюсь, что аппарат наконец готов."

        menu:
            extend ""

            "Отдать бесплатно":

                $ clients["nonni"]["repair_price"] = 0
                $ clients["nonni"]["repair_day"] = current_day
                $ clients["nonni"]["order_active"] = False
                $ clients["andrea"]["nonni_delivered"] = True

                n "Ого."
                n "Второй звонок оказался не зря."
                n "Спасибо."

            "15 кредитов":

                $ clients["nonni"]["repair_price"] = 15
                $ clients["nonni"]["repair_day"] = current_day
                $ clients["nonni"]["order_active"] = False
                $ clients["andrea"]["nonni_delivered"] = True
                $ money += 15
                play sound "money.mp3" noloop
                "Вам зачислили 15 кредитов"
                n "Я уже начала думать, что ты звонишь просто поболтать."
                n "Ладно. Пятнадцать так пятнадцать."

            "20 кредитов":

                $ clients["nonni"]["repair_price"] = 20
                $ clients["nonni"]["repair_day"] = current_day
                $ clients["nonni"]["order_active"] = False
                $ clients["andrea"]["nonni_delivered"] = True
                $ money += 20
                play sound "money.mp3" noloop
                "Вам зачислили 20 кредитов"
                n "Андрея в больнице, а ты всё ещё пытаешься заработать."
                n "Впечатляет."

        jump phone_menu

# ---------------- ТРЕТИЙ ЗВОНОК ----------------

elif clients["nonni"]["called"] >= 3:

    scene bg call_nonni_sad
    play sound "call_answer.mp3" noloop

    # Аппарат уже сдан
    if not clients["nonni"]["order_active"]:

        n "Квист, зачем ты звонишь?"
        n "Я понимаю, что переживаешь."
        n "Но мне надо работать."

        $ clients["nonni"]["banned"] = True
        jump phone_menu

    # Аппарат не готов
    elif not clients["nonni"]["order_completed"]:

        n "Квист, ты издеваешься?"

        k "Пока нет."

        n "Тогда перестань звонить и начни работать."

        $ clients["nonni"]["banned"] = True
        jump phone_menu

    # Аппарат готов
    else:

        n "Третий звонок."
        n "Я очень надеюсь, что аппарат наконец готов."

        menu:
            extend ""

            "Отдать бесплатно":

                $ clients["nonni"]["repair_price"] = 0
                $ clients["nonni"]["repair_day"] = current_day
                $ clients["nonni"]["order_active"] = False

                n "Наконец-то."
                n "Спасибо."
                n "И пожалуйста, больше сегодня не звони."

            "15 кредитов":

                $ clients["nonni"]["repair_price"] = 15
                $ clients["nonni"]["repair_day"] = current_day
                $ clients["nonni"]["order_active"] = False
                $ money += 15
                play sound "money.mp3" noloop
                "Вам зачислили 15 кредитов"
                n "Третий звонок."
                n "Пятнадцать кредитов."
                n "Хотя бы аппарат готов."
                n "И пожалуйста, больше не звони."

            "20 кредитов":

                $ clients["nonni"]["repair_price"] = 20
                $ clients["nonni"]["repair_day"] = current_day
                $ clients["nonni"]["order_active"] = False
                $ money += 20
                play sound "money.mp3" noloop
                "Вам зачислили 20 кредитов"

                n "Третий звонок."
                n "Двадцать кредитов."
                n "Знаешь, сейчас я даже спорить не хочу."
                n "И пожалуйста, больше не звони."

        $ clients["nonni"]["banned"] = True
        jump phone_menu

