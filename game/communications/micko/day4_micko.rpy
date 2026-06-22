label day4_call_mikko:
    $ clients["mikko"]["is_called"] = True
    
    # Если не помогал Микко скрыться
    if not clients["mikko"]["hangouts_day_3"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        m "..."
        "Микко не отвечает."
        jump phone_menu
    
    # Если уже забанил
    if clients["mikko"]["banned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        m "..."
        "Микко не отвечает."
        jump phone_menu
    
    $ clients["mikko"]["called"] += 1
    
    # ==========================
    # ПЕРВЫЙ ЗВОНОК
    # ==========================

    if clients["mikko"]["hangouts_day_2"]:
        scene bg call_mikko
    else: 
        scene bg call_mikko_sad
        
    if clients["mikko"]["called"] == 1:
        play sound "call_answer.mp3" noloop
        m "Квист. Спасибо."
        k "За что?"
        m "За вчера."
        m "Без тебя я бы сейчас не знаю, где бы был"
        
        # Аппарат Нонни не сделан
        if clients["nonni"]["order_active"] and not clients["nonni"]["order_completed"]:
            m "Кстати. Я слышал про Андрею. Если совсем прижмёт, могу достать похожий аппарат."
            m "Прадва придется отдать пятнадцать кредитов и нужно будет сгонять за ним со мной"
        
        # Аппарат сделан, но не сдан
        elif clients["nonni"]["order_active"] and clients["nonni"]["order_completed"] and not clients["andrea"]["nonni_delivered"]:
            m "Кстати."
            m "Если аппарат уже готов, могу помочь его быстро довезти."
            m "Я сейчас как раз стараюсь не сидеть на одном месте."
            $ clients["andrea"]["nonni_delivered"] = True
        
        # Аппарат уже сдан - переделать в тусовку с ним - сначала даст 5 кредитов, но потом сможет еще накинуть
        else:
            m "Слышал, что аппарат уже у Нонни."
            m "Хорошо."
            m "На лекартва? Давай подзаработаем на них. Приезжай ко мне расскажу"
            m "Держи. У меня еще дома есть флешка с кредитами, заскочешь отдам за так"
            $ money += 5
            play sound "money.mp3" noloop
            "Вам зачислили 5 кредитов"
            m "Немного, но сейчас пригодится."
        
        m "Ладно. Мне пора."
        $ clients["mikko"]["banned"] = True
        jump phone_menu
    
    # ==========================
    # ПОСЛЕДУЮЩИЕ ЗВОНКИ
    # ==========================
    else:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        m "..."
        "Микко не отвечает."
        jump phone_menu

label day4_hangout_mikko:
    if clients["mikko"]["hangouts_day_3"]:
        if clients["andrea"]["nonni_delivered"]:
            "Заскочил к Микко отдал флешку"
            $ money += 10
            play sound "money.mp3" noloop
            "Вам зачислили 10 кредитов"
            jump day5_start
        elif money < 15:
        
            if clients["mikko"]["hangouts_day_2"]:
                scene bg call_mikko
            else: 
                scene bg call_mikko_sad

            play sound "call_answer.mp3" noloop
            m "Без 15 кредитов никак, на что аппарат купим."
        else:
            scene bg city
            "Вечером вы вместе с Микко отправились за аппаратом через половину Старого Центра."

            "Нужный человек жил в старом складском помещении и почему-то держал медицинское оборудование рядом с коллекцией сломанных игровых автоматов."

            "Пока Микко торговался, продавец успел трижды передумать насчёт цены и дважды предложить купить что-нибудь ещё."

            "В конце концов сделка состоялась, аппарат погрузили на тележку и поспешили уехать, пока никто не передумал снова."

            "По дороге обратно Микко выглядел заметно спокойнее, чем в последние дни."

            "Похоже, впервые за долгое время всё прошло почти по плану."

            $ actions -= 1
            $ money -= 15
            play sound "money_send.mp3" noloop
            "Вы отправили кредиты - 15 штук"
            $ clients["nonni"]["repair_price"] = 0
            $ clients["nonni"]["repair_day"] = current_day
            $ clients["nonni"]["order_active"] = False
            $ clients["andrea"]["nonni_delivered"] = True
            jump day5_start
    else:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        m "..."
        "Микко не отвечает."
        k "Я к нему не поеду, если он не отвечает, он может быть занят... или пропал?"
        jump evening_menu