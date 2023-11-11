from ArrayGenerator.Task1Generator import generate_array_task1
from InputHelper.InputChecker import get_user_input


def calculate_sum_between(array, a, b):
    start, end = min(a, b), max(a, b)
    indices_between = [i for i, val in enumerate(array) if start <= val <= end]
    sum_between = sum(array[i] for i in indices_between)
    return sum_between


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)

sum_between_values = calculate_sum_between(result_array, a_value, b_value)
print(f"Sum of values between {a_value} and {b_value}: {sum_between_values}")