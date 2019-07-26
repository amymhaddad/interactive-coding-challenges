"""A template to determine if a number is a power of 2"""


class Solution(object):
    def is_power_of_two(self, val):
        if val <= 0 or val == None:
            return False

        return True if val % 2 == 0 else False


s = Solution()

print(s.is_power_of_two(1))
