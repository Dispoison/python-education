data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%f"

print(format_string % data)

from string import Template

print('Hello ' + 'World!')
hello_str = 'Hello'
world_str = 'World'
print('{} {}!'.format(hello_str, world_str))
print(f'{hello_str} {world_str}!')
print(f'%s %s!' % (hello_str, world_str))

template = Template('$hello $world!')
print(template.substitute(hello=hello_str, world=world_str))
