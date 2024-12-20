from typing import Dict


def find_letter_in_list(arr: list[str], letter: str, index: int) -> int | None:
    """finds if a letter is in a list

    Args:
        arr (list[str]): array to find the letter
        letter (str): letter to find
        letter (int): current index

    Returns:
        int | None: index if found None if not
    """
    if len(arr) == 0:
        return None
    if arr[0] == letter:
        return index
    index += 1
    arr.pop(0)
    return find_letter_in_list(arr, letter, index)


def check_if_word_in_cards(cards: list[str], word: str) -> int:
    # iterate over the word and if the first letter of the work matches the current
    if word == "":
        return True
    letter_index = find_letter_in_list(cards, word[0], 0)
    if letter_index is not None:
        return check_if_word_in_cards(cards, word[1:])
    return False


# return the score for the longest word that we can create
def create_word_recursive(
    cards: list[str], words: Dict[str, int], max_value: int | None, max_value_word: str
) -> str:
    # iterate over all the words and return the highest value
    if len(words) == 0:
        return max_value_word
    word, value = words.popitem()
    if check_if_word_in_cards(cards.copy(), word):
        if max_value == None or max_value < value:
            max_value_word = word
            max_value = value
    return create_word_recursive(cards, words, max_value, max_value_word)


def create_word(cards: list[str], words: Dict[str, int]) -> str:
    return create_word_recursive(cards, words, None, "")


cards = ["h", "e", "l", "o", "t", "i", "s", "w", "r", "d"]
words = {"hi": 1, "hello": 40, "world": 10, "this": 4, "a": 6, "test": 7}

print(create_word(cards, words))
