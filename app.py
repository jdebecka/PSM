import math
import re


def factorial_function(number):
    if number == 1:
        return number
    return number * factorial_function(number - 1)


def degree_to_radians(angle_degree):
    return angle_degree / 180


def shift_to_appropriate_range(angle):
    return math.fmod(angle, 2)


def operation_calculation(operation_defined, a, b):
    if operation_defined == '*':
        return a * b
    else:
        return a / b


def return_one_rotation(angle_rotation):
    if angle_rotation <= 2:
        return angle_rotation
    else:
        return shift_to_appropriate_range(angle_rotation)


def calculate_sin_equation(current_sin, loop_number):
    return current_sin ** loop_number / factorial_function(loop_number)


def calculate_sin(angle_x):
    sign_negative = True
    sin_of_x = angle_x
    print(f'''n: 0. sin(x) = {sin_of_x}''')

    for i in range(3, 19, 2):
        if sign_negative:
            sin_of_x -= calculate_sin_equation(angle_x, i)
            sign_negative = False
        else:
            sin_of_x += calculate_sin_equation(angle_x, i)
            sign_negative = True

        print(f'''n: {i}. sin(x) = {sin_of_x}''')


prompt = '''Input in radians should contain \'pi\'
Input angle to calculate sin(x): '''

userInput = input(prompt)
angleRadians: float

if re.search('pi', userInput, re.IGNORECASE):
    first_number = re.findall('\\d+', userInput)
    operation = re.findall('\\W', userInput)
    if re.match('pi', userInput, re.IGNORECASE):
        first_number.insert(0, 1)

    if not operation:
        angleRadians = return_one_rotation(int(first_number[0]))
    else:
        angleRadians = return_one_rotation(operation_calculation(operation, int(first_number[0]), int(first_number[1])))
else:
    angleRadians = return_one_rotation(degree_to_radians(int(userInput)))
    
print(f"Build in function. sin(x): {math.sin(angleRadians * math.pi)}")
calculate_sin(angleRadians * math.pi)

