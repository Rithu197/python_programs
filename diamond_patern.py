def print_diamond(n):
    # Upper part of the diamond (increasing)
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print stars
        print("*" * (2 * i + 1))

    # Lower part of the diamond (decreasing)
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print stars
        print("*" * (2 * i + 1))

# Input for the number of rows (height of the diamond's top half)
n = int(input("Enter the number of rows for the top half of the diamond: "))
print_diamond(n)
