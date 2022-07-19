def double (number):
    return number * 2


new_number = double(5)


def caps_strings (letter):
    return letter.upper()

my_letter = caps_strings('say hello')
print(my_letter)

names = ['nick', 'Jane', 'sara']

for name in names:
    print(caps_strings(name))