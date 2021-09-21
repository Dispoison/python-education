phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
# your code goes here
phonebook['Jake'] = 938273443
del phonebook['Jill']

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

text = 'Coca-Cola'


def number_of_chars(text):
    chars = dict()
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars


print(number_of_chars(text))

print(dict([(0, 'first'), (1, 'second'), (2, 'third')]))
print({key: value for key, value in enumerate(text)})