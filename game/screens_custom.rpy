screen game_hud():
    zorder 100
    frame:
        xalign 0.02
        yalign 0.02
        background Frame("#00000080", padding=(15, 10))
        vbox:
            spacing 8
            text "День [current_day]" size 28
            text "💰 [money]$" size 28
            text "⚡ Действия: [actions]" size 28
            text "🔌 Провода: [wires]" size 28
            text "💾 Микросхемы: [chips]" size 28
            null height 10
            text "Активные заказы:" size 24 bold True
            for key, client in clients.items():
                if client.get("order_active", False):
                    $ mark = " ✔" if client.get("order_completed", False) else ""
                    $ client_name = client.get("name", key)
                    $ order_name = client.get("order_name", "")
                    text "  [client_name]: [order_name][mark]" size 22
                    