"""Reverse characters without using slicing or the reversed function"""

chars = ["f", "o", "o", " ", "b", "a", "r"]

# Use recursion to reverse characters
def reverse(chars):
    if chars is None:
        return None
    elif chars == []:
        return []
    return [chars[-1]] + reverse(chars[: len(chars) - 1])


# Use iteration to reverse characters
def reverse(chars):
    if chars:
        return [chars[-i - 1] for i, letter in enumerate(chars)]
