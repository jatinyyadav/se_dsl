def create_sparse_matrix(rows, cols):
    sparse_matrix = []
    print(f"Enter the non-zero elements (row, col, value) for a {rows}x{cols} matrix:")
    while True:
        row = int(input("Row index (negative number to stop): "))
        if row < 0:
            break
        col = int(input("Column index: "))
        value = int(input("Value: "))
        if value != 0:
            sparse_matrix.append((row, col, value))
    return sparse_matrix

def display_sparse_matrix(sparse_matrix):
    print("Sparse matrix: (row, col, value)")
    for element in sparse_matrix:
        print(element)

def transpose(sparse_matrix, rows, cols):
    transposed = []
    for row, col, value in sparse_matrix:
        transposed.append((col, row, value))
    return sorted(transposed)

  

rows = int(input("enter the number of rows: "))
cols = int(input("enter the number of cols: "))

matrix = create_sparse_matrix(rows, cols)
print("Original sparse matrix:")
display_sparse_matrix(matrix)

tmatrix = transpose(matrix, rows, cols)
print("Transposed sparse matrix:")
display_sparse_matrix(tmatrix)
