def sum_of_rows_3d(matrix):
    row_sums = []
    for matrix_2d in matrix:
        matrix_row_sums = []
        for row in matrix_2d:
            matrix_row_sums.append(sum(row))
        row_sums.append(matrix_row_sums)
    return row_sums

# Input 3D list from user
layers = int(input("Enter the number of 2D matrices (layers) in the 3D list: "))
rows = int(input("Enter the number of rows in each 2D matrix: "))
columns = int(input("Enter the number of columns in each row: "))

matrix_3d = []
for i in range(layers):
    print(f"Enter matrix {i + 1}:")
    matrix_2d = []
    for j in range(rows):
        row = list(map(int, input(f"Enter row {j + 1} elements separated by spaces: ").split()))
        matrix_2d.append(row)
    matrix_3d.append(matrix_2d)

row_sums_3d = sum_of_rows_3d(matrix_3d)
print("Sum of each row in 3D list:", row_sums_3d)
