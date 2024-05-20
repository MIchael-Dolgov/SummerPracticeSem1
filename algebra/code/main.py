def gauss_elimination(A, B):
    n = len(A)
    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск максимального элемента в столбце i
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[k][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]

        # Обнуление нижних элементов столбца i
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            B[k] -= factor * B[i]
            A[k] = [A[k][j] - factor * A[i][j] for j in range(n)]

    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (B[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]


# Пример использования
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

B = [8, -11, -3]

solution = gauss_elimination(A, B)
print("Решение уравнения Ax = B:", solution)