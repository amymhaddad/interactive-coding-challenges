"""A program that compresses a string (ie, 'AAABCCDDDD' becomes 'A3BC2D4') only if the compressed string saves space."""


def shortest_string(string):
    """
    Return the shortest string: the compressed string or the given string.
    """

    if len(compress_string(string)) < len(string):
        return compress_string(string)
    return string


def compress_string(string):
    """Create a new, compressed string that contains the letter and the number of times it's repeated"""

    compressed_string = ""
    for letter in list_repeated_and_unique_letters(string):
        number_repeated_letters = len(letter)
        if number_repeated_letters == 1:
            compressed_string += letter
        else:
            compressed_string += letter[1] + str(number_repeated_letters)
    return compressed_string


def list_repeated_and_unique_letters(string):
    """Iterate through a given string and identify the repeated and unique letters"""

    letters_and_count = []
    repeated_letters = ""

    for letter in string:

        if not repeated_letters:
            repeated_letters += letter

        elif letter in repeated_letters:
            repeated_letters += letter

        else:
            letters_and_count.append(repeated_letters)
            repeated_letters = letter

    letters_and_count.append(repeated_letters)
    return letters_and_count
