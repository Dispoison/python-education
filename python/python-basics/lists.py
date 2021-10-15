numbers = [1, 2, 3]
strings = ['hello', 'world']
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s\n" % second_name)

random_text = "It,h gIi nl ievhet  afmoo nsge rtuhtea ecr"

print(random_text[::2] + random_text[::-2])

just_list = [1, 2, 3, 5, 8, 13, 21, 34, 55]
print(*just_list)


def recursion(nums):
    if isinstance(nums, int):
        print(f'{" "*(len(just_list) + 1)}{nums}')
        return
    elif not nums:
        return

    if len(nums) == 3:
        first, middle, last = nums
    else:
        first, *middle, last = nums
    print(f'{" " * (len(just_list) - len(nums))}{first}{" "*(len(nums)*2)}{last}')
    return recursion(middle)


recursion(just_list)
