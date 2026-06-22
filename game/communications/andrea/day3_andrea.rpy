label day3_call_andrea:
    $ clients["andrea"]["called"] += 1
    play sound "call_no_answer.mp3" noloop
    scene bg call_no_answer
    a "..."
    "Андреа не отвечает."
    k "Черт, надо что-то придумать"
    jump phone_menu

label day3_andrea_takeaway:
    if actions == 2:
        $ clients["andrea"]["takeaway"] = True
        k "Ты забрал Андреу."
        jump day4_start
    else:
        k "Меня едва хватит дойти до Даров Моря, может, кто-то согласится помочь."
        k "Может, Беккер, если я был к нему добр... или не алчен? Или Микко, как там он вообще?"
        jump evening_menu