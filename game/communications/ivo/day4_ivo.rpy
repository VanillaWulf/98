label day4_ivo_talk:
    scene bg ivo
    i "Готово?"
    $ clients["ivo"]["called"] += 1

    menu:
        extend ""
        "Не сегодня":
            k "Не сегодня."
            i "Ладно. Куплю по дороге домой новый"
            $ clients["ivo"]["banned"] = True
            jump evening_menu
        
        # первый визит
        # заказ не готов
        "Подожди еще немного" if clients["ivo"]["order_active"] and not clients["ivo"]["order_completed"] and clients["ivo"]["called"] == 1:
            k "Подожди еще немного."
            if clients["ivo"]["called"] == 2:
                "Я наверно пойду, куплю новый по дороге домой - это будет даже быстрее"
                $ clients["ivo"]["banned"] = True
                jump evening_menu
            else:
                i "Ладно."
                jump evening_menu
        
        # -----------------------------------
        # Заказ готов
        # -----------------------------------
        "Работаю вот над твоим браслетом, почти готов" if clients["ivo"]["order_active"] and clients["ivo"]["order_completed"]:
            i "Отлично."
            menu:
                extend ""
                "Пока не готов":
                    if clients["ivo"]["called"] < 3:
                        i "Ладно. Куплю по дороге домой новый - так будет быстрее чем ждать."
                        $ clients["bekker"]["banned"] = True
                    else:
                        i "М?"

                "Готов, отдам бесплатно":
                    k "Забирай."
                    $ clients["ivo"]["repair_price"] = 0
                    $ clients["ivo"]["repair_day"] = current_day
                    $ clients["ivo"]["order_active"] = False
                    i "Спасибо."
                    $ clients["pol"]["hacked"] = True
                    if not clients["andrea"]["nonni_delivered"]:
                        i "Если хочешь, могу отвезти аппарат Андрее."
                        menu:
                            extend ""
                            "Да":
                                i "Без проблем. Одна нога тут, другая там."
                                $ clients["andrea"]["nonni_delivered"] = True
                            "Не надо":
                                i "Ладно."
                    else: 
                        i "Я хочу тебя отблагодарить, Квист, я все равно себе могу это позволить"  
                        $ money += 25   
                        play sound "money.mp3" noloop
                        "Вам зачислили 25 кредитов"      
                    $ clients["bekker"]["banned"] = True

                "Готов, с тебя 15 кредитов":
                    k "Пятнадцать кредитов. Ладно."
                    $ clients["ivo"]["repair_price"] = 15
                    $ clients["ivo"]["repair_day"] = current_day
                    $ clients["ivo"]["order_active"] = False
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    if not clients["andrea"]["nonni_delivered"]:
                        i "Могу заодно отвезти аппарат Нонни."
                        menu:
                            extend ""
                            "Отвезти":
                                $ clients["andrea"]["nonni_delivered"] = True
                            "Не надо":
                                i "Хорошо."
                    else: 
                        i "Давай насыпим немного за скорость"  
                        $ money += 7
                        play sound "money.mp3" noloop
                        "Вам зачислили 7 кредитов"
                    $ clients["ivo"]["banned"] = True

                "Готов, 20 кредитов":
                    $ clients["ivo"]["repair_price"] = 20
                    $ clients["ivo"]["repair_day"] = current_day
                    $ clients["ivo"]["order_active"] = False
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    i "Хм. Спасибо"
                    $ clients["ivo"]["banned"] = True

            jump evening_menu