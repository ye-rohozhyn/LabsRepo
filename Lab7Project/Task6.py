import matplotlib.pyplot as plt
import numpy as np
from ArrayGenerator.Task1Generator import generate_array_task1
from InputHelper.InputChecker import get_user_input


def calculate_averages(array, a, b):
    indices_before_a = [i for i, val in enumerate(array) if i < a]
    indices_between_a_b = [i for i, val in enumerate(array) if a <= i <= b]
    indices_after_b = [i for i, val in enumerate(array) if i > b]

    average_before_a = sum(array[i] for i in indices_before_a) / len(indices_before_a) if indices_before_a else 0
    average_between_a_b = sum(array[i] for i in indices_between_a_b) / len(
        indices_between_a_b) if indices_between_a_b else 0
    average_after_b = sum(array[i] for i in indices_after_b) / len(indices_after_b) if indices_after_b else 0

    return average_before_a, average_between_a_b, average_after_b


def visualize_averages(array, a, b):
    plt.plot(array, label='Array')

    plt.fill_between(np.arange(0, len(array)), np.min(array), a, color='lightgreen', alpha=0.3, label='Before a')
    plt.fill_between(np.arange(0, len(array)), a, b, color='lightblue', alpha=0.3, label='Between a and b')
    plt.fill_between(np.arange(0, len(array)), b, np.max(array), color='lightcoral', alpha=0.3, label='After b')

    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Array Visualization')
    plt.legend()
    plt.show()


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)

averages = calculate_averages(result_array, a_value, b_value)

print(f"Average values:")
print(f"Before a: {averages[0]}")
print(f"Between a and b: {averages[1]}")
print(f"After b: {averages[2]}")

visualize_averages(result_array, a_value, b_value)
