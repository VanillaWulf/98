label day2_call_becker:
    # Увеличиваем счётчик звонков (если это не первый вызов, то called уже > 1)
    $ clients["bekker"]["called"] += 1

    # --- Блок проверки бана ---
    if clients["bekker"]["banned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        b "..."
        "Беккер не отвечает."
        jump phone_menu

    scene bg call_becker
    play sound "call_answer.mp3" noloop

    # --- Заказ деталей (только при первом звонке) ---
    if clients["bekker"]["called"] == 1:
        b "Квист, слушай. Завтра у меня будет поставка. Могу привезти детали. Провод или микросхема – по [clients['bekker']['base_price']]$ или оба по [clients['bekker']['base_price'] * 2]$. Что закажешь?"
        menu:
            extend ""
            "Заказать провод ([clients['bekker']['base_price']]$)":
                if money >= clients["bekker"]["base_price"]:
                    $ money -= clients["bekker"]["base_price"]
                    play sound "money_send.mp3" noloop
                    "Вы отправили кредиты - [clients['bekker']['base_price']] штук"
                    $ clients["bekker"]["ordered_part"] = "wire"
                    b "Привезу завтра."
                else:
                    b "Денег не хватает. Не заказывай, если платить нечем и не звони мне больше."
                    $ clients["bekker"]["banned"] = True
                    k "Ладно, завтра уже отойдет"
                    jump phone_menu
            "Заказать микросхему ([clients['bekker']['base_price']]$)":
                if money >= clients["bekker"]["base_price"]:
                    $ money -= clients["bekker"]["base_price"]
                    play sound "money_send.mp3" noloop
                    "Вы отправили кредиты - [clients['bekker']['base_price']] штук"
                    $ clients["bekker"]["ordered_part"] = "chip"
                    b "Привезу завтра."
                else:
                    b "Денег не хватает. Не звони мне сегодня, козел, я к тебе со всей душой"
                    $ clients["bekker"]["banned"] = True
                    k "Ладно, завтра уже отойдет"
                    jump phone_menu
            "Заказать оба ([clients['bekker']['base_price'] * 2]$)":
                if money >= clients["bekker"]["base_price"] * 2:
                    $ money -= clients["bekker"]["base_price"] * 2
                    $ clients["bekker"]["ordered_part"] = "both"
                    play sound "money_send.mp3" noloop
                    "Вы отправили кредиты - [clients['bekker']['base_price']] штук"
                    b "Привезу завтра."
                else:
                    b "Денег не хватает. Не звони мне сегодня, козел, я к тебе со всей душой"
                    $ clients["bekker"]["banned"] = True
                    k "Ладно, завтра уже отойдет"
                    jump phone_menu
            "Ничего не заказывать":
                b "Как знаешь. Два раза предлагать не стану"

    # --- Проверка статуса ремонта модуля (после заказа или при повторных звонках) ---
    if clients["bekker"]["order_completed"] and clients["bekker"]["order_active"]:
        # Модуль готов, но ещё не сдан
        if clients["bekker"]["called"] < 3:
            b "Кстати, модуль самоката готов? Мне надоело ходить пешком, завтра у меня ответственный день, надо всё успеть."
            menu:
                extend ""
                "Пока не готов":
                    if clients["bekker"]["called"] == 1:
                        b "Ну давай быстрее. Ну"
                        $ clients["bekker"]["banned"] = True
                    else:
                        b "Полу, знаешь, может быть интересно про твои полусерые заказы."
                        $ clients["bekker"]["banned"] = True
                "Готов, отдам бесплатно":
                    $ clients["bekker"]["repair_price"] = 0
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    b "Наконец-то. Ладно, проехали. До завтра"
                    $ clients["bekker"]["base_price"] -=4
                    $ clients["bekker"]["banned"] = True
                "Готов, с тебя 15 кредитов":
                    $ clients["bekker"]["repair_price"] = 15
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    $ clients["bekker"]["banned"] = True
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    $ money += 15
                    $ clients["bekker"]["base_price"] -=2
                    b "Справедливо. До завтра, если повезет"
                "Готов, с тебя 20 кредитов":
                    $ clients["bekker"]["repair_price"] = 20
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    $ clients["bekker"]["banned"] = True
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    $ money += 20
                    $ clients["bekker"]["base_price"] -=1
                    b "Начинаю понимать, почему ты дружишь с Микко. До завтра, если повезет"
        else:
            b "Квист, мне надоело, делай уже мой модуль"
            $ clients["bekker"]["banned"] = True
        jump phone_menu
    
    # Заказ активен и не сделан - тест
    if not clients["bekker"]["order_completed"] and clients["bekker"]["order_active"]:
        if clients["bekker"]["called"] < 3:
            b "Как там модуль?"
            k "Делается"
            b "Лучше бы ему сделаться"
        elif clients["bekker"]["called"] == 3:
            b "Ты сначала сделай, потом звони"
            $ clients["bekker"]["banned"] = True

    # Заказ сделан и не активен (сдан) 
    elif clients["bekker"]["order_completed"] and not clients["bekker"]["order_active"] and not clients["bekker"]["banned"]:
        # Модуль готов и сдан
        if clients["bekker"]["called"] < 3:
            b "Ты уже звонил, а толку нет."
            $ clients["bekker"]["banned"] = True


    jump phone_menu