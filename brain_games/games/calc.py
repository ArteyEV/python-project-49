import random

MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = ('+', '-', '*')


def calculate(first_number, second_number, operation):
    match operation:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number


def generate_round():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)
    question = f'{first_number} {operation} {second_number}'
    correct_answer = str(calculate(first_number, second_number, operation))
    return question, correct_answer