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


def save_array_to_file(array, filename='output_array.txt'):
    with open(filename, 'w') as file:
        for element in array:
            file.write(f"{element}\n")


a_value = get_user_input("Enter a (from -255 to 255): ", -255, 255)
b_value = get_user_input(f"Enter b (from -255 to 255, except a ({a_value})): ", -255, 255, a_value)

result_array = generate_array_task1(a_value, b_value)

save_array_to_file(result_array, 'output_array.txt')
print("Array saved to 'output_array.txt'")
