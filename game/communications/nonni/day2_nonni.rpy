label day2_call_nonni:
    # Если клиент в бане — не отвечает
    if clients["nonni"]["banned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        n "..."
        "Нонни не отвечает."
        jump phone_menu

    # Увеличиваем счётчик звонков (без ограничения)
    $ clients["nonni"]["called"] += 1

    # ----- ПЕРВЫЙ ЗВОНОК -----
    if clients["nonni"]["called"] == 1:
        # Случай: заказ сдан в первый день (order_active == False и repair_day == 1)
        if not clients["nonni"]["order_active"] and clients["nonni"]["repair_day"] == 1:
            if clients["nonni"]["repair_price"] == 0:
                scene bg call_nonni_happy
                play sound "call_answer.mp3" noloop
                n "Квист, спасибо за аппарат. Пациенты довольны."
                n "Слушай, может, хочешь зайду сегодня вечером? У меня есть бутылочка вина, отметим."
                menu:
                    extend ""
                    "Согласиться":
                        $ clients["nonni"]["wine_accepted"] = True
                        n "Отлично. Приду после заката."
                    "Отказаться":
                        $ clients["nonni"]["banned"] = True
                        n "Ну как хочешь. Тогда в другой раз."
            elif clients["nonni"]["repair_price"] == 15:
                scene bg call_nonni_happy
                play sound "call_answer.mp3" noloop
                n "Квист, аппарат работает, спасибо."
                n "Хотела пригласить тебя на вино, но ты у меня все выгреб. Может, ты угостишь? Ты же теперь можешь себе позволить - всего 5 кредитов."
                menu:
                    extend ""
                    "Согласиться угостить":
                        $ money -= 5
                        play sound "money_send.mp3" noloop
                        "Вы отправили кредиты - 5 штук"
                        $ clients["nonni"]["wine_accepted"] = True
                        n "Вот и славно. Вечером приду."
                    "Отказаться":
                        $ clients["nonni"]["banned"] = True
                        n "Жаль. Ну ладно."
            else:  # repair_price == 20
                scene bg call_nonni
                play sound "call_answer.mp3" noloop
                n "Аппарат работает. Спасибо, но сейчас мне некогда."
                $ clients["nonni"]["banned"] = True
            jump phone_menu

        # Случай: заказ активен и выполнен (можно сдать)
        elif clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:
            scene bg call_nonni
            play sound "call_answer.mp3" noloop
            n "Как продвигается ремонт, Квист? Уже целых 2 дня прошло"
            menu:
                extend ""
                "Пока не готов":
                    n "Звони, когда починишь, не отвлекай меня."
                "Готов, отдам бесплатно":
                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    n "Медленней, чем я думала, но огромное спасибо за щедрость."
                "Готов, с тебя 15":
                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    n "Медленней, чем я думала."
                "Готов, 20":
                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    n "Медленней, чем я думала. И дорого, Квист!"
            jump phone_menu

        # Случай: заказ активен, но не выполнен
        elif clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:
            scene bg call_nonni_sad
            play sound "call_answer.mp3" noloop
            n "Давай быстрее с аппаратом!"
            jump phone_menu

        # Иначе (например, заказ уже сдан, но не в первый день?) — не отвечает
        # else:
        #     scene bg call_no_answer
        #     play sound "call_no_answer.mp3" noloop
        #     n "..."
        #     "Нонни не отвечает."
        #     jump phone_menu

    # ----- ВТОРОЙ ЗВОНОК -----
    elif clients["nonni"]["called"] == 2:
        # Если принято приглашение на вино
        if clients["nonni"]["wine_accepted"] == True: 
            scene bg call_nonni_happy
            play sound "call_answer.mp3" noloop
            n "Квист, не торопи события. Жди вечером, я не заставлю ждать."
            jump phone_menu

        # Если заказ активен и выполнен — нервная сдача
        if clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:
            scene bg call_nonni_sad
            play sound "call_answer.mp3" noloop
            n "Ну что там с моим аппаратом? Второй то раз позвонил с хорошими новостями?"
            menu:
                extend ""
                "Пока не готов":
                    n "Ты совсем сдурел звонить и говорит, что он не сделан?"
                "Готов, отдам бесплатно":
                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 12
                    n "Этот звонок мне нравится больше, чем предыдущий! Огромное спасибо за щедрость, хоть и медленно. Все, мне пора"
                    $ clients["nonni"]["banned"] = True
                "Готов, с тебя 15":
                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 9
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    n "Этот звонок мне нравится больше, чем предыдущий! Хотя и медленней, чем я думала. Мне пора"
                    $ clients["nonni"]["banned"] = True
                "Готов, 20":
                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 10
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    n "Этот звонок мне нравится больше, чем предыдущий, хотя цены у тебя высокие, мне пора по делам"
                    $ clients["nonni"]["banned"] = True
            jump phone_menu

        # Если заказ активен и не выполнен — бан с упрёком
        elif clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:
            scene bg call_nonni_sad
            play sound "call_answer.mp3" noloop
            n "Не отвлекайся на звонки, а делай!"
            $ clients["nonni"]["banned"] = True
            jump phone_menu

        elif not clients["nonni"]["order_active"]:
            scene bg call_nonni
            play sound "call_answer.mp3" noloop
            n "Cпасибо за ремонт, сегодня у меня нет времени дальше говорить, пока"
            $ clients["nonni"]["banned"] = True
            jump phone_menu


        # Любая другая ситуация (например, заказ уже сдан без вина — но там уже должен быть бан)
        # scene bg call_no_answer
        # play sound "call_no_answer.mp3" noloop
        # n "..."
        # "Нонни не отвечает."
        # jump phone_menu

    # ----- ТРЕТИЙ ЗВОНОК -----
    elif clients["nonni"]["called"] == 3:
        # Если принято приглашение на вино — ругается и банит
        if clients["nonni"]["wine_accepted"] == True:
            scene bg call_nonni_happy
            play sound "call_answer.mp3" noloop
            n "Уже скоро. Не звони каждые пять минут."
            $ clients["nonni"]["banned"] = True
            jump phone_menu

        # Если заказ активен и выполнен — нервная сдача
        if clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:
            scene bg call_nonni_sad
            play sound "call_answer.mp3" noloop
            n "Ну что там с моим аппаратом? Который раз позвонил, надеюсь, с хорошими новостями?"
            menu:
                extend ""
                "Пока не готов":
                    n "Ты меня достал, Квист!"
                    $ clients["nonni"]["banned"] = True
                "Готов, отдам бесплатно":
                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 12
                    n "Этот звонок мне нравится больше, чем предыдущий! Огромное спасибо за щедрость, хоть и медленно. Все, мне пора"
                    $ clients["nonni"]["banned"] = True
                "Готов, с тебя 15":
                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 9
                    $ money += 15
                    n "Этот звонок мне нравится больше, чем предыдущий! Не отвлекая меня"
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    $ clients["nonni"]["banned"] = True
                "Готов, 20":
                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 10
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    n "Цены у тебя высокие, но спасибо, мне пора"
                    $ clients["nonni"]["banned"] = True
            jump phone_menu
