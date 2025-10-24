def announce_players():
    players = input("Введите количество игроков: ")
    if players.isdigit():
        players_int = int(players)
        name_players = []
        for count in range(1, players_int + 1):
            while True:
                name = input(f"Введите имя игрока номер {count}: ")
                if name.isalpha():
                    name = name.capitalize()
                    print(f"Игрок {count}: {name.capitalize()}, мы приветствуем вас на капитал-шоу поле чудес!")
                    break
                else:
                    print("введено что-то неверно")
    else:
        print("Введенны неверные данные")


