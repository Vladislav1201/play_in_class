import random

def choise_words(words):
    try:
        with open(words, "r") as dict_words:
            inform = dict_words.read().splitlines()
    except FileNotFoundError:
        print("файл не получилось открыть ")
        return None

    line_random = random.choice(inform)
    word = line_random.split(":")
    left_part = word[0].strip()
    right_part = word[1].strip()
    return left_part, right_part



word, clue = choise_words("words.txt")

print("Подсказка:", clue)