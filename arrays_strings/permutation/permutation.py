# Solution 1: use set() to see if one string is a permutation of another
class Permutations(object):
    def is_permutation(self, str1, str2):
        return bool(set(str1) == set(str2))


# Solution 2: use a for loop
def is_permutation(str1, str2):
    if None:
        return False
    matched_letters = [char for char in str1 if char in str2]
    if (len(matched_letters) == len(str2)) and (len(str1) == len(matched_letters)):
        return True
    return False


# Solution 3: Use sorted() and convert the strings to a list
def is_permutation(str1, str2):
    if str1 is None or str2 is None:
        return False
    return sorted(list(str1)) == sorted(list(str2))


# Solution 4: Use dictionaries
def is_permutation(str1, str2):
    if str1 is None or str2 is None:
        return False
    return count_string_characters(str1, str2)


def count_string_characters(str1, str2):
    """
    Return a dictionary for each string:
    keys are the characters; values are the number of repetitions
    """
    letters_and_count_str1 = {}
    letters_and_count_str2 = {}

    for char in str1:
        letters_and_count_str1[char] = letters_and_count_str1.get(char, 0) + 1

    for char in str2:
        letters_and_count_str2[char] = letters_and_count_str2.get(char, 0) + 1

    return letters_and_count_str1 == letters_and_count_str2
