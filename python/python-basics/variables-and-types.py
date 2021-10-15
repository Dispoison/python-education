# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

number = 12345679 * 9
print(type(number), number)

number = 55 / 1.1
print(type(number), number, f'| Is equals 50 => {number == 50}\n')

some_text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'
print(*some_text)
print(f'"dolor" at index: {some_text.index("dolor")}\n')

another_text = """Oh, the night is my world
City light painted girl
In the day nothing matters
It's the night time that flatters
"""


another_text = another_text.split('\n')
rhymes = f'{another_text[0].split()[2]} - {another_text[1].split()[1]}\n'
rhymes += f'{another_text[2].split()[4]} - {another_text[3].split()[5]}\n'
print('Rhymes:')
print(rhymes)
