from ArrayGenerator.ArrayLoader import read_array_from_file


loaded_array = read_array_from_file()

if loaded_array is not None:
    print(f"Loaded Array: {loaded_array}")
