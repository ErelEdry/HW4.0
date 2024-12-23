def find_letter_in_list(arr, letter, index):
    """
    Find the index of a letter in a list.
    """
    if len(arr) == 0:
        return None
    if arr[0] == letter:
        return index
    index += 1
    arr.pop(0)
    return find_letter_in_list(arr, letter, index)


def check_if_word_in_cards(cards, word):
    """
    Check if a word can be formed using the cards.
    """
    # iterate over the word and if the first letter of the work matches the current
    if word == "":
        return True
    letter_index = find_letter_in_list(cards.copy(), word[0], 0)
    if letter_index is not None:
        cards.pop(letter_index)
        return check_if_word_in_cards(cards.copy(), word[1:])
    return False


# return the score for the longest word that we can create
def create_words_recursive(cards, words, max_value, max_value_word):
    """
    Recursively find the word with the highest value that can be made from the cards.
    """
    # iterate over all the words and return the highest value
    words=words.copy()
    if len(words) == 0:
        return max_value_word
    word, value = words.popitem()
    if check_if_word_in_cards(cards.copy(), word):
        if max_value == None or max_value < value:
            max_value_word = word
            max_value = value
    return create_words_recursive(cards, words, max_value, max_value_word)


def create_words(words, cards):
    """
    Find the highest value word that can be made from the cards.
    """
    return create_words_recursive(cards, words, None, "")
