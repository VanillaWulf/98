label day3_start:
    $ current_day = 3
    scene bg kvist

    # Влияние встречи с Микко на количество действий
    if clients["mikko"]["hangouts_day_2"]:
        "После вчерашней встречи с Микко болит всё тело..."
        $ actions = 1
        "У вас осталось только одно действие на сегодня."
    else:
        "Ты отлично выспался сегодня."
        $ actions = 2

    # Сброс банов для клиентов 
    $ clients["bekker"]["banned"] = False
    $ clients["nonni"]["banned"] = False

    # Сброс счётчиков звонков для всех клиентов
    python:
        for person in clients:
            clients[person]["called"] = 0

    # --- Утро ---
    "Третий день."

    # --- Визит Линь Чи ---
    jump day3_linh_visit

label day3_linh_visit:
    scene bg door
    play sound "knock.mp3" noloop
    "Стук в дверь."

    scene bg linchi
    l "Добрый день, Квист. Как спалось?"

    if clients["mikko"]["hangouts_day_2"]:
        "Квист потирает набитые шишики."
    else:
        k "Как обычно."

    # Ситуации с заказом Линь Чи
    if clients["linh"]["order_active"] and clients["linh"]["order_completed"]:
        # Заказ выполнен – можно сдать
        l "Как там мой заказ?"
        menu:
            extend ""
            "Пока не готов":
                l "Жалко, зайду завтра, милок."
                $ clients["bekker"]["base_price"] += 4
            "Готов, отдам бесплатно":
                play sound "order.mp3" noloop
                $ clients["linh"]["repair_price"] = 0
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False
                l "Спасибо, дорогой! Ты такой добрый."
                $ clients["bekker"]["base_price"] += 1
            "Готов, с тебя 15":
                play sound "order.mp3" noloop
                $ clients["linh"]["repair_price"] = 15
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False
                $ clients["bekker"]["base_price"] += 2
                $ money += 15
                play sound "money.mp3" noloop
                "Вам зачислили 15 кредитов"
                l "Ну ладно, держи. Спасибо."
            "Готов, 20":
                play sound "order.mp3" noloop
                $ clients["linh"]["repair_price"] = 20
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False
                $ clients["bekker"]["base_price"] += 3
                $ money += 20
                play sound "money.mp3" noloop
                "Вам зачислили 15 кредитов"
                l "Ох, дороговато, но что поделать... Спасибо."

    l "Кстати, читал про ограбление Лувра в 2025?"
    k "Я не очень интериceюсь таким"
    if clients["mikko"]["hangouts_day_2"]:            
        l "Несколько месяцев планировали 7 минут, есть чему поучиться."
    else:
        "Ну ладно, там все равно их поймали потом"
    elif clients["linh"]["order_active"] and not clients["linh"]["order_completed"]:
        l "Ах, плеер ещё не готов?.. Ну ладно, подожду."
        $ clients["bekker"]["base_price"] += 4

    "Линь Чи ушла, Квист сидит и пытается проснуться."
    jump day3_bekker_visit

label day3_bekker_visit:
    scene bg door
    play sound "door_call.mp3" noloop
    "Звонок в дверь."
    k "Когда я уже его починю."
    scene bg becker
    b "Привет, Квист."
    if clients["mikko"]["hangouts_day_2"]:
        b "Кстати, слышал, ты во второй день с Микко время проводил."
        k "Слухи быстро расходятся."
        b "Особенно когда кто-то выносит для меня склад биорук. Кстати, скажу поставщикам сильно не борзеть с ценами"
        $ clients["bekker"]["base_price"] -= 2
        k "Понятно."

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
        "Беккер достаёт из сумки моток провода и кладёт его на стол."
        b "Провод, как и договаривались."
        play sound "order.mp3" noloop
        $ wires += 1
        "Получен провод."
        $ clients["bekker"]["ordered_part"] = None
        $ clients["bekker"]["brought_part"] = "wire"

    # Вариант 3: Заказаны и микросхема, и провод
    elif clients["bekker"]["ordered_part"] == "both":
        "Беккер достаёт из кармана микросхему, а из сумки — провод."
        b "Держи, что просил. И микросхема, и провод."
        play sound "order.mp3" noloop
        $ chips += 1
        $ wires += 1
        "Получены микросхема и провод."
        $ clients["bekker"]["ordered_part"] = None
        $ clients["bekker"]["brought_part"] = "both"

    # Проверяем модель: готов, но ещё не сдан
    if clients["bekker"]["order_completed"] and clients["bekker"]["order_active"]:
        b "Кстати, модуль самоката готов? У меня вечером куча дел, надо всё успеть."
        menu:
            extend ""
            "Пока не готов":
                b "Ну давай быстрее. У меня много дел. Просто в очередной раз напоминаю про пол."
            "Готов, отдам бесплатно":
                play sound "order.mp3" noloop
                $ clients["bekker"]["repair_price"] = 0
                $ clients["bekker"]["order_active"] = False
                b "Ты меня спас, папаша. Сделаю тебе скидочку на следующий заказ 2 кредита на деталь, правда всегда поставищи могут офигеть, но все равно лучше, чем ничего"
                $ clients["bekker"]["base_price"] -= 2
            "Готов, с тебя 15":
                play sound "order.mp3" noloop
                $ clients["bekker"]["repair_price"] = 15
                $ clients["bekker"]["order_active"] = False
                $ money += 15
                play sound "money.mp3" noloop
                "Вам зачислили 15 кредитов"
                b "Справедливо."
            "Готов, 20":
                play sound "order.mp3" noloop
                $ clients["bekker"]["repair_price"] = 20
                $ clients["bekker"]["order_active"] = False
                $ money += 20
                play sound "money.mp3" noloop
                "Вам зачислили 20 кредитов"
                b "Начинаю понимать, почему ты дружишь с Микко."

    # Проверяем модель: не готов готов, но ещё не сдан
    elif not clients["bekker"]["order_completed"] and clients["bekker"]["order_active"]:
        b "Кстати, модуль самоката готов?"
        k "А что?"
        b "У меня вечером очень важные дела. И без самоката я на них тупо не успею."
        b "Так что очень надеюсь услышать хорошие новости... хотя бы сегодня вечером."

    # Модуль готов и сдан вчера (день 2)
    elif clients["bekker"]["order_completed"] and not clients["bekker"]["order_active"] and clients["bekker"]["repair_day"] == 2:
        b "Спасибо за модуль самоката. У меня вечером куча дел, должен всё успеть."

    b "Кстати, актуальная цена на следующий заказ [clients['bekker']['base_price']] за запчасть. Пока!"

    # Беккер уходит
    "Беккер уходит."
    jump day2_call_pol

label day2_call_pol:
    scene bg call_pol
    play sound "call.mp3" noloop
    p "Квист, привет! Это Пол."
    p "Слушай, Андрею сбил какой-то придурок, вернее..."
    p "Похоже, потеряла управление на моноколесе. А навстречу как раз ехал какой-то пьяный придурок на магнитном самокате"
    p "Он даже затормозить нормально не успел. Я помог ей дойти до Даров моря, но ей срочно нужна помощь."
    p "Надо помочь ей доехать до Нонни. Я бы сделал сам, но меня вызвали в рейд."
    jump evening_menu