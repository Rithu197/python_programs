def sum_of_rows_2d(matrix):
    row_sums = []
    for row in matrix:
        row_sums.append(sum(row))
    return row_sums

# Input 2D list from user
rows = int(input("Enter the number of rows in the 2D list: "))
columns = int(input("Enter the number of columns in each row: "))

matrix_2d = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split()))
    matrix_2d.append(row)

row_sums_2d = sum_of_rows_2d(matrix_2d)
print("Sum of each row in 2D list:", row_sums_2d)
