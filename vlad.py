word = "карп"

def announce_players():
        players_int = 2

        for count in range(1, players_int + 1):
            while True:
                name = input(f"Введите имя игрока номер {count}: ")
                if name.isalpha():
                    name = name.capitalize()
                    print(f"Игрок {count}: {name.capitalize()}, мы приветствуем вас на капитал-шоу поле чудес!")
                    break
                else:
                    print("введено что-то неверно")

count_first = 0
count_second = 0


def func_luck(x, arr, count):
    if x in arr:
        count += 10
    else:
        count -= 5
    if x == word:
        is_word_true = True
        print(f"Player wins ")
    return count


announce_players()
is_word_true = False
while not is_word_true:
    a = input('first_name: ')
    func_luck(a, word, count_first)
    count_first = func_luck(a, word, count_first)
    print(f"Your current points: {count_first}")

    b = input('second_name: ')
    func_luck(b, word, count_second)
    count_second = func_luck(a, word, count_second)
    print(f"Your current points: {count_second}")

