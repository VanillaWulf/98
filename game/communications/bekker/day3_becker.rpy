label day3_call_becker:
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
        b "Квист, слушай. Завтра у меня будет поставка. Могу привезти детали. Провод или микросхема – по [clients['bekker']['base_price']]$ или оба. Что закажешь?"
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
                    b "Денег не хватает. Не заказывай, если платить нечем."
            "Заказать микросхему ([clients['bekker']['base_price']]$)":
                if money >= clients["bekker"]["base_price"]:
                    $ money -= clients["bekker"]["base_price"]
                    play sound "money_send.mp3" noloop
                    "Вы отправили кредиты - [clients['bekker']['base_price']] штук"
                    $ clients["bekker"]["ordered_part"] = "chip"
                    b "Привезу завтра."
                else:
                    b "Денег не хватает. Я к тебе со всей душой."
            "Заказать оба ([clients['bekker']['base_price'] * 2]$)":
                if money >= clients["bekker"]["base_price"] * 2:
                    $ money -= clients["bekker"]["base_price"] * 2
                    play sound "money_send.mp3" noloop
                    "Вы отправили кредиты - [clients['bekker']['base_price']]*2 штук"
                    $ clients["bekker"]["ordered_part"] = "both"
                    b "Привезу завтра."
                else:
                    b "Денег не хватает. Как обычно, Квист."
            "Ничего не заказывать":
                b "Как знаешь. Два раза предлагать не стану."

        # Случай: заказ сдан во второй день (repair_day == 2, order_active == False)
        if not clients["bekker"]["order_active"]:
            if clients["bekker"]["repair_price"] == 0 or clients["bekker"]["repair_price"] == 15 and money > 10:
                # Поможет с Андреей за 10 долларов
                b "Квист, спасибо за ремонт."
                b "Слушай, я слышал про Андрею, могу ее подвезти на обратном пути? За 10 кредитов."
                menu:
                    extend ""
                    "Согласиться за 10$":
                        $ money -= 10
                        play sound "money_send.mp3" noloop
                        "Вы отправили кредиты - 10 штук"
                        b "Все сделаем"
                    "Отказаться":
                        b "Ну и ладно."
            elif clients["bekker"]["repair_price"] == 20 and money > 15:
                # Поможет с Андреей за 15 долларов
                b "Квист, спасибо за ремонт."
                b "Слушай, я слышал про Андрею, могу ее подвезти на обратном пути? За 15 кредитов."
                menu:
                    extend ""
                    "Согласиться за 15$":
                        $ money -= 15
                        play sound "money_send.mp3" noloop
                        "Вы отправили кредиты - 15 штук"
                        b "Все сделаем"
                    "Отказаться":
                        b "Ну ладно."

        # Случай: заказ активен и выполнен (можно сдать квест)
        elif clients["bekker"]["order_active"] and clients["bekker"]["order_completed"]:
            b "Кстати, модуль самоката готов? Мне надоело ходить пешком, у меня ответственный вечер, надо всё успеть."
            menu:
                extend ""
                "Пока не готов":
                    b "Давай торопись, мне нужно это сегодня."
                "Готов, отдам бесплатно":
                    $ clients["bekker"]["repair_price"] = 0
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    b "Наконец-то. Ладно, проехали."
                    b "Квист, спасибо за ремонт."
                    b "Слушай, я слышал про Андрею, могу ее подвезти на обратном пути? За 10 кредитов."
                    menu:
                        extend ""
                        "Согласиться за 10$":
                            $ money -= 10
                            play sound "money_send.mp3" noloop
                            "Вы отправили кредиты - 10 штук"
                            b "Все сделаем"
                        "Отказаться":
                            b "Странный ты"
                "Готов, с тебя 15$":
                    $ clients["bekker"]["repair_price"] = 15
                    $ clients["bekker"]["order_active"] = False
                    $ clients["bekker"]["repair_day"] = current_day
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"        
                      # Поможет с Андреей за 15 долларов
                    b "Справедливо."
                    b "Слушай, я слышал про Андрею, могу ее подвезти на обратном пути? За 15 кредитов."
                    menu:
                        extend ""
                        "Согласиться за 15$":
                            $ money -= 15
                            play sound "money_send.mp3" noloop
                            "Вы отправили кредиты - 15 штук"
                            b "Сработал в ноль, Квист"
                        "Отказаться":
                            b "Ну ладно."
                "Готов, 20$":
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
            b "Давай торопись, мне нужно это сегодня."
            jump phone_menu

        else: 
            b "Еще раз спасибо за модуль"
            jump phone_menu

    # ========== ВТОРОЙ ЗВОНОК ==========
    elif clients["bekker"]["called"] == 2:
        # Андреа забрать
        # if clients["bekker"]["repair_price"] == 0 or clients["bekker"]["repair_price"] == 15 and money > 14:
        #         # Поможет с Андреей за 10 долларов
        #         b "Квист, спасибо за ремонт."
        #         b "Слушай, я слышал про Андрею, могу ее подвезти обратном пути? За 10 кредитов."
        #         menu:
        #             extend ""
        #             "Согласиться за 10 кредитов":
        #                 $ money -= 10
        #                 b "Все сделаем"
        #             "Отказаться":
        #                 b "Ну и ладно."
        #     elif clients["bekker"]["repair_price"] == 20:
        #         # Поможет с Андреей за 15 долларов
        #         b "Квист, спасибо за ремонт."
        #         b "Слушай, я слышал про Андрею, могу ее подвезти обратном пути? За 15 кредитов."
        #         menu:
        #             extend ""
        #             "Согласиться за 15$":
        #                 $ money -= 15
        #                 b "Все сделаем"
        #             "Отказаться":
        #                 b "Ну ладно."    
                        
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
                    b "Справедливо. Некогда."
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
            b "Ты чего звонишь, если модуль не готов? Я ушел по делам... Возможно, встречу Пола по дороге"
            b "Он только корчит из себя приличного, но лишними деньгами не побрезгует."
            $ clients["bekker"]["banned"] = True
            jump phone_menu
      
        # Сдан в первом звонке
        else:
            b "Еще раз спасибо за модуль, мне пора"
            $ clients["bekker"]["banned"] = True
            jump phone_menu

    jump phone_menu