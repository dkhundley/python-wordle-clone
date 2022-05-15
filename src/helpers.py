def compare_words(guess_word, actual_word):
    '''
    Comparing the word guessed by the person to the actual word for correctness

    Args:
        - guess_word (str): The word guessed by the person
        - actual_word (str): The actual word the person is trying to solve for

    Returns:
        - final_result (str): A list of properly colored emojis indicating level of correctness
    '''

    # Creating lists of letters from each of the respective "actual" and "guess" words
    actual_letters = list(actual_word)
    guess_letters = list(guess_word)

    # Creating a dictionary that holds how many remaining letters are necessary for the actual answer
    remaining_letters_dict = {}
    for letter in actual_letters:
        if letter not in remaining_letters_dict.keys():
            remaining_letters_dict[letter] = 1
        else:
            remaining_letters_dict[letter] += 1


    # Performing logic to check for precise matches
    for index in range(len(guess_letters)):
        if actual_letters[index] == guess_letters[index]:
            guess_letters[index] = '🟩'
            remaining_letters_dict[actual_letters[index]] -= 1

    # Performing logic to check for any remaining letters that might be right but not in right spot
    for index in range(len(guess_letters)):

        # Skipping over letters that have already been properly verified
        if guess_letters[index] == '🟩':
            continue

        # Performing appropriate action if guess letter is not at all in the actual word
        elif guess_letters[index] not in remaining_letters_dict.keys():
            guess_letters[index] = '⬜️'

        # Performing appropriate action if guess letter's key is in remaining_letters_dict but no remaining slots are open
        elif (guess_letters[index] in remaining_letters_dict.keys()) and (remaining_letters_dict[guess_letters[index]] <= 0):
            guess_letters[index] = '⬜️'

        # Performing appropriate action where letter is correct but not in proper position
        elif (guess_letters[index] in remaining_letters_dict.keys()) and (remaining_letters_dict[guess_letters[index]] >= 1):
            remaining_letters_dict[guess_letters[index]] -= 1
            guess_letters[index] = '🟨'

    # Joining together the list of altered "guess letters" as a single string for the final result
    final_result = ''.join(guess_letters)

    return final_result