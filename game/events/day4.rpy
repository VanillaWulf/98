label day4_start:
    play sound "new_day.mp3" noloop
    play music "rain.mp3" loop

    $ current_day = 4

    scene bg kvist

    "Утро четвёртого дня."

    # Влияние встречи с Микко на количество действий
    if clients["mikko"]["hangouts_day_3"]:
        "После вчерашней встречи с Микко ты абсолютно не выспался... Но ты помогу другу"
        $ actions = 1
        "У вас осталось только одно действие на сегодня."
    else:
        "Ты отлично выспался сегодня."
        $ actions = 2

    # Сброс банов
    $ clients["bekker"]["banned"] = False
    $ clients["nonni"]["banned"] = False
    $ clients["mikko"]["banned"] = False

    # --- Утро ---
    "Четвертый день."

    # Сброс звонков
    python:
        for person in clients:
            clients[person]["called"] = 0

    # ==========================
    # ИВО
    # ==========================
    
    scene bg door
    play sound "door-knock-ivo.mp3" noloop

    "Стук в дверь."

    scene bg ivo

    i "Привет, Квист."

    k "Привет. Как поживает самый крутой хакер в этом городе?"

    i "Не очень - мой браслет окончательно умер. Теперь я даже позвонить никому не могу"

    i "Приходится разговаривать с людьми лично. Ужас."

    k "Сочувствую."

    i "Посмотришь?"

    k "Конечно."

    $ clients["ivo"]["order_active"] = True
    $ clients["ivo"]["order_completed"] = False
    play sound "order.mp3" noloop
    "Добавлен новый заказ: [tr('ivo', 'name')] - [tr('ivo', 'order_name')]"

    i "Спасибо. И... как Андреа?"

    k "Держится."

    i "Это хорошо. Тогда позже зайду за браслетом, а то я уже не могу."

    # ==========================
    # ЛИНЬ ЧИ
    # ==========================

    scene bg door
    play sound "knock.mp3" noloop

    "Стук в дверь."

    scene bg linchi

    l "Доброе утро, Квист."

    # переаботать реакцию
    k "Доброе."

    l "Вчера видела ужасного человека."

    k "Да?"

    l "На магнитном самокате."

    k "Вообще-то вчера таким образом сбили Андрею."

    l "Правда?"

    k "Сейчас она в больнице."

    l "Какой ужас."

    if clients["linh"]["order_active"] and clients["linh"]["order_completed"]:

        l "Кстати, как там мой заказ?"

        menu:
            extend ""

            "Пока не готов":

                l "Жалко."

                $ clients["andrea"]["cure_price"] += 15
                $ clients["pol"]["made_raid"] = True
                $ clients["linh"]["burned"] = True


            "Готов, бесплатно":

                play sound "order.mp3" noloop

                $ clients["linh"]["repair_price"] = 0
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False

                l "Спасибо, дорогой."

                $ clients["andrea"]["cure_price"] += 5

            "Готов, 15 кредитов":

                play sound "order.mp3" noloop

                $ clients["linh"]["repair_price"] = 15
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False

                $ money += 15
                play sound "money.mp3" noloop
                "Вам зачислили 15 кредитов"
                l "Конечно."

                $ clients["andrea"]["cure_price"] += 10
                $ clients["pol"]["made_raid"] = True

            "Готов, 20 кредитов":

                play sound "order.mp3" noloop

                $ clients["linh"]["repair_price"] = 20
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False
                $ clients["andrea"]["cure_price"] += 10
                $ clients["pol"]["made_raid"] = True
                $ clients["linh"]["burned"] = True
                $ money += 20
                play sound "money.mp3" noloop
                "Вам зачислили 20 кредитов"
                l "Дороговато."

    

    elif clients["linh"]["order_active"] and not clients["linh"]["order_completed"]:

        l "Ах, заказ ещё не готов?"

        l "Ну ничего. Подожду."

        $ clients["andrea"]["cure_price"] += 15
        $ clients["pol"]["made_raid"] = True
        $ clients["linh"]["burned"] = True


    else:

        l "Просто зашла проведать."

    # ==========================
    # БЕККЕР
    # ==========================

    if not clients["bekker"]["foreverbanned"]:

        scene bg door
        play sound "door_call.mp3" noloop

        "Звонок в дверь."

        k "Когда я уже найду время починить этот звонок."

        scene bg becker

        b "Привет, Квист."

        # Вариант 1: Заказана только микросхема
        if clients["bekker"]["ordered_part"] == "chip":
            "Беккер достаёт из кармана небольшую упаковку и кладёт её на стол."
            b "Твоя микросхема."
            play sound "order.mp3" noloop
            $ chips += 1
            "Получена микросхема."
            $ clients["bekker"]["ordered_part"] = None
            $ clients["bekker"]["brought_part"] = "chip"

        # Вариант 2: Заказан только провод
        elif clients["bekker"]["ordered_part"] == "wire":
            "Беккер достаёт из кармана моток провода и кладёт его на стол."
            b "Провод, как и договаривались."
            play sound "order.mp3" noloop
            $ wires += 1
            "Получен провод."
            $ clients["bekker"]["ordered_part"] = None
            $ clients["bekker"]["brought_part"] = "wire"

        # Вариант 3: Заказаны и микросхема, и провод
        elif clients["bekker"]["ordered_part"] == "both":
            "Беккер достаёт из кармана микросхему и провод."
            b "Держи, что просил. И микросхема, и провод."
            play sound "order.mp3" noloop
            $ chips += 1
            $ wires += 1
            "Получены микросхема и провод."
            $ clients["bekker"]["ordered_part"] = None
            $ clients["bekker"]["brought_part"] = "both"

        # Заказ не сделан
        if clients["bekker"]["order_active"] and not clients["bekker"]["order_completed"]:

            b "По поводу модуля - скажи мне, что ты хотя бы начал."

            k "..."

            b "Я говорил тебе, что вчера у меня важные дела. Ты подвёл меня. Очень подвёл."

            b "Если из-за этого у меня будут проблемы, у тебя тоже будут проблемы."

            $ clients["pol"]["made_raid"] = True
            # $ clients["bekker"]["foreverbanned"] = True

        # Заказ сделан
        elif clients["bekker"]["order_active"] and clients["bekker"]["order_completed"]:

            b "Надеюсь, ты хотя бы закончил."

            menu:
                extend ""

                "Отдать бесплатно":

                    $ clients["bekker"]["repair_price"] = 0
                    $ clients["bekker"]["repair_day"] = current_day
                    $ clients["bekker"]["order_active"] = False

                    b "Даже бесплатно?"

                    k "Да."

                    b "Поздно. Но спасибо"

                "15 кредитов":

                    $ clients["bekker"]["repair_price"] = 15
                    $ clients["bekker"]["repair_day"] = current_day
                    $ clients["bekker"]["order_active"] = False

                    $ money += 15
                    play sound "money.mp3" noloop
                    "Вам зачислили 15 кредитов"

                    b "Пятнадцать? После всего этого? Больше не приду к тебе чиниться"

                "20 кредитов":

                    $ clients["bekker"]["repair_price"] = 20
                    $ clients["bekker"]["repair_day"] = current_day
                    $ clients["bekker"]["order_active"] = False

                    $ money += 20
                    play sound "money.mp3" noloop
                    "Вам зачислили 20 кредитов"

                    b "Двадцать. Ты подвёл меня и решил заработать на этом. Больше 15 не дам"

        else:

            b "Все работает."

            b "Жаль только, что вчера всё пришлось делать без тебя."

        b "На этой неделе поставок не будет, только на следующей, если ты продержишься"

        "Беккер ушел"


    "День прошел тревожно"
    # ==========================
    # ВЕЧЕР
    # ==========================
    
    jump day4_evening

label day4_evening:
    # Если заказ Нонни всё ещё активен


    # изменить нони всегда звонит с плохими новостями
    scene bg call_nonni_sad
    play sound "call.mp3" noloop

    n "Квист, это Нонни. Андрее стало хуже."
    if clients["nonni"]["order_active"]:
        n "Аппарат нужен срочно. Заканчивай ремонт и привози его как можно быстрее."

        if not clients["andrea"]["takeaway"]:
            n "И да. Андрею забирала я. Раз уж ты не смог. Сделай для неё хотя бы это."
    
    else: 
         n "Аппарат у меня есть, я буду стараться сделать все, что нужно"


    # ==========================
    # ИВО
    # ==========================

    scene bg door
    play sound "door-knock-ivo.mp3" noloop

    "Cтук в дверь."

    scene bg ivo

    i "Ну что, как там мой браслет?"

    k "Работаю. А как там твои поиск уязвимостей в системе ОКБР?"

    i "Ха-ха! Вчера их хакнул! Если ты сделаешь браслет, я для тебя все что угода сделаю, клянусь!"

    k "Запомню. Побудь пока здесь, мне надо все обдумать."

jump evening_menu
    