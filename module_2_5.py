def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
result = get_matrix(3, 4, 5)
result1 = get_matrix(4, 5, 10)
result2 = get_matrix(2, 7, 36)
print(result)
print(result1)
print(result2)