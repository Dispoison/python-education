import re
find_members = [func_name for func_name in dir(re) if 'find' in func_name]
find_members.sort()
print(find_members)
