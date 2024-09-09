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

def add_sparse_matrices(matrix1, matrix2, rows, cols):
    result = {}
    
    # Add elements of the first matrix
    for row, col, value in matrix1:
        if (row, col) in result:
            result[(row, col)] += value
        else:
            result[(row, col)] = value
    
    # Add elements of the second matrix
    for row, col, value in matrix2:
        if (row, col) in result:
            result[(row, col)] += value
        else:
            result[(row, col)] = value
    
    # Convert result to sparse matrix format (excluding zero values)
    return [(row, col, value) for (row, col), value in result.items() if value != 0]

def subtract_sparse_matrices(matrix1, matrix2, rows, cols):
    result = {}
    
    # Subtract elements of the second matrix from the first matrix
    for row, col, value in matrix1:
        if (row, col) in result:
            result[(row, col)] += value
        else:
            result[(row, col)] = value
    
    for row, col, value in matrix2:
        if (row, col) in result:
            result[(row, col)] -= value
        else:
            result[(row, col)] = -value
    
    # Convert result to sparse matrix format (excluding zero values)
    return [(row, col, value) for (row, col), value in result.items() if value != 0]

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Creating first sparse matrix...")
    matrix1 = create_sparse_matrix(rows, cols)
    print("Original first sparse matrix:")
    display_sparse_matrix(matrix1)

    print("Creating second sparse matrix...")
    matrix2 = create_sparse_matrix(rows, cols)
    print("Original second sparse matrix:")
    display_sparse_matrix(matrix2)

    # Transpose
    tmatrix1 = transpose(matrix1, rows, cols)
    tmatrix2 = transpose(matrix2, rows, cols)
    print("Transposed first sparse matrix:")
    display_sparse_matrix(tmatrix1)
    print("Transposed second sparse matrix:")
    display_sparse_matrix(tmatrix2)

    # Addition
    added_matrix = add_sparse_matrices(matrix1, matrix2, rows, cols)
    print("Sum of sparse matrices:")
    display_sparse_matrix(added_matrix)

    # Subtraction
    subtracted_matrix = subtract_sparse_matrices(matrix1, matrix2, rows, cols)
    print("Difference of sparse matrices:")
    display_sparse_matrix(subtracted_matrix)

if __name__ == "__main__":
    main()
