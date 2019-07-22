"""A template to find prime numbers."""


class Primes(object):
    def check_prime(self, num):
        if (
            self.is_greater_than_one(num)
            and self.is_whole_number(num)
            and self.only_two_factors(num)
            and self.not_None(num)
        ):
            return f"Success: {num} is prime."
        return False

    def is_whole_number(self, num):
        if not isinstance(num, int):
            raise TypeError("This is not an integer.")
        return True

    def is_greater_than_one(self, num):
        if num < 2:
            raise ValueError("This number is less than 2.")
        return True

    def not_None(self, num):
        return num is not None

    def only_two_factors(self, num):
        factors = [i for i in range(1, num + 1) if num % i == 0]
        return len(factors) == 2
