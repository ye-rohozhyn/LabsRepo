def save_array_to_file(array, filename='output_array.txt'):
    with open(filename, 'w') as file:
        for element in array:
            file.write(f"{element}\n")