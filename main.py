import random


def player_one(): #ввожу и проверяю первого игрока
    while True:
        name_one = input("Введите имя первого игрока: ").capitalize()
        if name_one.isalpha():
            return name_one
        else:
            print("Некорректное имя первого игрока")


def player_two(): # ввод и проверка для втрого игрока
    while True:
        name_two = input("Введите имя второго игрока: ").capitalize()
        if name_two.isalpha():
            return name_two
        else:
            print("Некорректное имя второго игрока")

def player_three(): #ввод и проверка для третьего игрока
    while True:
        name_three = input("Введите имя третьего игрока: ").capitalize()
        if name_three.isalpha():
            return name_three
        else:
            print("Некорректное имя третьего игрока")

def func_luck(name, count): #изменил чуть программу.
    """пользователь вводит букву или слово и далее смотрю соответсвкет ли это
    загаданному слову, если да то выводиья что угалали слово,
    если букву то пишу что букву угадали, если нет,то пишу что
    нет такой буквы и проверяю есть ли подчеркивания"""
    print(f"{name} введите вашу букву или попробуйте угадать слово")
    letter = input()

    if letter == word:
        print(f"{name} - вы отгадали слово: {word}")
        count = count + 500
        print(f"У вас {count} баллов")
        return count, True

    if letter in word:
        print(f"{name} верно, есть такая буква")
        count += 100
        for i in range(len(word)):
            if word[i] == letter:
                player_guess_word[i] = letter
                print(player_guess_word)
    else:
        print(f"{name} увы но такой буквы нету")
        print(player_guess_word)
        count = count - 10

    if "_" not in player_guess_word:
        print(f"{name} у вас {count} баллов")
        print(f"Слово '{word}' угаданно")
        return count, True
    print(f"{name} у вас {count} баллов")

    return count, False

def choise_words(words):
    with open(words, "r") as dict_words:
        inform = dict_words.read().splitlines()
    line_random = random.choice(inform)
    word_split = line_random.split(":")
    word = word_split[0].strip()
    clue = word_split[1].strip()
    return word, clue


word, clue = choise_words("words.txt")
print("Подсказка:", clue)

"""пока слово объявлено так, потом вывожу строчку с колисеством пробелов равную длинне загаданного слова
объявляю трех игроков, красиво приветсвую их и пишу цикл который выполняется пока есть незаполненные нижние подчеркивания в строке"""

print(f"В загададаном слове {len(word)} букв(ы)")
player_guess_word = ['_'] * len(word)
print(f"Загаданное слово: {player_guess_word}")

name_player_one = player_one()
name_player_two = player_two()
name_player_three = player_three()
all_names = [name_player_one, name_player_two, name_player_three]
print(f"Под аплодисменты зрительного зала, тройка игроков в студию: {name_player_one}, {name_player_two}, {name_player_three}")

count_one = count_two = count_three = 0
is_game_over = False

while not is_game_over:
    count_one, game_over = func_luck(name_player_one, count_one)
    if game_over:
        break
    count_two, game_over = func_luck(name_player_two, count_two)
    if game_over:
        break
    count_three, game_over = func_luck(name_player_three, count_three)
    if game_over:
        break



print("От первого канала подарки тройке игроков в студию")