def print_upper_words(words):
    """Prints all the words in uppercase on a separate line"""
    for word in words:
        print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])


def print_e_words(words):
    """Print only the words that start with e in uppercase on separate lines"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


print_e_words(["hello", "hey", "evening", "yo", "every"])


def print_given_letter_words(words, given_letter):
    for word in words:
        for letter in given_letter:
            if word.startswith(letter):
                print(word.upper())


print_given_letter_words(
    ["hello", "hey", "goodbye", "yo", "yes"], given_letter=["h", "y"]
)
