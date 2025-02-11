def find_letter_in_list(arr, letter, index):
    """
    Find the index of a letter in a list.
    :param arr: list of letters
    :param letter: letter to find
    :param index: index of the letter
    :return: index of the letter
    """
    # If the list is empty, return None
    if len(arr) == 0:
        return None
    # If the first letter matches, return the index
    if arr[0] == letter:
        return index
    # Increase the index by 1
    index += 1
    # Remove the first letter from the list
    arr.pop(0)
    # Call the function again with the rest of the list
    return find_letter_in_list(arr, letter, index)


def check_if_word_in_cards(cards, word):
    """
    Check if a word can be made from a list of letters.
    :param cards: list of letters
    :param word: word to check
    :return: True if we can make word from the list of letters, else False
    """
    # If the word is empty, return True
    if word == "":
        return True
    # Find the index of the first letter in the list
    letter_index = find_letter_in_list(cards.copy(), word[0], 0)
    # If the letter is found, remove it and check the rest of the word
    if letter_index is not None:
        cards.pop(letter_index)
        return check_if_word_in_cards(cards.copy(), word[1:])
    # If the letter is not found, return False
    return False


# return the score for the longest word that we can create
def create_words_recursive(cards, words, max_value, max_value_word):
    """
    Find the word with the max value that can be made from the cards. (but all the recursive calls are done in this function)
    :param cards: list of letters
    :param words: dictionary of words and their values
    :param max_value: max value of the word
    :param max_value_word: the word with the max value
    :return: the word with the max value that can be made from the cards
    """
    words=words.copy()
    # If there are no more words, return the word with the max value
    if len(words) == 0:
        return max_value_word
    # Take one word and its value from the dictionary
    word, value = words.popitem()
    if check_if_word_in_cards(cards.copy(), word):
        if max_value == None or max_value < value:
            max_value_word = word
            max_value = value
    return create_words_recursive(cards, words, max_value, max_value_word)


def create_words(words, cards):
    """
    Find the word with the max value that can be made from the cards.
    :param words: dictionary of words and their values
    :param cards: list of letters
    :return: the word with the max value that can be made from the cards
    """
    return create_words_recursive(cards, words, None, "")