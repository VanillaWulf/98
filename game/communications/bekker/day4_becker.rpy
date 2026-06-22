label day4_call_becker:
    # Увеличиваем счётчик звонков
    $ clients["bekker"]["called"] += 1

    # --- Блок проверки бана ---
    if clients["bekker"]["banned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        b "..."
        "Беккер не отвечает."
        jump phone_menu

    # --- Проверка перманентного бана ---
    if clients["bekker"]["foreverbanned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        b "..."
        "Беккер больше никогда не отвечает."
        k "Ну я и кретин, довел его"
        jump phone_menu

    scene bg call_becker
    play sound "call_answer.mp3" noloop

    # ========== ПЕРВЫЙ ЗВОНОК ==========
    if clients["bekker"]["called"] == 1:
        # заказ деталей
             # --- Заказ деталей (отдельный блок, если нет активного заказа или заказ уже сдан) ---
        b "Квист, поставки завтра нет"

        # Случай: заказ активен и выполнен (можно сдать квест)
        if clients["bekker"]["order_active"] and clients["bekker"]["order_completed"]:
            b "Кстати, модуль самоката готов? Мне надоело ходить пешком, у меня ответственный вечер, надо всё успеть."
            menu:
                extend ""
                "Пока не готов":
                    b "Давай торопись, мне нужно это сегодня."
                "Готов, отдам бесплатно":
                    play sound "order.mp3" noloop
                    $ clients["bekker"]["repair_price"] = 0
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    b "Наконец-то. Ладно, проехали."
                   
                "Готов, с тебя 15$":
                    play sound "order.mp3" noloop
                    $ clients["bekker"]["repair_price"] = 15
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    b "Справедливо."

                "Готов, 20$":
                    play sound "order.mp3" noloop
                    $ clients["bekker"]["repair_price"] = 20
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    b "Начинаю понимать, почему ты дружишь с Микко."
            jump phone_menu

        # Случай: заказ активен и не выполнен
        elif clients["bekker"]["order_active"] and not clients["bekker"]["order_completed"]:
            b "Как там модуль?"
            k "Делается."
            b "Давай торопись."
            jump phone_menu

        else: 
            b "Еще раз спасибо за модуль"
            jump phone_menu

    # ========== ВТОРОЙ ЗВОНОК ==========
    elif clients["bekker"]["called"] == 2:
    
        # Случай: заказ активен и выполнен (можно сдать)
        if clients["bekker"]["order_active"] and clients["bekker"]["order_completed"]:
            b "Ну что там с моим модулем? Ты обещал сделать."
            menu:
                extend ""
                "Пока не готов":
                    b "Ты меня троллишь? Больше не звони мне никогда. Про детали можешь забыть, деньги не верну"
                    $ clients["bekker"]["ordered_part"] = None
                    $ clients["bekker"]["foreverbanned"] = True
                "Готов, отдам бесплатно":
                    play sound "order.mp3" noloop
                    $ clients["bekker"]["repair_price"] = 0
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    b "Наконец-то. Ладно, проехали. Мне некогда"
                    $ clients["bekker"]["banned"] = True
                "Готов, с тебя 15":
                    play sound "order.mp3" noloop
                    $ clients["bekker"]["repair_price"] = 15
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    b "Справедливо. некогда"
                    $ clients["bekker"]["banned"] = True
                "Готов, 20":
                    play sound "order.mp3" noloop
                    $ clients["bekker"]["repair_price"] = 20
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    b "Начинаю понимать, почему ты дружишь с Микко. некогда"
                    $ clients["bekker"]["banned"] = True
            jump phone_menu     

        # Случай: заказ активен и не выполнен
        elif clients["bekker"]["order_active"] and not clients["bekker"]["order_completed"]:
            b "Ты чего звонишь, если модуль не готов"
            $ clients["bekker"]["banned"] = True
            jump phone_menu
      
        # Сдан в первом звонке
        else:
            b "Еще раз спасибо за модуль, мне пора"
            $ clients["bekker"]["banned"] = True
            jump phone_menu

    jump phone_menu