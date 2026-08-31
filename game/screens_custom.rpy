# ============================================================
# CITY N98 — GAME HUD
# ============================================================

screen game_hud():

    zorder 100

    # =========================================================
    # ОСНОВНОЙ HUD
    # =========================================================

    fixed:

        xalign 0.00
        yalign 0.00

        xsize 830
        ysize 125


        # =====================================================
        # ФОН
        # =====================================================

        add Solid("#050608C8"):

            xpos 0
            ypos 0

            xsize 830
            ysize 125


        # =====================================================
        # КОНТЕНТ
        # =====================================================

        hbox:

            xpos 10
            ypos 10

            xsize 830
            ysize 125

            spacing 0


            # =================================================
            # ДЕНЬ
            # =================================================

            fixed:

                xsize 75
                ysize 135


                text _("ДЕНЬ"):

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

                        xsize 29
                        ysize 29

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


                text _("КРЕДИТЫ"):

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


                text _("ДЕЙСТВИЯ"):

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


                text _("ЗАПАСЫ"):

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
                    ypos 25

                    xsize 50
                    ysize 80


                    text _("ПРОВОДА"):

                        xpos 0
                        ypos 0

                        size 14
                        bold True

                        color "#9EA4A7"


                    hbox:

                        xpos 0
                        ypos 25

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
                    ypos 25

                    xsize 1
                    ysize 60

                    background "#AEB4B722"


                # =================================================
                # МИКРОСХЕМЫ
                # =================================================

                fixed:

                    xpos 155
                    ypos 25

                    xsize 180
                    ysize 80


                    text _("МИКРОСХЕМЫ"):

                        xpos 0
                        ypos 0

                        size 14
                        bold True

                        color "#9EA4A7"


                    hbox:

                        xpos 0
                        ypos 25

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
        yalign 0

        xsize 350
        ysize 440


        # --------------------------------------------------------
        # ФОН
        # --------------------------------------------------------

        add Solid("#050608C0"):

            xsize 500
            ysize 440


        # --------------------------------------------------------
        # КОНТЕНТ
        # --------------------------------------------------------

        vbox:

            xpos 15
            ypos 15

            xsize 400

            spacing 20


            # ====================================================
            # ЗАГОЛОВОК
            # ====================================================

            text _("АКТИВНЫЕ ЗАКАЗЫ"):

                size 27
                bold True
                color "#9EA4A7"

                outlines [
                    (1, "#00000090", 0, 1)
                ]


            # ====================================================
            # СПИСОК ЗАКАЗОВ
            # ====================================================

            vbox:

                xsize 452
                spacing 0


                for key, client in clients.items():

                    if client.get("order_active", False):

                        $ completed = client.get(
                            "order_completed",
                            False
                        )

                        $ client_name = tr(
                            key,
                            "name"
                        )

                        $ order_name = tr(
                            key,
                            "order_name"
                        )


                        # =================================================
                        # ОДИН ЗАКАЗ
                        # =================================================

                        vbox:

                            xsize 452

                            spacing 8


                            # ---------------------------------------------
                            # ИМЯ КЛИЕНТА
                            # ---------------------------------------------

                            if completed:
                                text "[client_name]":

                                    size 24
                                    bold True

                                    color "#88B38A"

                            else:

                                text "[client_name]":

                                    size 24
                                    bold True

                                    color "#C5A35E"


                            # ---------------------------------------------
                            # НАЗВАНИЕ ЗАКАЗА
                            # ---------------------------------------------

                            text "[order_name]":

                                size 18

                                color "#A2A8AA"
                        
                            # ---------------------------------------------
                            # РАЗДЕЛИТЕЛЬ
                            # ---------------------------------------------

                            frame:

                                xsize 370
                                ysize 1

                                if completed:

                                    background "#789F7A45"

                                else:

                                    background "#AEB4B722"


                            null height 14