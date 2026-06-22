label evening_menu:
    scene bg kvist
    "Кажется сегодня больше никто не придет, время сделать заказы и позвонить."
    menu:
        extend ""
        "Позвонить":
            jump phone_menu
        "Ремонтировать (-1 действие)" if actions > 0:
            jump repair_menu
        "Встретиться с Микко (-1 действие и вернёшься уже завтра)" if actions > 0:
            jump expression "day" + str(current_day) + "_hangout_mikko"
        "Ждать на вино к Нони (-1 действие, на это потребуются силы)" if actions > 0 and clients["nonni"]["wine_accepted"] and current_day == 2:
            jump day2_noni_hangout
        "Забрать Андрею из Даров моря (-2 действия)" if current_day == 3:
            jump day3_andrea_takeaway
        "Поговорить с Иво" if current_day == 4 and not clients["ivo"]["banned"]:
            jump day4_ivo_talk  
        "Отвезти аппарат к Нонни (-1 действие и вернёшься уже завтра)" if current_day == 4 and clients["nonni"]["order_active"] or (not clients["nonni"]["order_active"] and clients["nonni"]["repair_day"] == 4):
            if not clients["nonni"]["order_completed"]:
                k "И что же ты собрался везти к Нонни, друг?"
                k "Если ты приедеешь без аппарата, она будет пострашнее Линь Чи"
                jump evening_menu
            else:
                jump day4_nonni_move 
        "Спать (восстановит действия и запустить новый день)":
            jump  expression "day" + str(current_day + 1) + "_start" 
            