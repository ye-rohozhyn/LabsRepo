from ArrayGenerator.Task1Generator import generate_array_task1


def get_user_input(prompt, min_value, max_value, exclusion_value=None):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value and user_input != exclusion_value:
                return user_input
            else:
                print(f"Invalid input. Please enter a value between {min_value} and {max_value} (excluding {exclusion_value}).")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)

print(f"Array: {result_array}")
print(f"Positions of a: {[pos for pos in range(100) if result_array[pos] == a_value]}")
print(f"Positions of b: {[pos for pos in range(100) if result_array[pos] == b_value]}")
