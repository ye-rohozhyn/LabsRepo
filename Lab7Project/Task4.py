import matplotlib.pyplot as plt
from ArrayGenerator.Task1Generator import generate_array_task1
from InputHelper.InputChecker import get_user_input
from ArrayGenerator.ArraySaver import save_array_to_file
from ArrayGenerator.ArrayLoader import read_array_from_file


def visualize_array(array, a, b):
    plt.plot(array, label='Array')

    plt.scatter([i for i, val in enumerate(array) if val == a], [a] * array.count(a), color='red', label=f'a = {a}')
    plt.scatter([i for i, val in enumerate(array) if val == b], [b] * array.count(b), color='blue', label=f'b = {b}')

    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Array Visualization')
    plt.legend()
    plt.show()


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)
save_array_to_file(result_array)
load_array = read_array_from_file()
visualize_array(load_array, a_value, b_value)
