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


def visualize(array, a, b, averages):
    plt.plot(array, label='Array')

    plt.scatter(np.argmin(array), np.min(array), color='green', label=f'Min: {np.min(array)}')
    plt.scatter(np.argmax(array), np.max(array), color='red', label=f'Max: {np.max(array)}')
    plt.scatter(a, array[a], color='blue', label=f'Before a: {averages[0]}')
    plt.scatter(b, array[b], color='orange', label=f'Between a and b: {averages[1]}')
    plt.scatter(len(array) - 1, array[-1], color='purple', label=f'After b: {averages[2]}')
    plt.scatter([i for i, val in enumerate(array) if val == a], [a] * array.count(a), color='brown', label=f'a = {a}')
    plt.scatter([i for i, val in enumerate(array) if val == b], [b] * array.count(b), color='grey', label=f'b = {b}')

    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Array Visualization')
    plt.legend()
    plt.show()


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)
averages = calculate_averages(result_array, a_value, b_value)
visualize(result_array, a_value, b_value, averages)