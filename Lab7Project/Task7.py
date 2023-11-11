import matplotlib.pyplot as plt
import numpy as np
from ArrayGenerator.Task1Generator import generate_array_task1
from InputHelper.InputChecker import get_user_input


def visualize_min_max_a_b(array, a, b):
    plt.plot(array, label='Array')

    plt.scatter(np.argmin(array), np.min(array), color='green', label=f'Min: {np.min(array)}')
    plt.scatter(np.argmax(array), np.max(array), color='red', label=f'Max: {np.max(array)}')
    plt.scatter([i for i, val in enumerate(array) if val == a], [a] * array.count(a), color='blue', label=f'a = {a}')
    plt.scatter([i for i, val in enumerate(array) if val == b], [b] * array.count(b), color='yellow', label=f'b = {b}')

    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Array Visualization')
    plt.legend()
    plt.show()


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)
visualize_min_max_a_b(result_array, a_value, b_value)
