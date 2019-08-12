str1 = "aaabbcdd"
str2 = "abdbacade"

longer_string = ""
shorter_string = ""

if len(str1) < len(str2):
    shorter_string += str1
    longer_string += str2
else:
    shorter_string += str2
    longer_string += str1


def unique_string(longer_string, shorter_string):
    """Find the unique character in a string"""

    compare_string = longer_string[: len(shorter_string)]
    for i, letter in enumerate(compare_string):
        if sorted(compare_string) == sorted(shorter_string):
            return longer_string[-1]

        elif shorter_string[i] != compare_string[i]:
            return letter


print(unique_string(longer_string, shorter_string))
