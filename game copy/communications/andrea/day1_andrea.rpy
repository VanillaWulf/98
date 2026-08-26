label day1_call_andrea:
    if clients["andrea"]["called"] == 0:
        play sound "call_answer.mp3" noloop
        scene bg call_andrea
        $ clients["andrea"]["called"] += 1
        a "Квист. Я уже дома. Дай человеку отдохнуть."
    else:
        play sound "call_no_answer.mp3" noloop
        scene bg call_no_answer
        a "..."
        "Андреа не отвечает."
    jump phone_menu