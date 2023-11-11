import random


def generate_array(a, b):
    array = [random.randint(-255, 255) for _ in range(100)]

    positions_a = random.sample(range(100), 10)
    positions_b = random.sample(list(set(range(100)) - set(positions_a)), 20)

    for pos in positions_a:
        array[pos] = a

    for pos in positions_b:
        array[pos] = b

    array.sort()
    return array


a_value = random.randint(1, 254)
b_value = random.randint(1, 254)

result_array = generate_array(a_value, b_value)

print(f"Array: {result_array}")
print(f"a = {a_value}, b = {b_value}")
print(f"Positions of 'a': {[pos for pos in range(100) if result_array[pos] == a_value]}")
print(f"Positions of 'b': {[pos for pos in range(100) if result_array[pos] == b_value]}")
