import random

words_list = ["onomatopee", "animal", "abecedar", "spanzuratoarea"]
complete_word_list = []
wrong_letters = []

HANGMAN_PICS = [r'''
           +---+
               |
               |
               |
              ===''', r'''
           +---+
           O   |
               |
               |
              ===''', r'''
           +---+
           O   |
           |   |
               |
              ===''', r'''
           +---+
           O   |
          /|   |
               |
              ===''', r'''
           +---+
           O   |
          /|\  |
               |
              ===''', r'''
        +---+
        O   |
       /|\  |
       /    |
           ===''', r'''
        +---+
        O   |
       /|\  |
       / \  |
              ===''']

if __name__ == '__main__':
    selected_word = random.choice(words_list)
    mistakes = 0
    wrong_letters.append(selected_word[0])
    wrong_letters.append(selected_word[-1])

    for i in range(len(selected_word)):
        if selected_word[0] == selected_word[i]:
            complete_word_list.append(selected_word[0])
        elif selected_word[-1] == selected_word[i]:
            complete_word_list.append(selected_word[-1])
        else:
            complete_word_list.append('_')
    print(' '.join(complete_word_list))

    while 1:
        letter = input("Input letter: ")
        if letter in wrong_letters:
            print("You already entered that letter")
        elif not letter.isalpha():
            print("This is not a letter")
        elif letter in selected_word:
            for i in range(len(selected_word)):
                if letter == selected_word[i]:
                    complete_word_list[i] = letter
        else:
            print(HANGMAN_PICS[mistakes])
            mistakes += 1
            wrong_letters.append(letter)

        print(' '.join(complete_word_list))
        print(f"mistakes = {mistakes}")

        if complete_word_list.count('_') == 0:
            print("You won")
            break

        if mistakes == 7:
            print("You lost")
            break
