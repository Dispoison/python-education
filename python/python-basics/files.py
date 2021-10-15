with open('some_text_file.txt') as file:  # read
    print(file.read(), '\n')

with open('some_text_file.txt') as file:  # read
    for line in file.readlines():
        print(line, end='')

# with open('some_text_file.txt', 'a') as file:  # append
#     file.write('text')

# with open('some_text_file.txt', 'w') as file:  # rewrite
#     file.write('rewrite text')
