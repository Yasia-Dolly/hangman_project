import random
word_list = []
with open('russian_words', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.strip()
        word_list.append(word)
secret_word = random.choice(word_list)
guessed_letters = []
remaining_attempts = 6
wrong_letters = []
stages = [
        """
        ------
        |    |
        |    0
        |   /|\\
        |   / \\
        |
        """,
        """
        ------
        |    |
        |    0
        |   /|\\
        |   / 
        |
        """,
        """
        ------
        |    |
        |    0
        |   /|\\
        |   
        |
        """,
        """
        ------
        |    |
        |    0
        |   /|
        |  
        |
        """,
        """
        ------
        |    |
        |    0
        |    |
        |
        |
        """,
        """
        ------
        |    |
        |    0
        |
        |
        |
        """,
        """
        ------
        |    |
        |   
        |
        |
        |
        """
    ]
print("Добро пожаловать в игру Виселица!")
print(f"Загадано слово из {len(secret_word)} букв. У вас есть {remaining_attempts} попыток.")
while remaining_attempts > 0:
    print(stages[remaining_attempts])
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append('_')
    print("Слово:", ' '.join(display))
    print("Осталось попыток:", remaining_attempts)
    print("Неверные буквы:", ', '.join(wrong_letters))
    guess = input("Введите букву: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Нужно ввести одну букву!")
        continue
    if guess in guessed_letters or guess in wrong_letters:
        print("Вы уже вводили эту букву!")
        continue
    if guess in secret_word:
        guessed_letters.append(guess)
        print("Правильно!")
        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break
        if all_guessed:
            print("Поздравляем! Вы выиграли!")
            print("Загаданное слово было:", secret_word)
            break
    else:
        wrong_letters.append(guess)
        remaining_attempts -= 1
        print("Неправильно!")
if remaining_attempts == 0:
    print(stages[0])
    print("Игра окончена! Вы проиграли.")
    print("Загаданное слово было:", secret_word)