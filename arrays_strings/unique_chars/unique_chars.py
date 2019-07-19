# One way to solve: use for loop and iterate
class UniqueChars(object):
    def has_unique_chars(self, string):

        if string == None:
            return False

        else:
            repeats = ""
            for letter in string.lower():
                if letter in repeats:
                    return False
                else:
                    repeats += letter
            return True

# Second way: set()
class UniqueChars(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        return bool(len(string) == len(set(string)))


# Third way: add letters to empty set
class UniqueChars(object):
    def has_unique_chars(self, string):

        if string == None:
            return False

        else:
            repeats = set()
            for letter in string.lower():
                if letter in repeats:
                    return False
                else:
                    repeats.add(letter)
            return True


# Fourth way: iterate without a data structure
class UniqueChars(object):
    def has_unique_chars(self, string):
        if string == None:
            return False
        for i, letter in enumerate(string.lower()):

            next_letter = string[i + 1 : i + 2 : 1]
            if string[i] == next_letter:
                return False
        return True

# Fifth way: code credit for this last solution: Donne Martin
class UniqueCharsInPlace(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True
