import random

MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10
HIDDEN_MARK = '..'


def generate_round():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = random.randint(0, length - 1)

    sequence = [start + index * step for index in range(length)]
    correct_answer = str(sequence[hidden_index])

    numbers = [
        HIDDEN_MARK if index == hidden_index else str(number)
        for index, number in enumerate(sequence)
    ]
    question = ' '.join(numbers)

    return question, correct_answer