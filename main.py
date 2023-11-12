import random

def gen_random_word(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    random_number = random.randint(1, len(data))
    word = data[random_number]
    return word

def generate_guess_template():
    random_word = gen_random_word('data.txt')
    final_guess = []
    if len(random_word) > 1:
        for i in range(len(random_word)):
            final_guess.append('_')
    else:
        final_guess.append('_')
    print('_' * len(random_word))
    return {'final_guess': final_guess,
            'random_word': random_word}


def hangman_game(guess_template):
    got = False
    won = True
    final_guess = guess_template.get('final_guess')
    word = guess_template.get('random_word')
    counter = 10
    while won and counter != 0:
        guess = input(f"Enter a guess, you have {counter} guesses remaining\n").lower()
        list_word = list(word)
        if guess not in list_word:
            counter -= 1
        if guess == word:
            print("You got it")
            got = True
            break
        for i, j in enumerate(word):
            if guess == j:
                final_guess[i] = j
                final_guess = ''.join(final_guess)
                if final_guess == word:
                    print("You got it!")
                    won = False
                else:
                    final_guess = list(final_guess)
        print(''.join(final_guess))
    if got is False:
        print(f"Nice try, it was {word}")


hangman_game(generate_guess_template())
