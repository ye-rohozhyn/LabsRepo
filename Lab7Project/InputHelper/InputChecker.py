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