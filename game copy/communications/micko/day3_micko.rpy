label day3_call_mikko:

$ clients["mikko"]["is_called"] = True
if clients["mikko"]["banned"]:
    scene bg call_no_answer
    play sound "call_no_answer.mp3" noloop
    m "..."
    "Микко не отвечает."
    jump phone_menu

$ clients["mikko"]["called"] += 1

if clients["mikko"]["hangouts_day_2"]:
    scene bg call_mikko
else: 
    scene bg call_mikko_sad

# ---------- ПЕРВЫЙ ЗВОНОК ----------

if clients["mikko"]["called"] == 1:


    play sound "call_answer.mp3" noloop

    if clients["mikko"]["hangouts_day_2"]:

        m "Квист, хорошо, что позвонил. Ты вчера меня здорово выручил."

        k "Как ты?"

        m "Хреново, но спасибо, что спросил. После склада биорук меня выследили."

        k "А меня?"

        m "Тебя нет. Спрашивают только про меня."

        m "Мне нужна помощь. Надо на время исчезнуть."

        k "Насколько всё плохо?"

        m "Серьезнее, чем обычно, Хопп Квист, едь ко мне!"

    else:

        m "Квист, у меня проблемы."

        k "Какие?"

        m "Вчера там на складе биорук... Всё пошло сильно хуже, чем я рассчитывал. Меня выследили."

        k "И что теперь?"

        m "Теперь мне нужна помощь. Приежай ко мне, объясню подробнее. Времени мало"

    jump phone_menu

# ---------- ВТОРОЙ ЗВОНОК ----------

elif clients["mikko"]["called"] == 2:

    if clients["mikko"]["hangouts_day_2"]:
        scene bg call_mikko
    else: 
        scene bg call_mikko_sad
    play sound "call_answer.mp3" noloop

    m "Квист, нет времени объяснять."

    k "Что происходит?"

    m "Встретимся у меня. Приезжай скорее."

    jump phone_menu

# ---------- ТРЕТИЙ ЗВОНОК ----------

elif clients["mikko"]["called"] == 3:

    if clients["mikko"]["hangouts_day_2"]:
        scene bg call_mikko
    else: 
        scene bg call_mikko_sad

    play sound "call_answer.mp3" noloop

    m "Квист, если у меня будут новости, я сам позвоню. Мне нужна помощь, а не звонки"

    $ clients["mikko"]["banned"] = True

    jump phone_menu


label day3_hangout_mikko:

    scene bg city
    
    "Вечером вы встретились с Микко у него дома. Он сразу повёл вас через несколько дворов, постоянно оглядываясь по сторонам."

    "Кто-то действительно искал его. По дороге вам дважды пришлось менять маршрут, заметив незнакомцев, которые явно интересовались не прогулками по району."

    "Несколько часов вы перевозили коробки с документами и деталями между тайниками знакомых Микко."

    "Один раз пришлось даже переждать в закрытой ремонтной мастерской, пока подозрительная машина не уехала."

    "К полуночи всё было закончено."

    "На прощание Микко впервые за вечер улыбнулся и сказал, что теперь у него появился шанс пережить эту неделю."
    $ actions -= 1
    $ clients["mikko"]["hangouts_day_3"] = True
    jump day4_start