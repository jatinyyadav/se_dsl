# Store a sparse matrix using a dictionary
def store_sparse_matrix(matrix):
    sparse_matrix = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                sparse_matrix[(i, j)] = matrix[i][j]
    return sparse_matrix

# Transpose a sparse matrix
def transpose_sparse_matrix(sparse_matrix):
    transposed = {}
    for (i, j), value in sparse_matrix.items():
        transposed[(j, i)] = value
    return transposed

# Add two sparse matrices
def add_sparse_matrices(sparse_matrix1, sparse_matrix2):
    result = sparse_matrix1.copy()
    for (i, j), value in sparse_matrix2.items():
        if (i, j) in result:
            result[(i, j)] += value
        else:
            result[(i, j)] = value
    return result

# Example usage
if __name__ == "__main__":
    matrix1 = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]
    ]

    matrix2 = [
        [0, 4, 0],
        [5, 0, 6],
        [0, 0, 0]
    ]

    sparse_matrix1 = store_sparse_matrix(matrix1)
    sparse_matrix2 = store_sparse_matrix(matrix2)

    print("Sparse Matrix 1:", sparse_matrix1)
    print("Sparse Matrix 2:", sparse_matrix2)

    transposed_matrix1 = transpose_sparse_matrix(sparse_matrix1)
    print("Transpose of Sparse Matrix 1:", transposed_matrix1)

    added_matrices = add_sparse_matrices(sparse_matrix1, sparse_matrix2)
    print("Addition of Sparse Matrices:", added_matrices)
