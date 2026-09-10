label day1_call_becker:

    # --- Блок проверки бана ---
    if clients["bekker"]["banned"]:
        scene bg call_no_answer
        play sound "call_no_answer.mp3" noloop
        b "..."
        "Беккер не отвечает."
        k "Надеюсь, он не разозлился"  
        jump phone_menu

    $ clients["bekker"]["called"] += 1
    scene bg call_becker
    play sound "call_answer.mp3" noloop

    if clients["bekker"]["called"] == 1:
        $ price = clients["bekker"]["base_price"]
        b "Слушаю. Если нужны детали, всегда рад помочь, но завтра смогу подвезти только 1 микросхему = [price]$. Берешь?"
        menu:
            extend ""
            "Давай, беру (квист, лучше закажи)":
                b "Завтра привезу" 
                $ clients["bekker"]["ordered_part"] = "chip"
                $ money -= clients["bekker"]["base_price"]
                play sound "money_send.mp3" noloop
                "Вы отправили кредиты - [clients['bekker']['base_price']] штук"
            "Не, в другой раз":
                b "Два раза не предлагаю"
    elif clients["bekker"]["called"] ==2:
        scene bg call_becker
        play sound "call_answer.mp3" noloop
        b "Мы вроде уже поговорили - на неделе пополню ассортимент. Ничего нового не скажу"
    elif clients["bekker"]["called"] == 3:
        scene bg call_becker
        play sound "call_answer.mp3" noloop
        b "Ты со мной так не шути, папаша, я могу и разозлиться"
        $ clients["bekker"]["banned"] = True

    jump phone_menu