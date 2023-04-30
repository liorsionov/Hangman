HANGMAN_ASCII_ART = "Welcome to the game Hangman\n" + """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

MAX_TRIES = 6

print(HANGMAN_ASCII_ART, "\n", 'You have '+str(MAX_TRIES)+' tries to guess')


def main():
    """This is the main function , this function make all other functions co-operate and make the game run
    old_letters_guessed: it holds the letters the player already entered(legal letters only)
    counter: holds the counting of the tries the player played(if player makes incorrect the counter go +1
    letter_guessed: the letter inputed by the player
    :returns: if the player won or lose
    :rtype: str
    """
    secret_word = choose_word()
    print("Let's start!")
    print(print_hangman(1))
    print(len(secret_word) * "_ ")
    old_letters_guessed = []
    counter = 1
    while check_win(secret_word, old_letters_guessed) == False:
        letter_guessed = input('Enter a letter: ')
        if check_win(secret_word, old_letters_guessed):
            break
        if not letter_guessed.isalpha() or not len(letter_guessed) == 1:
            print('X')
            continue
        if letter_guessed in secret_word:
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
            print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            if letter_guessed in old_letters_guessed:
                print("X")
                print(show_hidden_word(secret_word, old_letters_guessed))
                continue
            print(':(')
            counter += 1
            print(print_hangman(counter))
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
            print(show_hidden_word(secret_word, old_letters_guessed))
            if counter == MAX_TRIES + 1:
                break
    if counter < MAX_TRIES or check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print('LOSE')


def choose_word():
    """this functions takes from player the file path and index number that will give the player word from the file
    file_path: player inputs the file path
    :type: file.txt
    index: player inputs the index
    :type: int
    :returns CHOSEN_WORD: the word that got from the file_path
    :rtype: str
    """
    import os
    file_path = input("Enter file path: ")
    while not os.path.isfile(file_path):
        print("this file does not exict, try again")
        file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    with open(file_path, "r") as tem:
        original = tem.read().split(" ")
        if len(original) != index:
            i = (index - 1) % len(original)
            number = i
        else:
            number = index - 1
        CHOSEN_WORD = original[number]
        return CHOSEN_WORD


def print_hangman(num_of_tries):
    """ this func will show you the picture of the Hangman with the number of tries you have done
    :param num_of_tries: the number of tries
    ":type: int
    :return: the picture of the hangman
    :rtype: dict
    """
    HANGMAN_PHOTOS = {
     1: "    x-------x",
     2: """    x-------x
    |
    |
    |
    |
    |""",
     3: """    x-------x
    |       |
    |       0
    |
    |
    |""",
     4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
     5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
     6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
     7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""",
    }
    return HANGMAN_PHOTOS[num_of_tries]


def check_valid_input(letter_guessed, old_letters_guessed):
    """ this function checks if the word enterd by the player is valid or not.
    :param letter_guessed: the letter that the player guessed:
    :type: str
    :param old_letters_guessed: the list of letters that the player already inputed
    :type : list
    :returns: if the letter True
    """
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and not letter_guessed.lower() in old_letters_guessed:
        return True


def the_printed_list(my_list):
    """this function will show the player what words he already tried
    :param my_list: the list of letters in this list
    :type: list
    :returns: the list in format
    :rtype: str
    """
    return ' -> '.join(my_list)


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """this function checks if the function check_valid_input() == True, if it does so the function will append
    the letter to list, if the function isn't True the function will show the player what letters already entered
    with the function the_printed_list()
    :param letter_guessed: the letter that inputed by the player
    :type: str
    :param old_letters_guessed: the letters that already inputed by the player
    :type: list
    :returns: append the letter to the list or print the list
    :rtype: list or str
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        return old_letters_guessed.append(letter_guessed.lower())
    else:
        print(the_printed_list(old_letters_guessed))


def show_hidden_word(secret_word, old_letters_guessed):
    """ this function will give you a string of the secret word with the words that exist in old_letters_guessed
    and the words that don't exist it will appear as "_ "
    :param secret_word: the word you enter
    :type: str
    :param old_letters_guessed: the letters you already guessed
    :type: str
    :return: the result
    :rtype: str
    """
    result = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            result += letter + ' '
        else:
            result += "_ "
    return result[:-1]


def check_win(secret_word, old_letters_guessed):
    """this function will check if the letters in old_letters guessed combine the secret word
    :param secret_word: the word that the player has to guess
    :type: str
    :param old_letters_guessed: the list of leters that the player already inputed
    :type: list
    :returns: if result equals to the secret_word
    :rtype: True or False
    """
    result = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            result += letter
    if result == secret_word:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
