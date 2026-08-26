
label day1_call_nonni:
    if clients["nonni"]["called"] == 0:
        scene bg call_nonni
        play sound "call_answer.mp3" noloop
        $ clients["nonni"]["called"] += 1
        n "Как там мой аппарат? Пациенты уже ругаются."
        if clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:
            menu:
                extend ""
                "Пока не готов":
                    n "Звони, когда починишь, не отвлекай меня"
                "Готов, отдам бесплатно":
                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False   # исправлено: False
                    $ clients["andrea"]["nonni_delivered"] = True
                    n "Ты просто душка"
                "Готов, с тебя 15":
                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 15
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    n "Справедливо"
                "Готов 20$":
                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 12
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"

                    n "Ну ты и жук"
        else:
            k "Не готов"
            n "Звони, когда починишь, не отвлекай меня"        
    elif clients["nonni"]["called"] < 4:
        $ clients["nonni"]["called"] += 1
        if clients["nonni"]["order_active"] and clients["nonni"]["order_completed"]:
            scene bg call_nonni_sad
            play sound "call_answer.mp3" noloop
            n "Квист, я вообще-то работаю."
            n "Как аппарат?"
            menu:
                extend ""
                "Пока не готов":
                    n "Ты понимаешь, что я тут жизни спасаю, а ты с херней мне звонишь?!"
                "Готов, отдам бесплатно":
                    $ clients["nonni"]["repair_price"] = 0
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    n "Ты просто душка"
                "Готов, с тебя 15":
                    $ clients["nonni"]["repair_price"] = 15
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 15
                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"
                    n "Справедливо"
                "Готов 20":
                    $ clients["nonni"]["repair_price"] = 20
                    $ clients["nonni"]["repair_day"] = current_day
                    $ clients["nonni"]["order_active"] = False
                    $ clients["andrea"]["nonni_delivered"] = True
                    $ clients["andrea"]["cure_price"] -= 12
                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"
                    n "Ну ты и жук"
        elif clients["nonni"]["repair_day"] == 1:
            scene bg call_nonni_happy
            play sound "call_answer.mp3" noloop
            n "Не сегодня, душка"     
        else:
            scene bg call_nonni_sad
            play sound "call_answer.mp3" noloop
            n "Квист, я вообще-то работаю. Как аппарат?"
            k "Не готов еще"
            n "Ты придурок? Звонишь по несколько раз, чтобы мне об этом сказать?!" 
    else:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        n "..."
        "Нонни не отвечает."    
    jump phone_menu