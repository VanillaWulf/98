# label day4_call_nonni:

#   # Вечный бан
#   if clients["nonni"]["foreverbanned"]:
#       scene bg call_no_answer
#       play sound "call_no_answer.mp3" noloop
#       n "..."
#       "Нонни не отвечает."
#       k "Я забыл, что ее окончательно достал"
#       jump phone_menu

#   # Обычный бан
#   if clients["nonni"]["banned"]:
#       scene bg call_no_answer
#       play sound "call_no_answer.mp3" noloop
#       n "..."
#       "Нонни не отвечает."
#       jump phone_menu

#   $ clients["nonni"]["called"] += 1

#   # ===================================
#   # ПЕРВЫЙ ЗВОНОК
#   # ===================================

#   if clients["nonni"]["called"] == 1:

#       scene bg call_nonni_sad
#       play sound "call_answer.mp3" noloop

#       # Аппарат не сделан

#       if clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:

#           n "Квист, ты совсем идиот? Я же сказала, что Андрее стало хуже. Хватит трепаться по телефону."
#           $ clients["nonni"]["banned"] = True

#           jump phone_menu

#       # Аппарат сделан, но не сдан

#       elif clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:

#           n "Аппарат готов?"

#           menu:
#               extend ""

#               "Отдать бесплатно":

#                   $ clients["nonni"]["repair_price"] = 0
#                   $ clients["nonni"]["repair_day"] = current_day
#                   $ clients["nonni"]["order_active"] = False
#                   $ clients["nonni"]["banned"] = True
#                   n "Спасибо. Сегодя ты все сделал правильно. Вези его скорее ко мне!"

#               "15 кредитов":

#                   $ clients["nonni"]["repair_price"] = 15
#                   $ clients["nonni"]["repair_day"] = current_day
#                   $ clients["nonni"]["order_active"] = False
#                   $ money += 15
#                   $ clients["nonni"]["banned"] = True
#                   n "Сейчас? Ты решил торговаться сейчас? Ладно. Вези его скорее ко мне!"

#               "20 кредитов":

#                   $ clients["nonni"]["repair_price"] = 20
#                   $ clients["nonni"]["repair_day"] = current_day
#                   $ clients["nonni"]["order_active"] = False
#                   $ money += 20
#                   $ clients["nonni"]["banned"] = True
#                   n "Двадцать кредитов?"

#                   n "Когда твоя пациентка лежит без аппарата? Знаешь что, Квист... Забирай, придурок, только привези его срочно"

#           jump phone_menu

#       # Аппарат уже сдан

#       else:

#           n "Я делаю всё, что могу."

#           # Вино + забрал Андрею сам
#           if (
#               clients["nonni"]["wine_accepted"]
#               and clients["nonni"]["wine_complete"]
#               and clients["andrea"]["takeaway"]
#           ):

#               n "Слышишь? Не накручивай себя раньше времени. Она сильная."
#               n "И ты тоже. Я позвоню сразу, если что-нибудь изменится."
#               $ clients["nonni"]["banned"] = True

#           # Приглашение было, но вина не было
#           elif (
#               clients["nonni"]["wine_accepted"]
#               and clients["andrea"]["takeaway"]
#           ):

#               n "Я понимаю, что ты переживаешь. Но сейчас лучше дай мне работать. Если что-то изменится, я сама позвоню."
#               $ clients["nonni"]["banned"] = True

#           else:

#               n "Я разберусь. Не мешай мне работать. Если будут новости, я сама позвоню."

#               $ clients["nonni"]["banned"] = True

#           jump phone_menu

#   # ===================================
#   # ВТОРОЙ ЗВОНОК
#   # ===================================

#   elif clients["nonni"]["called"] >= 2:

#       scene bg call_nonni_angry
#       play sound "call_answer.mp3" noloop

#       # Можно сдать аппарат

#       if clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:

#           n "Это уже второй звонок. Надеюсь, ты наконец решил не тянуть время, как Аппарат?"

#           menu:
#         extend ""

#         "Отдать бесплатно":

#                 $ clients["nonni"]["repair_price"] = 0
#                 $ clients["nonni"]["repair_day"] = current_day
#                 $ clients["nonni"]["order_active"] = False

#                 n "Спасибо. Наконец-то. Со второго раза, но все равно правильное решение, вези его"

#         "Готов, 15 кредитов":

#                 $ clients["nonni"]["repair_price"] = 15
#                 $ clients["nonni"]["repair_day"] = current_day
#                 $ clients["nonni"]["order_active"] = False
#                 $ money += 15

#                 n "Даже сейчас ты пытаешься заработать. Потрясающе. Привези его"

#         "Готов, 20 кредитов":

#                 $ clients["nonni"]["repair_price"] = 20
#                 $ clients["nonni"]["repair_day"] = current_day
#                 $ clients["nonni"]["order_active"] = False
#                 $ money += 20

#                 n "Двадцать кредитов. ААААААААА! ВЕЗИ ЕГО"
#           $ clients["nonni"]["banned"] = True

#           jump phone_menu

#       else:

#           n "Квист. Либо работай. Либо не отвлекай меня."

#           $ clients["nonni"]["banned"] = True

#           jump phone_menu


# label day4_nonni_move:
#   $ actions -= 1
#   $ clients["andrea"]["nonni_delivered"] = True
#   "отвезли аппарарат"    
#   jump day5_start

label day4_call_nonni:
    # Вечный бан
    if clients["nonni"]["foreverbanned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        n "..."
        "Нонни не отвечает."
        k "Я забыл, что ее окончательно достал"
        jump phone_menu

    # Обычный бан
    if clients["nonni"]["banned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        n "..."
        "Нонни не отвечает."
        jump phone_menu

    $ clients["nonni"]["called"] += 1

    # ===================================
    # ПЕРВЫЙ ЗВОНОК
    # ===================================

    if clients["nonni"]["called"] == 1:
        scene bg call_nonni_sad
        play sound "call_answer.mp3" noloop

        # Аппарат не сделан
        if clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:
            n "Квист, ты совсем идиот? Я же сказала, что Андрее стало хуже. Хватит трепаться по телефону."
            $ clients["nonni"]["banned"] = True
            jump phone_menu

        # Аппарат сделан, но не сдан
        elif clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:
            n "Аппарат готов?"

            menu:
                "Отдать бесплатно":
                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["nonni"]["banned"] = True
                    n "Спасибо. Сегодня ты все сделал правильно. Вези его скорее ко мне!"

                "15 кредитов":
                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ money += 15
                    $ clients["nonni"]["banned"] = True
                    n "Сейчас? Ты решил торговаться сейчас? Ладно. Вези его скорее ко мне!"

                "20 кредитов":
                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ money += 20
                    $ clients["nonni"]["banned"] = True
                    n "Двадцать кредитов?"
                    n "Когда твоя пациентка лежит без аппарата? Знаешь что, Квист... Забирай, придурок, только привези его срочно"

            jump phone_menu

        # Аппарат уже сдан
        else:
            n "Я делаю всё, что могу."

            # Вино + забрал Андрею сам
            if (
                clients["nonni"]["wine_accepted"]
                and clients["nonni"]["wine_complete"]
                and clients["andrea"]["takeaway"]
            ):
                n "Слышишь? Не накручивай себя раньше времени. Она сильная."
                n "И ты тоже. Я позвоню сразу, если что-нибудь изменится."
                $ clients["nonni"]["banned"] = True

            # Приглашение было, но вина не было
            elif (
                clients["nonni"]["wine_accepted"]
                and clients["andrea"]["takeaway"]
            ):
                n "Я понимаю, что ты переживаешь. Но сейчас лучше дай мне работать. Если что-то изменится, я сама позвоню."
                $ clients["nonni"]["banned"] = True

            else:
                n "Я разберусь. Не мешай мне работать. Если будут новости, я сама позвоню."
                $ clients["nonni"]["banned"] = True

            jump phone_menu

    # ===================================
    # ВТОРОЙ ЗВОНОК
    # ===================================

    elif clients["nonni"]["called"] == 2:
        scene bg call_nonni_angry
        play sound "call_answer.mp3" noloop

        # Можно сдать аппарат
        if clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:
            n "Это уже второй звонок. Надеюсь, ты наконец решил не тянуть время, как Аппарат?"

            menu:
                "Отдать бесплатно":
                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    n "Спасибо. Наконец-то. Со второго раза, но все равно правильное решение, вези его"

                "Готов, 15 кредитов":
                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ money += 5
                    play sound "money.mp3" noloop
                    "Вам зачислили 5 кредитов"
                    n "Даже сейчас ты пытаешься заработать. Я за такое гавно вообще платить не должна"

                "Готов, 20 кредитов":
                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    n "Двадцать кредитов. Ты вообще охренел? Вези его, и молись, чтобы я тебя не прибила"

            $ clients["nonni"]["banned"] = True
            jump phone_menu

        else:
            n "Квист. Либо работай. Либо не отвлекай меня."
            $ clients["nonni"]["banned"] = True
            jump phone_menu


label day4_nonni_move:
    $ actions -= 1
    $ clients["andrea"]["nonni_delivered"] = True
    "Отвезли аппарат."
    jump day5_start