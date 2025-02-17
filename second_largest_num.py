def find_second_largest(numbers):
    # Initialize two variables to track the largest and second largest numbers
    largest = second_largest = float('-inf')
    
    for num in numbers:
        # Update largest and second largest accordingly
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    # If second_largest is still -inf, it means there was no second largest number
    if second_largest == float('-inf'):
        return None
    return second_largest

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

second_largest = find_second_largest(numbers)
if second_largest is not None:
    print("The second largest number is:", second_largest)
else:
    print("There is no second largest number.")
