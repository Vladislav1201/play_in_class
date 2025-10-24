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


"""def check_letter(secret_word, guessed, letter):
    letter = letter.lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Введите одну букву!")
        return guessed, False


    found = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed[i] = letter
            found = True

    if found:
        print("Есть такая буква!")
    else:
        print("Нет такой буквы!")

    return guessed, found


print("Вас приветствует капитал-шоу поле чудес")"""


announce_players()
























