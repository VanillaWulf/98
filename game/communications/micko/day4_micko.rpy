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
            m "Правда придётся отдать пятнадцать кредитов и нужно будет сгонять за ним со мной"
        
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
            m "На лекарства? Давай подзаработаем на них. Приезжай ко мне расскажу"
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
            scene bg micko4_1

            play music "city-street.mp3" loop

            m "Вот и всё. Спасибо ещё раз, Квист. Без тебя я бы с этим не справился."

            k "Не за что. Эти придурки из Авроры отцепились от тебя?"

            m "Больше не звонили, будем думать, что они простили."

            k "Хм, ты всё ещё выращиваешь цветки мора?"

            m "Ага. Для души. И для... ну, ты понял."

            k "Приправы из корней?"

            m "Ага. Её самой. Квист..."

            k "Да?"

            m "Да-да. Передай там Андрее, чтобы поправлялась."

            k "Передам."

            m "Как она?"

            k "Неважно, но с аппаратом Нонни управится."

            $ money += 20
            "Вам зачислили 20 кредитов"
            play sound "money.mp3" noloop
            jump day5_start
        elif money < 15:
        
            if clients["mikko"]["hangouts_day_2"]:
                scene bg call_mikko
            else: 
                scene bg call_mikko_sad

            play sound "call_answer.mp3" noloop
            m "Без 15 кредитов никак, на что аппарат купим?"
            k "Понял, придумаю что-нибудь." 
            jump phone_menu


        else:
            scene bg city

            $ actions -= 1

            scene bg micko4_2

            play music "city-street.mp3" loop

            "Микко увел Квиста на самый север в самый стремный квартал, куда так просто никто не ходил."

            m "Сколько за аппарат?"

            seller "Двадцать пять кредитов."

            k "Двадцать пять?.."

            m "Пятнадцать."

            seller "Двадцать."

            k "Микко, у меня только пятнадцать."

            m "Я знаю."

            seller "Тогда вам тут делать нечего."

            k "Может, нам лучше посмотреть другой?"

            m "Погоди. Пятнадцать кредитов. И сверху пакетик корней мора."

            seller "Выпаренных?"

            m "Да."

            seller "Хм... Ладно. Пятнадцать."

            "Квист перечисляет деньги, а продавец протягивает заветный сверток."
            
            $ money -= 15
            play sound "money_send.mp3" noloop
            "Вы отправили кредиты - 15 штук"

            scene bg micko4_3 
            "Квист бережливо сжимал сверток, пока они шли с Микко обратно через Старый Центр."
            play sound "order.mp3" noloop

            k "Спасибо тебе, Микко. Без тебя я бы точно не справился."

            m "Да брось. Без тебя я бы вообще не знал, где был бы сейчас. И мне..."

            m "Мне Андреа дорога. Так что если могу помочь — помогу."

            if clients["mikko"]["hangouts_day_3"]: 
                k "Кстати, как там твои дела с Авророй?"

                m "Не звонили, надеюсь, забыли."

            m "Знаешь... вспомнил одну странную деталь."

            k "Какую?"

            m "На складе биорук у Авроры, кажется, видел синий платок."

            k "Синий?"

            m "Ага. Такой же, как у Линь Чи."

            k "Ты уверен?"

            m "Да нет, не уверен. Всё слишком быстро было. Может, вообще ошибся."

            "Квист и Микко дошли до Нонни, оставив аппарат. Нонни была немногословна и попросила их ей не мешать."
            "Квист хотел остаться, но Нонни его прогнала домой."

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