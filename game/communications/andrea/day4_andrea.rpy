label day4_call_andrea:
    $ clients["andrea"]["called"] += 1
    play sound "call_no_answer.mp3" noloop
    scene bg call_no_answer
    a "..."
    "Андреа не отвечает."
    k "Я думаю все новости можно узнать у Нонни"
    jump phone_menu