class Girl:

    gender = 'female'

    def __init__(self, name):
        self.name = name

r = Girl('rachel')
s = Girl('stanky')

print(r.gender)
print(s.gender)