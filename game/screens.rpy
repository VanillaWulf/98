################################################################################
## Инициализация
################################################################################

init offset = -1

################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

# =========================================================
# CITY N98 — DIALOGUE SCREEN
# =========================================================

screen say(who, what):

    # =====================================================
    # DIALOGUE WINDOW
    # =====================================================

    window:

        id "window"

        xalign 0.5
        yalign 1.0

        xsize 1480
        ysize 230

        yoffset -20

        background Fixed(

            # =================================================
            # ТЁМНЫЙ ФОН
            # =================================================

            Solid("#06151BCC"),


            # =================================================
            # ОСНОВНАЯ РАМКА — ПРИГЛУШЁННАЯ
            # =================================================

            # Верхняя линия

            Transform(
                Solid("#00647D55"),
                xpos=0,
                ypos=0,
                xsize=1480,
                ysize=1
            ),

            # Нижняя линия

            Transform(
                Solid("#00647D55"),
                xpos=0,
                ypos=229,
                xsize=1480,
                ysize=1
            ),

            # Левая линия

            Transform(
                Solid("#00647D55"),
                xpos=0,
                ypos=0,
                xsize=1,
                ysize=230
            ),

            # Правая линия

            Transform(
                Solid("#00647D55"),
                xpos=1479,
                ypos=0,
                xsize=1,
                ysize=230
            ),


            # =================================================
            # ВЕРХНИЙ ЛЕВЫЙ УГОЛ
            # =================================================

            Transform(
                Solid("#00B8ED"),
                xpos=0,
                ypos=0,
                xsize=18,
                ysize=2
            ),

            Transform(
                Solid("#00B8ED"),
                xpos=0,
                ypos=0,
                xsize=2,
                ysize=18
            ),


            # =================================================
            # ВЕРХНИЙ ПРАВЫЙ УГОЛ
            # =================================================

            Transform(
                Solid("#00B8ED"),
                xpos=1462,
                ypos=0,
                xsize=18,
                ysize=2
            ),

            Transform(
                Solid("#00B8ED"),
                xpos=1478,
                ypos=0,
                xsize=2,
                ysize=18
            ),


            # =================================================
            # НИЖНИЙ ЛЕВЫЙ УГОЛ
            # =================================================

            Transform(
                Solid("#00B8ED"),
                xpos=0,
                ypos=228,
                xsize=18,
                ysize=2
            ),

            Transform(
                Solid("#00B8ED"),
                xpos=0,
                ypos=212,
                xsize=2,
                ysize=18
            ),


            # =================================================
            # НИЖНИЙ ПРАВЫЙ УГОЛ
            # =================================================

            Transform(
                Solid("#00B8ED"),
                xpos=1462,
                ypos=228,
                xsize=18,
                ysize=2
            ),

            Transform(
                Solid("#00B8ED"),
                xpos=1478,
                ypos=212,
                xsize=2,
                ysize=18
            )
        )


        # =====================================================
        # ИМЯ ПЕРСОНАЖА
        # =====================================================

        if who:

            text who:

                id "who"

                style "say_who"

                xpos 55
                ypos 28


            # -------------------------------------------------
            # ЛИНИЯ ПОД ИМЕНЕМ
            # -------------------------------------------------

            add Solid("#00B8ED"):

                xpos 55
                ypos 73

                xsize 145
                ysize 2


        # =====================================================
        # ТЕКСТ ДИАЛОГА
        # =====================================================

        text what:

            id "what"

            style "say_what"
            color "#B7B9BB" 

            xpos 55
            ypos 95

            xsize 1280

            ymaximum 105


# =========================================================
# SPEAKER NAME
# =========================================================

style say_who:

    font "fonts/DejaVuSans.ttf"

    size 28

    color "#B7B9BB"

    bold False

    xalign 0.0
    yalign 0.0


# =========================================================
# DIALOGUE TEXT
# =========================================================

style say_what:

    font "fonts/DejaVuSans.ttf"

    size 27

    color "#C5A35E"

    xalign 0.0
    yalign 0.0

    text_align 0.0

    line_spacing 4


# =========================================================
# HIDE DEFAULT REN'PY WINDOW STYLES
# =========================================================

style say_window:

    background None

    xfill False
    yfill False


style say_dialogue:

    background None


# =========================================================
# CHARACTER NAME POSITION
# =========================================================

style say_label:

    xpos 55
    ypos 28
    
# screen say(who, what):

#     window:
#         id "window"

#         if who is not None:

#             window:
#                 id "namebox"
#                 style "namebox"
#                 text who id "who"

#         text what id "what"


#     ## Если есть боковое изображение ("голова"), показывает её поверх текста.
#     ## По стандарту не показывается на варианте для мобильных устройств — мало
#     ## места.
#     if not renpy.variant("small"):
#         add SideImage() xalign 0.0 yalign 1.0


# ## Делает namebox доступным для стилизации через объект Character.
# init python:
#     config.character_id_prefixes.append('namebox')

# style window is default
# style say_label is default
# style say_dialogue is default
# style say_thought is say_dialogue

# style namebox is default
# style namebox_label is say_label


# style window:
#     xalign 0.5
#     xfill True
#     yalign gui.textbox_yalign
#     ysize gui.textbox_height

#     background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

# style namebox:
#     xpos gui.name_xpos
#     xanchor gui.name_xalign
#     xsize gui.namebox_width
#     ypos gui.name_ypos
#     ysize gui.namebox_height

#     background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
#     padding gui.namebox_borders.padding

# style say_label:
#     properties gui.text_properties("name", accent=True)
#     xalign gui.name_xalign
#     yalign 0.5

# style say_dialogue:
#     properties gui.text_properties("dialogue")

#     xpos gui.dialogue_xpos
#     xsize gui.dialogue_width
#     ypos gui.dialogue_ypos

#     adjust_spacing False

## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# =========================================================
# CITY N98 — UNIVERSAL CHOICE MENU
# =========================================================


# =========================================================
# CITY N98 — UNIVERSAL CHOICE MENU
# =========================================================

screen choice(items):

    style_prefix "choice"

    vbox:

        for i in items:

            textbutton i.caption:
                action i.action


# =========================================================
# CONTAINER
# =========================================================

style choice_vbox is vbox:

    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing 16


# =========================================================
# BUTTON
# =========================================================

style choice_button is button:

    # -----------------------------------------------------
    # РАЗМЕР КНОПКИ
    # -----------------------------------------------------

    xsize 840
    ysize 84

    padding (28, 8)


    # =====================================================
    # ОБЫЧНОЕ СОСТОЯНИЕ
    # =====================================================

    background Fixed(

        # -------------------------------------------------
        # ТЁМНЫЙ ПРОЗРАЧНЫЙ ФОН
        # -------------------------------------------------

        Solid("#030b0fDD"),


        # -------------------------------------------------
        # ЛЕВАЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00647d"),
            xpos=0,
            ypos=0,
            xsize=2,
            ysize=84
        ),


        # -------------------------------------------------
        # ВЕРХНЯЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00647d"),
            xpos=2,
            ypos=0,
            xsize=836,
            ysize=1
        ),


        # -------------------------------------------------
        # НИЖНЯЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00647d"),
            xpos=2,
            ypos=83,
            xsize=836,
            ysize=1
        ),


        # -------------------------------------------------
        # ПРАВАЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00647d"),
            xpos=838,
            ypos=0,
            xsize=2,
            ysize=84
        )
    )


    # =====================================================
    # HOVER
    # =====================================================

    hover_background Fixed(

        # -------------------------------------------------
        # ФОН
        # -------------------------------------------------

        Solid("#06151BEE"),


        # -------------------------------------------------
        # ЛЕВАЯ ЯРКАЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00b8ed"),
            xpos=0,
            ypos=0,
            xsize=3,
            ysize=84
        ),


        # -------------------------------------------------
        # ВЕРХНИЙ ЛЕВЫЙ УГОЛ
        # -------------------------------------------------

        Transform(
            Solid("#00b8ed"),
            xpos=0,
            ypos=0,
            xsize=11,
            ysize=1
        ),


        # -------------------------------------------------
        # НИЖНИЙ ЛЕВЫЙ УГОЛ
        # -------------------------------------------------

        Transform(
            Solid("#00b8ed"),
            xpos=0,
            ypos=83,
            xsize=11,
            ysize=1
        ),


        # -------------------------------------------------
        # ВЕРХНЯЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00647d"),
            xpos=3,
            ypos=0,
            xsize=825,
            ysize=1
        ),


        # -------------------------------------------------
        # НИЖНЯЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00647d"),
            xpos=3,
            ypos=83,
            xsize=825,
            ysize=1
        ),


        # -------------------------------------------------
        # ПРАВАЯ ЛИНИЯ
        # -------------------------------------------------

        Transform(
            Solid("#00647d"),
            xpos=838,
            ypos=0,
            xsize=2,
            ysize=84
        ),


        # =================================================
        # ВЕРХНИЙ ПРАВЫЙ УГОЛ
        # =================================================

        Transform(
            Solid("#00b8ed"),
            xpos=828,
            ypos=0,
            xsize=10,
            ysize=1
        ),

        Transform(
            Solid("#00b8ed"),
            xpos=838,
            ypos=0,
            xsize=2,
            ysize=10
        ),


        # =================================================
        # НИЖНИЙ ПРАВЫЙ УГОЛ
        # =================================================

        Transform(
            Solid("#00b8ed"),
            xpos=828,
            ypos=83,
            xsize=10,
            ysize=1
        ),

        Transform(
            Solid("#00b8ed"),
            xpos=838,
            ypos=74,
            xsize=2,
            ysize=10
        ),


        # =================================================
        # СТРЕЛКА
        # =================================================

        Transform(
            Text(
                "›",
                font="fonts/DejaVuSans.ttf",
                size=42,
                color="#00b8ed"
            ),
            xpos=800,
            ypos=42,
            xanchor=0.5,
            yanchor=0.5
        )
    )


    # =====================================================
    # ЗВУКИ
    # =====================================================

    hover_sound "audio/hover.mp3"
    activate_sound "audio/menu_select.mp3"


# =========================================================
# BUTTON TEXT
# =========================================================

style choice_button_text is button_text:

    font "fonts/DejaVuSans.ttf"

    size 25

    color "#b7b9bb"

    hover_color "#00b8ed"

    xalign 0.0
    yalign 0.5

    text_align 0.0


# =========================================================
# DISABLED CHOICE TEXT
# =========================================================

style choice_button_text_disabled is choice_button_text:

    color "#596167"

# =========================================================
# ЗАПАСНЫЕ СТИЛИ REN'PY
# =========================================================

style choice_button is default

style choice_vbox is vbox

## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

# =========================================================
# QUICK MENU — CITY N98
# =========================================================

screen quick_menu():

    zorder 100

    key "game_menu" action ShowMenu("game_menu", title="Меню")

    if quick_menu:

        fixed:

            # =====================================================
            # ОБЩАЯ ПОЗИЦИЯ QUICK MENU
            # =====================================================

            # -----------------------------------------------------
            # ПРОПУСК — СЛЕВА
            # -----------------------------------------------------

            button:
                style "quick_button"

                xpos 45
                ypos config.screen_height - 40

                action Skip()
                alternate Skip(fast=True, confirm=True)

                hbox:
                    spacing 9
                    yalign 0.5

                    # add "images/hud/skip.png":
                    #     xsize 24
                    #     ysize 24

                    text _("ПРОПУСК"):
                        style "quick_button_text"


            # -----------------------------------------------------
            # МЕНЮ — СПРАВА
            # -----------------------------------------------------

            button:
                style "quick_button"

                xpos config.screen_width - 150
                ypos config.screen_height - 40

                action ShowMenu("game_menu", title="Меню")

                hbox:
                    spacing 9
                    yalign 0.5

                    # add "images/hud/game_menu.png":
                    #     xsize 24
                    #     ysize 24

                    text _("МЕНЮ"):
                        style "quick_button_text"
## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

# =========================================================
# QUICK MENU STYLES — CITY N98
# =========================================================

style quick_menu:
    xalign 1.0
    yalign 1.0

    # Отступ от правого и нижнего края
    xoffset -55
    yoffset -18

    spacing 22


style quick_button:
    background None
    hover_background None

    padding (0, 0)

    xminimum 125
    yminimum 32

    hover_sound "audio/menu_hover.mp3"
    activate_sound "audio/menu_click.mp3"


style quick_button_text:
    font "fonts/DejaVuSans.ttf"
    size 19

    color "#B7B9BB"
    idle_color "#B7B9BB"
    hover_color "#FFFFFF"

    insensitive_color "#697278"

style quick_menu:
    xalign 0.5
    yalign 1.0


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen main_menu():
    tag menu

    # Фон всего меню
    add "menu_bg" xysize (config.screen_width, config.screen_height)

    # # Затемнение левой панели
    # add Solid("#050a0d") xsize 650 ysize 1080

    # # Тонкая голубая граница панели
    # add Solid("#00a9dc") xpos 648 ypos 0 xsize 3 ysize 1080

    # # Внутренняя рамка панели
    # add Solid("#18303a") xpos 25 ypos 20 xsize 600 ysize 2
    # add Solid("#18303a") xpos 25 ypos 1058 xsize 600 ysize 2
    # add Solid("#18303a") xpos 25 ypos 20 xsize 2 ysize 1040
    # add Solid("#18303a") xpos 623 ypos 20 xsize 2 ysize 1040

    # ==========================================
    # ЛОГОТИП
    # ==========================================

    text "CITY N98":
        xpos 70
        ypos 145
        style "menu_title"

    text "SYSTEM MENU":
        xpos 70
        ypos 225
        style "menu_subtitle"

    # ==========================================
    # КНОПКИ
    # ==========================================

    vbox:
        xpos 70
        ypos 295
        spacing 15

        textbutton "НАЧАТЬ":
            style "main_menu_button"
            action Start()

        textbutton "НАСТРОЙКИ":
            style "main_menu_button"
            action ShowMenu("preferences")  

        textbutton "ОБ ИГРЕ":
            style "main_menu_button"
            action ShowMenu("about")

        textbutton "ВЫХОД":
            style "main_menu_button"
            action Confirm(_("Вы уверены, что хотите выйти?"), Quit(confirm=False))

    # ==========================================
    # ВЕРСИЯ
    # ==========================================

    text "N98-7F":
        xpos 80
        ypos 885
        style "menu_version"

    text "v1.0":
        xpos 80
        ypos 925
        style "menu_version"


# =========================================================
# СТИЛИ ГЛАВНОГО МЕНЮ
# =========================================================

style menu_title:
    font "fonts/DejaVuSans.ttf"
    size 64
    color "#DFA45A"
    bold True

style menu_subtitle:
    font "fonts/DejaVuSans.ttf"
    size 24
    color "#899196"
    kerning 2

style menu_version:
    font "fonts/DejaVuSans.ttf"
    size 22
    color "#697278"

style main_menu_button:
    background None

    hover_sound "audio/hover.mp3"
    activate_sound "audio/menu_select.mp3"

    hover_background Fixed(
        # =====================================================
        # ФОН КНОПКИ
        # =====================================================

        Solid("#06151b"),

        # =====================================================
        # ЛЕВАЯ ЯРКАЯ ЛИНИЯ
        # =====================================================

        Transform(
            Solid("#00b8ed"),
            xpos=0,
            ypos=0,
            xsize=3,
            ysize=55
        ),

        # =====================================================
        # ВЕРХНЯЯ ЛИНИЯ
        # =====================================================

        Transform(
            Solid("#00647d"),
            xpos=3,
            ypos=0,
            xsize=393,
            ysize=1
        ),

        # =====================================================
        # НИЖНЯЯ ЛИНИЯ
        # =====================================================

        Transform(
            Solid("#00647d"),
            xpos=3,
            ypos=54,
            xsize=393,
            ysize=1
        ),

        # =====================================================
        # ПРАВАЯ ТОНКАЯ ЛИНИЯ
        # =====================================================

        Transform(
            Solid("#00647d"),
            xpos=397,
            ypos=0,
            xsize=1,
            ysize=55
        ),

        # =====================================================
        # ВЕРХНИЙ ПРАВЫЙ ДЕКОРАТИВНЫЙ СЕГМЕНТ
        # =====================================================

        Transform(
            Solid("#00b8ed"),
            xpos=388,
            ypos=0,
            xsize=10,
            ysize=1
        ),

        Transform(
            Solid("#00b8ed"),
            xpos=397,
            ypos=0,
            xsize=1,
            ysize=9
        ),

        # =====================================================
        # НИЖНИЙ ПРАВЫЙ ДЕКОРАТИВНЫЙ СЕГМЕНТ
        # =====================================================

        Transform(
            Solid("#00b8ed"),
            xpos=388,
            ypos=53,
            xsize=10,
            ysize=1
        ),

        Transform(
            Solid("#00b8ed"),
            xpos=397,
            ypos=46,
            xsize=1,
            ysize=9
        ),

        # =====================================================
        # СТРЕЛКА
        # =====================================================

        Transform(
            Text(
                "›",
                font="fonts/DejaVuSans.ttf",
                size=38,
                color="#00b8ed"
            ),
            xpos=365,
            ypos=5
        )
    )

    # =========================================================
    # РАЗМЕР КНОПКИ
    # =========================================================

    xsize 400
    ysize 55

    padding (20, 10)


style main_menu_button_text:
    font "fonts/DejaVuSans.ttf"
    size 26
    color "#b7b9bb"
    hover_color "#00b8ed"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None или один из "viewport" или "vpgrid". Этот
## экран предназначен для использования с одним или несколькими дочерними
## элементами, которые трансклюдируются (помещаются) внутрь него.

init python:
    class MyMainMenu(Action):
        def __call__(self):
            renpy.full_restart()

## =========================================================
## ИГРОВОЕ МЕНЮ — ESC
## =========================================================

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    tag menu

    # =====================================================
    # ФОН
    # =====================================================

    add "menu_bg" xysize (config.screen_width, config.screen_height)

    # =====================================================
    # ЛОГОТИП
    # =====================================================

    text "CITY N98":
        xpos 70
        ypos 145
        style "menu_title"

    text "SYSTEM MENU":
        xpos 70
        ypos 225
        style "menu_subtitle"

    # =====================================================
    # КНОПКИ
    # =====================================================

    vbox:
        xpos 70
        ypos 295
        spacing 15

        # ГЛАВНОЕ МЕНЮ
        textbutton _("ГЛАВНОЕ МЕНЮ"):
            style "main_menu_button"
            action Confirm(
                _("Вы уверены, что хотите вернуться в\n главное меню? Весь прогресс\n будет потерян."),
                MyMainMenu()
            )

        # НОВАЯ ИГРА
        textbutton "НОВАЯ ИГРА":
            style "main_menu_button"
            action Confirm(_("Начать новую игру?"),Start())

        # НАСТРОЙКИ
        textbutton "НАСТРОЙКИ":
            style "main_menu_button"
            action ShowMenu("preferences")

        # ИСТОРИЯ
        textbutton "ИСТОРИЯ":
            style "main_menu_button"
            action ShowMenu("history")

        # ОБ ИГРЕ
        textbutton "ОБ ИГРЕ":
            style "main_menu_button"
            action ShowMenu("about")

        # НАЗАД
        textbutton "НАЗАД":
            style "main_menu_button"
            action Return()

        # ВЫХОД
        textbutton "ВЫХОД":
            style "main_menu_button"
            action Confirm(_("Вы уверены, что хотите выйти?"), Quit(confirm=False))

    # =====================================================
    # ВЕРСИЯ
    # =====================================================

    text "N98-7F":
        xpos 80
        ypos 885
        style "menu_version"

    text "v1.0":
        xpos 80
        ypos 925
        style "menu_version"



style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

# =========================================================
# ЭКРАН "ОБ ИГРЕ"
# =========================================================

screen about():

    tag menu

    # =====================================================
    # ФОН
    # =====================================================

    add "menu_bg" xysize (config.screen_width, config.screen_height)


    # =====================================================
    # ЛОГОТИП
    # =====================================================

    text "CITY N98":
        xpos 70
        ypos 145
        style "menu_title"


    text "ABOUT SYSTEM":
        xpos 70
        ypos 225
        style "menu_subtitle"


    # =====================================================
    # ИНФОРМАЦИЯ ОБ ИГРЕ
    # =====================================================

    vbox:
        xpos 70
        ypos 315
        xsize 350
        spacing 22

        text "ПРЕДИСЛОВИЕ":
            style "about_heading"

        text "Это игра-предисловие к книге о городе 98.":
            style "about_text"

        text "Небольшая история, которая знакомит с городом, его атмосферой и событиями, предшествующими основной истории.":
            style "about_text"


    # =====================================================
    # ВЕРСИЯ
    # =====================================================

    text "VERSION":
        xpos 70
        ypos 780
        style "about_version_label"

    text "[config.version]":
        xpos 70
        ypos 815
        style "about_version"


    # =====================================================
    # КНОПКА НАЗАД
    # =====================================================

    textbutton "НАЗАД":
        style "main_menu_button"
        xpos 70
        ypos 900
        action Return()


# =========================================================
# СТИЛИ ЭКРАНА "ОБ ИГРЕ"
# =========================================================

style about_heading:
    font "fonts/DejaVuSans.ttf"
    size 22
    color "#00b8ed"
    bold True


style about_text:
    font "fonts/DejaVuSans.ttf"
    size 25
    color "#b7b9bb"
    line_spacing 8


style about_version_label:
    font "fonts/DejaVuSans.ttf"
    size 18
    color "#697278"
    kerning 2


style about_version:
    font "fonts/DejaVuSans.ttf"
    size 22
    color "#899196"

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

# screen save():

#     tag menu

#     use file_slots(_("Сохранить"))


# screen load():

#     tag menu

#     use file_slots(_("Загрузить"))


# screen file_slots(title):

#     default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

#     use game_menu(title):

#         fixed:

#             ## Это гарантирует, что ввод будет принимать enter перед остальными
#             ## кнопками.
#             order_reverse True

#             ## Номер страницы, который может быть изменён посредством клика на
#             ## кнопку.
#             button:
#                 style "page_label"

#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()

#                 input:
#                     style "page_label_text"
#                     value page_name_value

#             ## Таблица слотов.
#             grid gui.file_slot_cols gui.file_slot_rows:
#                 style_prefix "slot"

#                 xalign 0.5
#                 yalign 0.5

#                 spacing gui.slot_spacing

#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):

#                     $ slot = i + 1

#                     button:
#                         action FileAction(slot)

#                         has vbox

#                         add FileScreenshot(slot) xalign 0.5

#                         text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
#                             style "slot_time_text"

#                         text FileSaveName(slot):
#                             style "slot_name_text"

#                         key "save_delete" action FileDelete(slot)

#             ## Кнопки для доступа к другим страницам.
#             vbox:
#                 style_prefix "page"

#                 xalign 0.5
#                 yalign 1.0

#                 hbox:
#                     xalign 0.5

#                     spacing gui.page_spacing

#                     textbutton _("<") action FilePagePrevious()
#                     key "save_page_prev" action FilePagePrevious()

#                     if config.has_autosave:
#                         textbutton _("{#auto_page}А") action FilePage("auto")

#                     if config.has_quicksave:
#                         textbutton _("{#quick_page}Б") action FilePage("quick")

#                     ## range(1, 10) задаёт диапазон значений от 1 до 9.
#                     for page in range(1, 10):
#                         textbutton "[page]" action FilePage(page)

#                     textbutton _(">") action FilePageNext()
#                     key "save_page_next" action FilePageNext()

#                 if config.has_sync:
#                     if CurrentScreenName() == "save":
#                         textbutton _("Загрузить Sync"):
#                             action UploadSync()
#                             xalign 0.5
#                     else:
#                         textbutton _("Скачать Sync"):
#                             action DownloadSync()
#                             xalign 0.5


# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text

# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text

# style page_label:
#     xpadding 75
#     ypadding 5
#     xalign 0.5

# style page_label_text:
#     textalign 0.5
#     layout "subtitle"
#     hover_color gui.hover_color

# style page_button:
#     properties gui.button_properties("page_button")

# style page_button_text:
#     properties gui.text_properties("page_button")

# style slot_button:
#     properties gui.button_properties("slot_button")

# style slot_button_text:
#     properties gui.text_properties("slot_button")


## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

# screen preferences():

#     tag menu

#     use game_menu(_("Настройки"), scroll="viewport"):

#         vbox:

#             hbox:
#                 box_wrap True

#                 if renpy.variant("pc") or renpy.variant("web"):

#                     vbox:
#                         style_prefix "radio"
#                         label _("Режим экрана")
#                         textbutton _("Оконный") action Preference("display", "window")
#                         textbutton _("Полный") action Preference("display", "fullscreen")

#                 vbox:
#                     style_prefix "check"
#                     label _("Пропуск")
#                     textbutton _("Всего текста") action Preference("skip", "toggle")
#                     textbutton _("После выборов") action Preference("after choices", "toggle")
#                     textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))

#                 ## Дополнительные vbox'ы типа "radio_pref" или "check_pref"
#                 ## могут быть добавлены сюда для добавления новых настроек.

#             null height (4 * gui.pref_spacing)

#             hbox:
#                 style_prefix "slider"
#                 box_wrap True

#                 vbox:

#                     label _("Скорость текста")

#                     bar value Preference("text speed")

#                     label _("Скорость авточтения")

#                     bar value Preference("auto-forward time")

#                 vbox:

#                     if config.has_music:
#                         label _("Громкость музыки")

#                         hbox:
#                             bar value Preference("music volume")

#                     if config.has_sound:

#                         label _("Громкость звуков")

#                         hbox:
#                             bar value Preference("sound volume")

#                             if config.sample_sound:
#                                 textbutton _("Тест") action Play("sound", config.sample_sound)


#                     if config.has_voice:
#                         label _("Громкость голоса")

#                         hbox:
#                             bar value Preference("voice volume")

#                             if config.sample_voice:
#                                 textbutton _("Тест") action Play("voice", config.sample_voice)

#                     if config.has_music or config.has_sound or config.has_voice:
#                         null height gui.pref_spacing

#                         textbutton _("Без звука"):
#                             action Preference("all mute", "toggle")
#                             style "mute_all_button"

# =========================================================
# НАСТРОЙКИ
# =========================================================

screen preferences():

    tag menu

    # =====================================================
    # ФОН
    # =====================================================

    add "menu_bg" xysize (config.screen_width, config.screen_height)


    # =====================================================
    # ЗАГОЛОВОК
    # =====================================================

    text "CITY N98":
        xpos 70
        ypos 145
        style "menu_title"

    text "SYSTEM SETTINGS":
        xpos 70
        ypos 225
        style "menu_subtitle"


    # =====================================================
    # НАСТРОЙКИ — ОДНА КОЛОНКА
    # =====================================================

    # -----------------------------------------------------
    # СКОРОСТЬ ТЕКСТА
    # -----------------------------------------------------

    text "СКОРОСТЬ ТЕКСТА":
        xpos 70
        ypos 315
        style "settings_label"

    bar:
        value Preference("text speed")
        xpos 70
        ypos 355
        xsize 400
        ysize 12
        style "settings_slider"


    # -----------------------------------------------------
    # ГРОМКОСТЬ МУЗЫКИ
    # -----------------------------------------------------

    text "ГРОМКОСТЬ МУЗЫКИ":
        xpos 70
        ypos 425
        style "settings_label"

    bar:
        value Preference("music volume")
        xpos 70
        ypos 465
        xsize 400
        ysize 12
        style "settings_slider"


    # -----------------------------------------------------
    # ГРОМКОСТЬ ЗВУКОВ
    # -----------------------------------------------------

    text "ГРОМКОСТЬ ЗВУКОВ":
        xpos 70
        ypos 535
        style "settings_label"

    bar:
        value Preference("sound volume")
        xpos 70
        ypos 575
        xsize 400
        ysize 12
        style "settings_slider"
    
    # -----------------------------------------------------
    # язык
    # -----------------------------------------------------
    
    text "ЯЗЫК":
        xpos 70
        ypos 755  # подстройте координаты под ваше меню
        style "settings_label"

    textbutton "РУССКИЙ":
        xpos 70
        ypos 795
        style "settings_option"
        action Function(renpy.change_language, None)
        selected (preferences.language == None)

    textbutton "ENGLISH":
        xpos 300
        ypos 795
        style "settings_option"
        action Function(renpy.change_language, "english")
        selected (preferences.language == "english")


    # -----------------------------------------------------
    # РЕЖИМ ЭКРАНА
    # -----------------------------------------------------

    text "РЕЖИМ ЭКРАНА":
        xpos 70
        ypos 645
        style "settings_label"

    textbutton "ОКОННЫЙ":
        xpos 70
        ypos 685
        style "settings_option"
        action Preference("display", "window")
        selected (not _preferences.fullscreen) 

    textbutton "ПОЛНЫЙ":
        xpos 300
        ypos 685
        style "settings_option"
        action Preference("display", "fullscreen")
        selected (_preferences.fullscreen)

    # =====================================================
    # НАЗАД
    # =====================================================

    textbutton "НАЗАД":
        xpos 70
        ypos 900
        style "main_menu_button"
        action Return()
# =========================================================
# СТИЛИ НАСТРОЕК
# =========================================================

style settings_label:
    font "fonts/DejaVuSans.ttf"
    size 24
    color "#00b8ed"
    kerning 1


style settings_option:
    font "fonts/DejaVuSans.ttf"
    size 30

    # Цвета самой кнопки (фона, рамки) – у вас их нет
    background None
    hover_background None


    xsize 130
    ysize 45
    padding (0, 0)

    hover_sound "audio/hover.mp3"
    activate_sound "audio/menu_select.mp3"

style settings_option_text:
    font "fonts/DejaVuSans.ttf"
    size 26
    color "#b7b9bb"
    hover_color "#00b8ed"
    selected_color "#00b8ed"


style settings_slider is slider:
    xsize 400
    ysize 12

    base_bar Solid("#063542")
    thumb Solid("#00b8ed")

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html



# =========================================================
# ЭКРАН ИСТОРИИ
# =========================================================

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


screen history():

    tag menu

    # =====================================================
    # ФОН
    # =====================================================

    add "menu_bg" xysize (config.screen_width, config.screen_height)


    # =====================================================
    # ЛЕВАЯ ПАНЕЛЬ
    # =====================================================

    text "CITY N98":
        xpos 70
        ypos 145
        style "menu_title"

    text "HISTORY LOG":
        xpos 70
        ypos 225
        style "menu_subtitle"


    # =====================================================
    # ИСТОРИЯ — ПРАВАЯ ЧАСТЬ
    # =====================================================

    if _history_list:

        viewport:

            xpos 550
            ypos 300

            xsize 1080
            ysize 545

            mousewheel True
            draggable True

            scrollbars "vertical"

            yinitial 1.0


            vbox:

                xsize 1010
                spacing 26


                for h in _history_list:

                    vbox:

                        xsize 980
                        spacing 6


                        # -----------------------------
                        # ИМЯ
                        # -----------------------------

                        if h.who:

                            text h.who:

                                style "history_name"

                                substitute False

                                if "color" in h.who_args:
                                    color h.who_args["color"]


                        # -----------------------------
                        # РЕПЛИКА
                        # -----------------------------

                        $ what = renpy.filter_text_tags(
                            h.what,
                            allow=gui.history_allow_tags
                        )

                        text what:

                            style "history_text"

                            substitute False


    else:

        text "ИСТОРИЯ ДИАЛОГОВ ПУСТА":

            xpos 550
            ypos 320

            style "history_empty"


    # =====================================================
    # НАЗАД
    # =====================================================

    textbutton "НАЗАД":

        style "main_menu_button"

        xpos 70
        ypos 900

        action Return()


# =========================================================
# СТИЛИ ИСТОРИИ
# =========================================================

style history_name:

    font "fonts/DejaVuSans.ttf"
    size 21
    color "#00b8ed"
    bold True


style history_text:
    font "fonts/DejaVuSans.ttf"
    size 23
    color "#b7b9bb"
    line_spacing 5


style history_empty:
    font "fonts/DejaVuSans.ttf"
    size 22
    color "#697278"



## Это определяет, какие теги могут отображаться на экране истории.

# define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


# style history_window is empty

# style history_name is gui_label
# style history_name_text is gui_label_text
# style history_text is gui_text

# style history_label is gui_label
# style history_label_text is gui_label_text

# style history_window:
#     xfill True
#     ysize gui.history_height

# style history_name:
#     xpos gui.history_name_xpos
#     xanchor gui.history_name_xalign
#     ypos gui.history_name_ypos
#     xsize gui.history_name_width

# style history_name_text:
#     min_width gui.history_name_width
#     textalign gui.history_name_xalign

# style history_text:
#     xpos gui.history_text_xpos
#     ypos gui.history_text_ypos
#     xanchor gui.history_text_xalign
#     xsize gui.history_text_width
#     min_width gui.history_text_width
#     textalign gui.history_text_xalign
#     layout ("subtitle" if gui.history_text_xalign else "tex")

# style history_label:
#     xfill True

# style history_label_text:
#     xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

# screen help():

#     tag menu

#     default device = "keyboard"

#     use game_menu(_("Помощь"), scroll="viewport"):

#         style_prefix "help"

#         vbox:
#             spacing 23

#             hbox:

#                 textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
#                 textbutton _("Мышь") action SetScreenVariable("device", "mouse")

#                 if GamepadExists():
#                     textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

#             if device == "keyboard":
#                 use keyboard_help
#             elif device == "mouse":
#                 use mouse_help
#             elif device == "gamepad":
#                 use gamepad_help


# screen keyboard_help():

#     hbox:
#         label _("Enter")
#         text _("Прохождение диалогов, активация интерфейса.")

#     hbox:
#         label _("Пробел")
#         text _("Прохождение диалогов без возможности делать выбор.")

#     hbox:
#         label _("Стрелки")
#         text _("Навигация по интерфейсу.")

#     hbox:
#         label _("Esc")
#         text _("Вход в игровое меню.")

#     hbox:
#         label _("Ctrl")
#         text _("Пропускает диалоги, пока зажат.")

#     hbox:
#         label _("Tab")
#         text _("Включает режим пропуска.")

#     hbox:
#         label _("Page Up")
#         text _("Откат назад по сюжету игры.")

#     hbox:
#         label _("Page Down")
#         text _("Откатывает предыдущее действие вперёд.")

#     hbox:
#         label "H"
#         text _("Скрывает интерфейс пользователя.")

#     hbox:
#         label "S"
#         text _("Делает снимок экрана.")

#     hbox:
#         label "V"
#         text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")

#     hbox:
#         label "Shift+A"
#         text _("Открывает меню специальных возможностей.")


# screen mouse_help():

#     hbox:
#         label _("Левый клик")
#         text _("Прохождение диалогов, активация интерфейса.")

#     hbox:
#         label _("Клик колёсиком")
#         text _("Скрывает интерфейс пользователя.")

#     hbox:
#         label _("Правый клик")
#         text _("Вход в игровое меню.")

#     hbox:
#         label _("Колёсико вверх")
#         text _("Откат назад по сюжету игры.")

#     hbox:
#         label _("Колёсико вниз")
#         text _("Откатывает предыдущее действие вперёд.")


# screen gamepad_help():

#     hbox:
#         label _("Правый триггер\nA/Нижняя кнопка")
#         text _("Прохождение диалогов, активация интерфейса.")

#     hbox:
#         label _("Левый Триггер\nЛевый Бампер")
#         text _("Откат назад по сюжету игры.")

#     hbox:
#         label _("Правый бампер")
#         text _("Откатывает предыдущее действие вперёд.")

#     hbox:
#         label _("Крестовина, Стики")
#         text _("Навигация по интерфейсу.")

#     hbox:
#         label _("Старт, Гид, B/Правая кнопка")
#         text _("Вход в игровое меню.")

#     hbox:
#         label _("Y/Верхняя кнопка")
#         text _("Скрывает интерфейс пользователя.")

#     textbutton _("Калибровка") action GamepadCalibrate()


# style help_button is gui_button
# style help_button_text is gui_button_text
# style help_label is gui_label
# style help_label_text is gui_label_text
# style help_text is gui_text

# style help_button:
#     properties gui.button_properties("help_button")
#     xmargin 12

# style help_button_text:
#     properties gui.text_properties("help_button")

# style help_label:
#     xsize 375
#     right_padding 30

# style help_label_text:
#     size gui.text_size
#     xalign 1.0
#     textalign 1.0



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Пропускаю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Пузырьковый экран ###########################################################
##
## Экран пузырьков используется для отображения диалога игроку при использовании
## речевых пузырьков. Экран пузырьков принимает те же параметры, что и экран
## say, должен создать отображаемый объект с id "what", и может создавать
## отображаемые объекты с id "namebox", "who" и "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
# screen quick_menu():
#     variant "touch"

#     zorder 100

#     if quick_menu:

#         hbox:
#             style "quick_menu"
#             style_prefix "quick"

#             # textbutton _("Назад") action Rollback()
#             textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
#             # textbutton _("Авто") action Preference("auto-forward", "toggle")
#             textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

# ============================================================
# ТРАНСФОРМАЦИЯ ДЛЯ ПРОКРУТКИ ТИТРОВ
# ============================================================

transform credits_viewport_scroll:
    yoffset 900                    # начальное смещение (титры начинаются снизу)
    linear 50.0 yoffset -1500      # финальное смещение (титры уходят вверх)


# ============================================================
# CITY N98 — END CREDITS
# ============================================================

screen city98_credits():

    modal True
    zorder 1000
    on "show" action Play("music", "audio/menu.mp3")
    on "hide" action Stop("music")


    # Фон
    add "images/city.png":
        xsize 1920
        ysize 1080

    add Solid("#06151B"):
        alpha 0.78


    # =========================================================
    # ПРОКРУЧИВАЕМЫЕ ТИТРЫ
    # =========================================================

    viewport at credits_viewport_scroll:
        xpos 420
        ypos 165
        xsize 1080
        ysize 1500
        mousewheel False
        draggable False
        scrollbars None

        vbox:
            xsize 1080
            xalign 0.5
            spacing 35

            # -------------------------------------------------
            # ЗАГОЛОВОК
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 8

                text "CITY N98":
                    xalign 0.5
                    style "menu_title"

                text "N98-7F / FINAL SYSTEM LOG":
                    xalign 0.5
                    style "menu_subtitle"

            null height 35

            # -------------------------------------------------
            # РАЗРАБОТКА
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 5

                text "РАЗРАБОТКА":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Anarsve":
                    xalign 0.5
                    color "#B7B9BB"
                    size 23

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # СЦЕНАРИЙ
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 5

                text "СЦЕНАРИЙ":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Anarsve":
                    xalign 0.5
                    color "#B7B9BB"
                    size 23

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # ДИЗАЙН ИНТЕРФЕЙСА
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 5

                text "ДИЗАЙН ИНТЕРФЕЙСА":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Anarsve":
                    xalign 0.5
                    color "#B7B9BB"
                    size 23

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # ГРАФИКА
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 5

                text "ГРАФИКА":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Anarsve":
                    xalign 0.5
                    color "#B7B9BB"
                    size 23

                # text "Микко":
                #     xalign 0.5
                #     color "#B7B9BB"
                #     size 23

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # МУЗЫКА И ЗВУК
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 5

                text "МУЗЫКА И ЗВУК":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Anarsve":
                    xalign 0.5
                    color "#B7B9BB"
                    size 23

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # ПЕРЕВОД
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 5

                text "ПЕРЕВОД НА АНГЛИЙСКИЙ":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Anarsve":
                    xalign 0.5
                    color "#B7B9BB"
                    size 23

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # ТЕСТИРОВАНИЕ
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 5

                text "ТЕСТИРОВАНИЕ":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Anarsve":
                    xalign 0.5
                    color "#B7B9BB"
                    size 23

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # ОСОБАЯ БЛАГОДАРНОСТЬ
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 8

                text "ОСОБАЯ БЛАГОДАРНОСТЬ":
                    xalign 0.5
                    color "#00B8ED"
                    size 24

                text "Всем, кто верил в проект":
                    xalign 0.5
                    color "#B7B9BB"
                    size 21

                text "и поддерживал нас на этом пути":
                    xalign 0.5
                    color "#B7B9BB"
                    size 21

            add Solid("#063542"):
                xsize 420
                ysize 1
                xalign 0.5

            # -------------------------------------------------
            # ФИНАЛ
            # -------------------------------------------------
            vbox:
                xalign 0.5
                spacing 10

                text "СПАСИБО ЗА ИГРУ":
                    xalign 0.5
                    color "#00B8ED"
                    size 27

                text "Город живёт только благодаря тем,":
                    xalign 0.5
                    color "#B7B9BB"
                    size 21

                text "кто возвращается в него снова.":
                    xalign 0.5
                    color "#B7B9BB"
                    size 21

                null height 25

                text "Каждое решение влияет на судьбу персонажей.":
                    xalign 0.5
                    color "#B7B9BB"
                    size 21

                text "Переиграйте игру — и история может закончиться иначе.":
                    xalign 0.5
                    color "#B7B9BB"
                    size 21

                null height 25

                text "УВИДИМСЯ в Cтаром Центре.":
                    xalign 0.5
                    color "#C58A32"
                    size 20

                null height 300

    # =========================================================
    # КНОПКИ ВНИЗУ
    # =========================================================

    button:
        style "quick_button"
        xpos 45
        ypos config.screen_height - 40
        action [Hide("city98_credits"), Function(renpy.full_restart, label="start")]

        hbox:
            spacing 9
            yalign 0.5

            text _("НОВАЯ ИГРА"):
                style "quick_button_text"

    button:
        style "quick_button"
        xpos config.screen_width - 150
        ypos config.screen_height - 40
        action [Hide("city98_credits"), MainMenu(confirm=False)]

        hbox:
            spacing 9
            yalign 0.5

            text _("МЕНЮ"):
                style "quick_button_text"
                

label splashscreen:
    if not persistent.language_chosen:
        menu:
            "Выберите язык"

            "Русский":
                $ renpy.change_language(None)
                $ persistent.language_chosen = True

            "English":
                $ renpy.change_language("english")
                $ persistent.language_chosen = True

        # После выбора просто возвращаемся (это завершит splashscreen)
        return
    return