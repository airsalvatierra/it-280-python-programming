name = input('Hello, what is your name? ')

while not isinstance(name, str) or name.isdigit():
    name = input('That wasn\'t a valid text. Please enter your name ')

city = input('Where are you from? ')

while not isinstance(city, str) or city.isdigit():
    city = input('That wasn\'t a valid text. Please enter where are you from ')

age = input('How old are you? ')

while not age.isdigit():
    age = input('That wasn\'t a valid age. Please enter your age in digits ')

print()
print('Hello Class')
print('My name is ' + name + '.')
print('I grew up in ' + city + '.')
print('I am ' + age + ' years old.')
