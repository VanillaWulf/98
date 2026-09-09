label day5_start:
   # --- Утро ---
    $ current_day = 5
    "Пятый день."

    scene bg call_nonni_sad
    play sound "call_answer.mp3" noloop

    n "Квист. Андрее совсем плохо. Нужны лекарства."
    n "Стоят [clients['andrea']['cure_price']] кредитов."

    menu:
        extend ""
        "Купить лекарства":
            if money >= clients["andrea"]["cure_price"]:
                $ money -= clients["andrea"]["cure_price"]
                $ clients["andrea"]["medicine_bought"] = True
                n "Хорошо."
                n "Я сразу начну лечение."
            else:
                if (
                    clients["nonni"]["wine_accepted"]
                    and clients["nonni"]["wine_complete"]
                    and clients["andrea"]["takeaway"]
                ):
                    n "Я понимаю."
                    n "Правда понимаю."
                    n "Не вини себя раньше времени."
                    n "Я сделаю всё, что смогу."
                else:
                    n "Понятно."
                    n "Тогда я попробую что-нибудь придумать."

        "У меня нет денег":
            if (
                clients["nonni"]["wine_accepted"]
                and clients["nonni"]["wine_complete"]
                and clients["andrea"]["takeaway"]
            ):
                n "Я понимаю."
                n "Не вини себя."
                n "Я сделаю всё, что смогу."
            else:
                n "Понятно."
                n "Тогда я попробую что-нибудь придумать."

    # ==========================
    # РЕЙД ПОЛА
    # ==========================
    scene bg city
    
    if clients["pol"]["made_raid"] or clients["bekker"]["order_active"] or clients["linh"]["order_active"]:
        scene bg call_pol
        play sound "call.mp3" noloop

        p "Квист."
        p "Мне очень жаль."
        p "Но по твоей мастерской проходит проверка."
        if clients["pol"]["hacked"]:
            p "Или подожди, а где?"
            p "Я клянусь, что когда ехал проверка была в системе, сейчас ее нет, ох уж эти баги."
            p "Извини, что побеспокоил..."
        else: 
            p "Штраф — [clients['pol']['base_price']] кредитов."

            menu:
                extend ""
                "Оплатить штраф":
                    if money >= clients["pol"]["base_price"]:
                        $ money -= clients["pol"]["base_price"]
                        p "Спасибо за понимание."
                        p "На этом всё."
                    else:
                        p "Понимаю."
                        p "Тогда мне придётся тебя забрать."
                        $ clients["pol"]["get_jailed"] = True

                "Не платить":
                    p "Понимаю."
                    p "Тогда мне придётся тебя забрать."
                    $ clients["pol"]["get_jailed"] = True


# ==========================
# ЭПИЛОГ
# ==========================
# Микко
if not clients["mikko"]["is_called"]:
    scene bg city
    "После этих событий Микко исчезает."
    "Квист винит себя, что не звонил ему. Микко часто рискует, ему нужен противовес."
    "Никто не знает, куда именно он пропал."
    
elif not clients["mikko"]["hangouts_day_3"] and clients["mikko"]["is_called"]:
    scene bg micko_good
    "Микко пропал на время, но через некоторое время его находят избитым."
    "Один глаз он теряет навсегда."
    "Нонни удаётся его спасти. Он уже делает важные звонки"

# Судьба Андреи
if not clients["nonni"]["order_active"]:
    if clients["andrea"]["medicine_bought"]:
        scene bg fin_andrea_good
        "Андреа медленно идёт на поправку."
        "Восстановление будет долгим, но Нонни уверена, что она справится."
    else:
        scene bg fin_andrea_bad
        "Состояние Андреи остаётся тяжёлым."
        "Без лекарств лечение идёт гораздо хуже."
else:
    if clients["andrea"]["medicine_bought"]:
        scene bg fin_andrea_critical
        "Андреа остаётся в тяжёлом состоянии."
        "Без аппарата последствия оказываются серьёзнее, чем могли бы быть."
    else:
        scene bg fin_andrea_dead
        "Нонни делает всё, что может."
        "Но без аппарата и лекарств её усилий оказывается недостаточно."
        "Через несколько дней Андреа умирает."

# Квист
if clients["pol"]["get_jailed"]:
    scene bg kvist_jailed
    "Квист оказывается под арестом."
    if clients["mikko"]["hangouts_day_3"]:
        scene bg kvist_jailed_free
        "Через несколько дней Микко каким-то образом решает проблему."
        "Дело неожиданно закрывают."
    else:
        "Квист все сидит и сидит в тюрьме."
else:
    scene bg kvist_hospital
    "Квист старается как можно больше времени проводить рядом с Андреей."

# Мастерская
if clients["linh"]["burned"] or clients["linh"]["order_active"]:
    scene bg burn
    "Однажды ночью мастерская сгорает. Никто не знает, почему и кто стал причиной"
    "От неё остаются только обгоревшие стены. Квист точно кому-то насолил по крупному на этой неделе"
else:
    scene bg repair_shop
    "Мастерская продолжает работать."

# Финал
if (
    not clients["nonni"]["order_active"]
    and clients["andrea"]["medicine_bought"]
    and not clients["pol"]["get_jailed"] 
    and not clients["linh"]["burned"]
):
    "Впервые за долгое время у семьи Квиста появляется надежда."
else:
    "Город N98 продолжает жить дальше."

hide screen quick_menu
hide screen game_hud

call screen city98_credits
