def can_form_word(word, cards):
    """
    Check if a word can be formed using the given cards
    """
    cards_count = {}
    # Count the occurrences of each card
    for card in cards:
        if card in cards_count:
            cards_count[card] += 1
        else:
            cards_count[card] = 1
    # Check if the word can be formed with the cards
    for char in word:
        if char not in cards_count or cards_count[char] == 0:
            return False
        cards_count[char] -= 1
    return True

def create_words_recursive(words, cards, max_score, best_word):
        if len(words) == 0:
            return max_score, best_word
        word = list(words.keys())[0]
        remaining_words = dict(list(words.items())[1:])
        # Check if the word can be formed with the cards
        if can_form_word(word, cards):
            score = words[word]
            # Update the max score and best word if the current word has a higher score
            if score > max_score:
                max_score = score
                best_word = word
        return create_words_recursive(remaining_words, cards, max_score, best_word)
def create_words(words, cards):
    """
    Get the highest word score with our letters cards
    """
    max_score, best_word = create_words_recursive(words, cards, 0, None)
    # Return the best word or an empty list if no word can be formed
    return [best_word] if best_word else []

words = {'hi': 11, 'hello': 40, 'world': 10, 'this': 4, 'a': 6, 'test': 73}
cards = ['h', 'e', 'l', 'o', 't', 'i', 's', 'w', 'r', 'd']
print(create_words(words, cards))