from ArrayGenerator.Task1Generator import generate_array_task1
from InputHelper.InputChecker import get_user_input


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)

print(f"Array: {result_array}")
print(f"Positions of a: {[pos for pos in range(100) if result_array[pos] == a_value]}")
print(f"Positions of b: {[pos for pos in range(100) if result_array[pos] == b_value]}")
