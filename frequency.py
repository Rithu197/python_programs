def find_frequencies(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

# Take input from the user
input_string = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers_list = [int(x) for x in input_string.split()]

# Call the function with the user's list
frequencies = find_frequencies(numbers_list)

# Print the frequencies
print(frequencies)
