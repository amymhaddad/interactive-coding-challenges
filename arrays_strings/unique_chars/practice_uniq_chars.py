class UniqueChars(object):
    def __init__(self, string):
        self.string = string
    
    def determine_if_unique(self):
        if self.string is None:
            return False
        return len(set(self.string)) == len(self.string)

s = UniqueChars('gem')

print(s.determine_if_unique())