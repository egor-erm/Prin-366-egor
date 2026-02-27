import random

words = ['программа', 'компьютер', 'телефон', 'солнце', 'река']
word = random.choice(words)

try_left = 5          # попытки
guesses = ''          # строка со всеми названными буквами
finish_word = ''      # текущее отображаемое состояние слова

print('Это Виселица')
print(f'Угадай слово (длина: {len(word)}) - у тебя {try_left} попыток\n')


def assemble_word(): # создать текущую отображаемую версию загаданного слова
    finish_word = ''
    for later in word:
        if later in guesses:
            finish_word += later
        else:
            finish_word += '_'
    return  finish_word


while try_left > 0:

    finish_word = assemble_word() # собираем finish_word
    print('Слово:', ' '.join(finish_word))

    if guesses:
        print('Буквы:', ' '.join(guesses))

    print(f'Попыток осталось: {try_left}')
    later = input('Буква: ').lower()

# -------------- проверки --------------
    if len(later) != 1 or not later.isalpha():
        print('Нужна одна буква')
        continue

    if later in guesses:
        print('уже была')
        continue

    guesses += later

    if later not in word:
        try_left -= 1
        print('Нет такой буквы')

# ---------------------------------------

    finish_word = assemble_word()

    if finish_word == word:
        print('Вы угадали слово : ', word.upper())
        break

if try_left==0:
    print('Попытки закончились... Слово было : ', word)

print('Конец игры')


