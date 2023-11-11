import random


def generate_array_task1(a, b):
    array = [random.randint(-255, 255) for _ in range(100)]

    positions_a = random.sample(range(100), 10)
    positions_b = random.sample(list(set(range(100)) - set(positions_a)), 20)

    for pos in positions_a:
        array[pos] = a

    for pos in positions_b:
        array[pos] = b

    array.sort()
    return array
