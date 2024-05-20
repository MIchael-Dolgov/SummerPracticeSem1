# Рабочий код его оставить
def gauss_elimination(A, B):
    n = len(B)

    # Прямой ход метода Гаусса с выборочным исключением
    for pivot_row in range(n):
        max_row = pivot_row
        for i in range(pivot_row + 1, n):
            if abs(A[i][pivot_row]) > abs(A[max_row][pivot_row]):
                max_row = i
        # Переставляем строки для выборочного исключения
        A[pivot_row], A[max_row] = A[max_row], A[pivot_row]
        B[pivot_row], B[max_row] = B[max_row], B[pivot_row]

        # Проверяем, что диагональный элемент не равен нулю
        if A[pivot_row][pivot_row] == 0:
            raise ValueError("Метод Гаусса не может быть применен: диагональный элемент равен нулю")

        # Приведение к верхнетреугольному виду
        for row in range(pivot_row + 1, n):
            factor = A[row][pivot_row] / A[pivot_row][pivot_row]
            for col in range(pivot_row, n):
                A[row][col] -= factor * A[pivot_row][col]
            B[row] -= factor * B[pivot_row]

    # Обратный ход метода Гаусса
    X = [0] * n
    for i in range(n - 1, -1, -1):
        # Проверяем, что диагональный элемент не равен нулю
        if A[i][i] == 0:
            raise ValueError("Метод Гаусса не может быть применен: диагональный элемент равен нулю")
        X[i] = B[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            B[j] -= A[j][i] * X[i]

    return X

# Пример использования
A = [[3, 1, -1], [4, -1, 3], [1, -1, 2]]
B = [5, 6, 2]

try:
    solution = gauss_elimination(A, B)
    print("Решение: ", solution)
except ValueError as e:
    print(e)
