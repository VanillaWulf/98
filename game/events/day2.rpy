label day2_start:
    play music "rain.mp3" loop
    $ renpy.music.set_volume(0.4, channel='music')
    play sound "new_day.mp3" noloop
    $ current_day = 2
    scene bg kvist
    if clients["mikko"]["hangouts_day_1"]:
        "После вчерашней бурной встречи с Микко голова раскалывается..."
        $ actions = 1
        "У вас осталось только одно действие на сегодня. Зато Микко  помог раздобыть халявный провод"
        "Правда вы прогуляли 5 кредитов, но это все равно дешевле, если брать у Беккера"
    else:
        "Ты отлично выспался сегодня."
        $ actions = 2

    python:
        for person in clients:
            clients[person]["called"] = 0

    $ clients["bekker"]["banned"] = False        

    # --- Утро ---
    "Второй день."

    # --- Визит Линь Чи ---
    jump day2_linh_visit

    label day2_linh_visit:
    scene bg door
    play sound "knock.mp3" noloop
    "Стук в дверь."
    scene bg linchi
    l "Доброе день, Квист. Как спалось?"
    if clients["mikko"]["hangouts_day_1"]:
        "Квист пытается улыбнуться"  
        l "Говорят, кто-то ночью бурогозил... без меня..."
    else:
        k "Добрый, бабуля, Линь, как обычно"  
    if clients["linh"]["order_active"] and clients["linh"]["order_completed"]:

        l "как там мой заказ?"
        menu:
            extend ""
            "Пока не готов":
                l "Жалко, зайду завтра, милок"
                $ clients["bekker"]["base_price"] += 4
            "Готов, отдам бесплатно":
                play sound "order.mp3" noloop
                $ clients["linh"]["repair_price"] = 0
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False
                $ clients["bekker"]["base_price"] += 1
                l "Спасибо, дорогой! Ты такой добрый."
            "Готов, с тебя 15 кредитов":
                play sound "order.mp3" noloop
                $ clients["linh"]["repair_price"] = 15
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False
                $ money += 15
                play sound "money.mp3" noloop
                "Вам зачислили 15 кредитов"
                $ clients["bekker"]["base_price"] += 2
                l "Ну ладно, держи. Спасибо."
            "Готов, 20 кредитов":
                play sound "order.mp3" noloop
                $ clients["linh"]["repair_price"] = 20
                $ clients["linh"]["repair_day"] = current_day
                $ clients["linh"]["order_active"] = False
                $ money += 20
                $ clients["bekker"]["base_price"] += 3
                play sound "money.mp3" noloop
                "Вам зачислили 20 кредитов"
                l "Ох, дороговато, но что поделать... Спасибо."
    elif clients["linh"]["order_active"] and not clients["linh"]["order_completed"]:
        l "Ах, плеер ещё не готов?.. Ну ладно, подожду."
        $ clients["bekker"]["base_price"] += 4
    else:
        l "Просто зашла проведать. Ты хороший мальчик."

    "Линь Чи ушла, Квист сидит и пытается проснуться"    
    jump day2_bekker_visit

    label day2_bekker_visit:
    scene bg door
    play sound "door_call.mp3" noloop
    "Звонок в дверь."
    k "Когда я уже починю этот звонок."
    scene bg becker
    b "Привет, Квист. Дела есть."

    if clients["bekker"]["ordered_part"] == "chip":
        "Беккер достаёт из кармана небольшую упаковку и кладёт её на стол."
        b "Твоя микросхема."
        play sound "order.mp3" noloop
        $ chips += 1
        "Получена микросхема."
        $ clients["bekker"]["ordered_part"] = None
       
    b "Слушай, помощь нужна."
    k "Что случилось?"
    b "Вчера ехал по магнитной дороге на север. И тут где-то впереди что-то рвануло."
    b "Дорогу тряхнуло так, что меня вместе с самокатом швырнуло в ограждение."
    b "Сам живой. Самокат тоже почти живой."
    k "Почти?"
    b "Главный модуль стабилизации накрылся. Теперь эта дрянь не парит над дорогой. Превратилась в очень тяжёлую хрень."
    k "И как добрался домой?"
    b "Тащил его километра три."
    b "Посмотришь?"
    k "Конечно."
    b "Отлично."
    b "Кстати, актуальная цена на следующий заказ [clients['bekker']['base_price']] за запчасть."
    play sound "order.mp3" noloop
    $ clients["bekker"]["order_active"] = True
    $ clients["bekker"]["order_name"] = "Модуль магнитного самоката"
    "Добавлен новый заказ: [tr('bekker', 'name')] - [tr('bekker', 'order_name')]"
    b "Кстати, что за бред у тебя на плакатах? Починим сам?"
    k "А, это Микко пару лет назад решил заняться рекламой и предложил напечатать плакаты"
    k "На каком-то старом корпоративном AI принтере, сам видишь, почему он попал к Микко. Я решил все равно повесить"
    "Беккер улыбается и уходит"

    jump day2_andrea_talk

   