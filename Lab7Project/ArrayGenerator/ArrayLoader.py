def read_array_from_file(filename='output_array.txt'):
    try:
        with open(filename, 'r') as file:
            array = [int(line.strip()) for line in file]
        return array
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except ValueError:
        print(f"Error reading data from '{filename}'. Ensure the file contains valid integers.")
        return None