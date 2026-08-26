# ============================================================
# CITY N98 — GAME HUD
# ============================================================

screen game_hud():

    zorder 100

    # Локализуемые тексты
    $ day_text = _("ДЕНЬ")
    $ credits_text = _("КРЕДИТЫ")
    $ actions_text = _("ДЕЙСТВИЯ")
    $ stock_text = _("ЗАПАСЫ")
    $ wires_text = _("ПРОВОДА")
    $ chips_text = _("МИКРОСХЕМЫ")
    $ orders_text = _("АКТИВНЫЕ ЗАКАЗЫ")
    $ done_text = _("ГОТОВО")


    # =========================================================
    # ОСНОВНОЙ HUD
    # =========================================================

    fixed:

        xalign 0.00
        yalign 0.00

        xsize 830
        ysize 135


        # =====================================================
        # ФОН
        # =====================================================

        add Solid("#050608C8"):

            xpos 0
            ypos 0

            xsize 830
            ysize 135


        # =====================================================
        # КОНТЕНТ
        # =====================================================

        hbox:

            xpos 10
            ypos 10

            xsize 830
            ysize 135

            spacing 0


            # =================================================
            # ДЕНЬ
            # =================================================

            fixed:

                xsize 75
                ysize 135


                text "[day_text]":

                    xpos 8
                    ypos 0

                    size 20
                    bold True

                    color "#9EA4A7"


                hbox:

                    xpos 8
                    ypos 47

                    spacing 5


                    add "images/hud/icon_day.png":

                        xsize 32
                        ysize 32

                        yalign 0.5


                    text "[current_day]":

                        size 35
                        bold True

                        color "#D4D6D7"

                        yalign 0.5


            # =================================================
            # РАЗДЕЛИТЕЛЬ
            # =================================================

            frame:

                xsize 1
                ysize 100

                background "#AEB4B722"

                yalign 0.05


            # =================================================
            # КРЕДИТЫ
            # =================================================

            fixed:

                xsize 125
                ysize 135


                text "[credits_text]":

                    xpos 5
                    ypos 0

                    size 20
                    bold True

                    color "#9EA4A7"


                hbox:

                    xpos 5
                    ypos 47

                    spacing 5


                    add "images/hud/icon_money.png":

                        xsize 32
                        ysize 32

                        yalign 0.5


                    text "[money]":

                        size 35
                        bold True

                        color "#D4D6D7"

                        yalign 0.5


            # =================================================
            # РАЗДЕЛИТЕЛЬ
            # =================================================

            frame:

                xsize 1
                ysize 100

                background "#AEB4B722"

                yalign 0.05


            # =================================================
            # ДЕЙСТВИЯ
            # =================================================

            fixed:

                xsize 125
                ysize 135


                text "[actions_text]":

                    xpos 5
                    ypos 0

                    size 20
                    bold True

                    color "#9EA4A7"


                hbox:

                    xpos 5
                    ypos 47

                    spacing 5


                    add "images/hud/icon_actions.png":

                        xsize 32
                        ysize 32

                        yalign 0.5


                    text "[actions]":

                        size 35
                        bold True

                        color "#D4D6D7"

                        yalign 0.5


            # =================================================
            # РАЗДЕЛИТЕЛЬ
            # =================================================

            frame:

                xsize 1
                ysize 100

                background "#AEB4B722"

                yalign 0.05


            # =================================================
            # ЗАПАСЫ
            # =================================================

            fixed:

                xsize 295
                ysize 135


                text "[stock_text]":

                    xpos 5
                    ypos 0

                    size 20
                    bold True

                    color "#9EA4A7"


                # =================================================
                # ПРОВОДА
                # =================================================

                fixed:

                    xpos 5
                    ypos 43

                    xsize 50
                    ysize 80


                    text "[wires_text]":

                        xpos 0
                        ypos 0

                        size 17
                        bold True

                        color "#9EA4A7"


                    hbox:

                        xpos 0
                        ypos 26

                        spacing 4


                        add "images/hud/icon_wires.png":

                            xsize 28
                            ysize 28

                            yalign 0.5


                        text "[wires]":

                            size 31
                            bold True

                            color "#D4D6D7"

                            yalign 0.5


                # =================================================
                # РАЗДЕЛИТЕЛЬ ВНУТРИ ЗАПАСОВ
                # =================================================

                frame:

                    xpos 130
                    ypos 43

                    xsize 1
                    ysize 60

                    background "#AEB4B722"


                # =================================================
                # МИКРОСХЕМЫ
                # =================================================

                fixed:

                    xpos 155
                    ypos 43

                    xsize 180
                    ysize 80


                    text "[chips_text]":

                        xpos 0
                        ypos 0

                        size 17
                        bold True

                        color "#9EA4A7"


                    hbox:

                        xpos 0
                        ypos 26

                        spacing 4


                        add "images/hud/icon_chips.png":

                            xsize 28
                            ysize 28

                            yalign 0.5


                        text "[chips]":

                            size 31
                            bold True

                            color "#D4D6D7"

                            yalign 0.5
    # ============================================================
    # ПРАВАЯ ПАНЕЛЬ — АКТИВНЫЕ ЗАКАЗЫ
    # ============================================================

    fixed:
        xalign 0.965
        yalign 0.025

        xsize 500
        ysize 440

        add Solid("#050608C0"):
            xsize 500
            ysize 440


        vbox:
            xpos 24
            ypos 20

            xsize 452
            spacing 20


            # Заголовок
            text "[orders_text]":
                size 27
                bold True
                color "#C4C8CA"

                outlines [
                    (1, "#00000090", 0, 1)
                ]


            # Список заказов
            vbox:
                xsize 452
                spacing 0

                for key, client in clients.items():

                    if client.get("order_active", False):

                        $ completed = client.get("order_completed", False)
                        $ client_name = tr(key, "name")
                        $ order_name = tr(key, "order_name")


                        vbox:
                            xsize 452
                            spacing 10


                            hbox:
                                xsize 452
                                spacing 12


                                # Индикатор
                                if completed:

                                    add "images/ui/hud/icon_done.png":
                                        xsize 30
                                        ysize 30
                                        yalign 0.15

                                else:

                                    add "images/ui/hud/icon_order.png":
                                        xsize 30
                                        ysize 30
                                        yalign 0.15


                                # Текст заказа
                                vbox:
                                    xsize 410
                                    spacing 3

                                    if completed:

                                        text "[client_name]":
                                            size 23
                                            bold True
                                            color "#88B38A"

                                    else:

                                        text "[client_name]":
                                            size 23
                                            bold True
                                            color "#C5A35E"


                                    text "[order_name]":
                                        size 18
                                        color "#A2A8AA"


                                    if completed:

                                        text "[done_text]":
                                            size 13
                                            bold True
                                            color "#789F7A"


                            # Разделитель
                            frame:
                                xsize 452
                                ysize 1

                                if completed:
                                    background "#789F7A45"
                                else:
                                    background "#C5A35E45"

                            null height 14
