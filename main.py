import random

def player_one():  # ввожу и проверяю первого игрока
    while True:
        name_one = input("Введите имя первого игрока: ").capitalize()
        if name_one.isalpha():
            return name_one
        else:
            print("Некорректное имя первого игрока, введите повторно")

def player_two():  # ввод и проверка для втрого игрока
    while True:
        name_two = input("Введите имя второго игрока: ").capitalize()
        if name_two.isalpha():
            return name_two
        else:
            print("Некорректное имя второго игрока, введите повторно")

def player_three():  # ввод и проверка для третьего игрока
    while True:
        name_three = input("Введите имя третьего игрока: ").capitalize()
        if name_three.isalpha():
            return name_three
        else:
            print("Некорректное имя третьего игрока, введите повторно")

def guess_word_func(name, count, word, player_guess_word):  # функция проверяющая введенные буквы
    while True:
        print(f"{name} - введите вашу букву или попробуйте угадать слово: ")
        input_letter = input().strip().lower()
        if input_letter.isalpha():
            letter = input_letter
            break
        else:
            print('Введите букву или слово корректно (только буквы)')
    global tries
    tries += 1
    if letter == word:
        print(f"{name} - вы отгадали слово: {word}")
        count = count + 500
        # print(f"У вас {count} баллов")
        return count, True

    if letter in word and letter not in player_guess_word:
        print(f"{name} верно, есть такая буква")

        # print(player_guess_word)
        for i in range(len(word)):
            if word[i] == letter:
                player_guess_word[i] = letter
                count += 100
                print(f"{player_guess_word}")

        print(f"У вас {count} баллов"
              f"\n")

    else:
        print(f"{name} - увы но такой буквы нет")
        count = count - 10
        print(f"У вас {count} баллов")
        print(f"{player_guess_word}"
              f"\n")

    if "_" not in player_guess_word:
        print(f"{name} у вас {count} баллов")
        print(f"Слово {word} угаданно")
        return count, True
    return count, False

def choice_words(words):
    with open(words, "r") as dict_words:
        inform = dict_words.read().splitlines()
    line_random = random.choice(inform)
    word_split = line_random.split(":")
    word = word_split[0].strip()
    clue = word_split[1].strip()
    return word, clue

def determine_winner(count_one, count_two, count_three):
    max_score = max(count_one, count_two, count_three)
    if count_one == max_score:
        print(f'{name_player_one} ВЫИГРЫВАЕТ со счетом - {count_one}')
    elif count_two == max_score:
        print(f'{name_player_two} ВЫИГРЫВАЕТ со счетом - {count_two}')
    elif count_three == max_score:
        print(f'{name_player_three} ВЫИГРЫВАЕТ со счетом - {count_three}')
    else:
        print('Победила дружба')


name_player_one = player_one()
name_player_two = player_two()
name_player_three = player_three()


print("\nПриветствуем вас на игре 'Поле Чудес'. В игре принимают участие 3 игрока."
      "\nДля всех игроков выводится подсказка с описанием слова, которое нужно отгадать."
      "\nКаждый игрок по очереди называет букву. Если буква в слове есть, "
      "\nто она появляется под соответсвующим номером в загаданном слове и игроку начисляются баллы."
      "\nЕсли буквы нету, то баллы отнимаются. Побеждает игрок с наибольшим количеством баллов"
      "\nПриятной игры!"
      "\n")


all_names = [name_player_one, name_player_two, name_player_three]
print(f"Приглашаем к столу наших игроков: {name_player_one}, {name_player_two}, {name_player_three}."
      f"\n")
word, clue = choice_words("words.txt")
print(f"Задание на игру: "
      f"\n{clue}")
print(f"В данном слове {len(word)} букв(ы)")
print(f"Игроки, на угадывание вам дается 10 попыток!")
player_guess_word = ['_'] * len(word)
print(f"Загаданное слово: {player_guess_word}"
      f"\n")


count_one = count_two = count_three = 0
is_game_over = False
max_tries = 10
tries = 0


while not is_game_over:
    count_one, game_over = guess_word_func(name_player_one, count_one, word, player_guess_word)
    if game_over or tries >= max_tries:
        break
    count_two, game_over = guess_word_func(name_player_two, count_two, word, player_guess_word)
    if game_over or tries >= max_tries:
        break
    count_three, game_over = guess_word_func(name_player_three, count_three, word, player_guess_word)
    if game_over or tries >= max_tries:
        break


if tries >= max_tries:
    print('Попытки закончились, игроки, вы проиграли')
else:
    determine_winner(count_one, count_two, count_three)


print(f"{name_player_one}, {name_player_two}, {name_player_three} спасибо вам за участие в игре!")
print("Подарки для игроков в студию!")
