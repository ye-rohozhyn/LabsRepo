from ArrayGenerator.Task1Generator import generate_array_task1
from ArrayGenerator.ArraySaver import save_array_to_file
from InputHelper.InputChecker import get_user_input


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)

save_array_to_file(result_array, 'output_array.txt')
print("Array saved to 'output_array.txt'")
