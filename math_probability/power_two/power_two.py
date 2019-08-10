def is_power_of_two(val):
    """Return a boolean to determine if a valid number is a power of two"""
    if is_valid(val):
        if val == 1 or val % 2 == 0:
            return True
    return False


def is_valid(val):
    """Determine if a number is valid"""
    if val is None:
        raise TypeError("The value can't be None")
    elif not isinstance(val, int) or val == 0:
        return False

    return True


print(is_power_of_two(0))
