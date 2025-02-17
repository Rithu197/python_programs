def remove_duplicates(numbers):
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    return unique_numbers

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

unique_numbers = remove_duplicates(numbers)
print("List after removing duplicates:", unique_numbers)
