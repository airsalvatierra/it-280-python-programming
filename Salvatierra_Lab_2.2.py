from math import pi

def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def get_area_from_a_circle_from_diameter():
    diameter = input('Enter the diameter: ')
    while not is_float(diameter):
        diameter = input('That wasn\'t a valid number, enter the diameter: ')

    area = 0.25 * pi * float(diameter) * 2

    print(f'The area is {area}')

def get_vehicle_mpg():
    traveled_distance = input('Enter the traveled distance: ')
    while not is_float(traveled_distance):
        traveled_distance = input(
            'That wasn\'t a valid number, enter the traveled distance: '
        )

    fuel_used = input('Enter fuel used: ')
    while not is_float(fuel_used):
        fuel_used = input('That wasn\'t a valid number, enter the fuel used: ')

    mpg = float(traveled_distance) / float(fuel_used)

    print(f'The MPG is {mpg}')

def get_total_worked_hour_per_week():
    hours = []
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        current_day = input(f'Enter the hours worked on {day}: ')
        while not is_float(current_day):
            current_day = input(
                f'That wasn\'t a valid number, enter the right hours for '
                f'{day}: '
            )
        hours.append(float(current_day))
    total_worked_hours = sum(hours)
    print(f'The total worked hour is {total_worked_hours}')

def convert_fahrenheit_to_celsius():
    fahrenheit = input('Enter the fahrenheit temperature: ')
    while not is_float(fahrenheit):
        fahrenheit = input(
            'That wasn\'t a valid number, enter the fahrenheit: '
        )
    celsius = (float(fahrenheit) - 32) / 1.8

    print(f'The converted temperature to celsius is {celsius}')

def convert_celsius_to_fahrenheit():
    celsius = input('Enter the celsius temperature: ')
    while not is_float(celsius):
        celsius = input(
            'That wasn\'t a valid number, enter the celsius: '
        )
    fahrenheit = (float(celsius) * 1.8) + 32

    print(f'The converted temperature to fahrenheit is {fahrenheit}')

# Assign function to dictionary keys
options = {
    '1': get_area_from_a_circle_from_diameter,
    '2': get_vehicle_mpg,
    '3': get_total_worked_hour_per_week,
    '4': convert_fahrenheit_to_celsius,
    '5': convert_celsius_to_fahrenheit,
}

print('Fun calculator!')
print('Choose of the option: ')
print('1: Calculate the area from a circle giving the diameter')
print(
    '2: Calculate the MPG giving the distance traveled and the amount of '
    'fuel used'
)
print(
    '3: Calculate the total number of houres worked in a week, giving hours '
    'worked each day of the week'
)
print('4: Convert fahrenheit to celsius')
print('5: Convert celsius to fahrenheit')
chosen_option = input()
while chosen_option not in ['1', '2', '3', '4', '5']:
    chosen_option = input('Please select the right option: ')

# Call the mapped function
options[chosen_option]()
