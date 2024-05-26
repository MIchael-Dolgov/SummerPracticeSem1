import copy


def add_to_list(list1, list2):
    return [a + b for a, b in zip(list1, list2)]


def multiply_to_list(lst, factor):
    return [a * factor for a in lst]


def forward_elimination(matrix) -> list:
    """Метод Гаусса - прямой ход"""
    rows_len = len(matrix)
    columns_len = len(matrix[0])

    for i in range(rows_len):
        # Поиск строки с максимальным элементом в текущем столбце
        max_row = i
        for k in range(i + 1, rows_len):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        # Перестановка строк
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Проверка на деление на 0
        if matrix[i][i] == 0:
            continue  # Пропустить итерацию если ведущий элемент нулевой

        # Прямой ход
        for l in range(i + 1, rows_len):
            factor = -matrix[l][i] / matrix[i][i]
            matrix[l] = add_to_list(matrix[l], multiply_to_list(matrix[i], factor))

    # Удаление нулевых строк
    matrix = [row for row in matrix if any(el != 0 for el in row)]

    return matrix


def backward_elimination(matrix) -> list:
    """Метод Гаусса - обратный ход"""
    rows_len = len(matrix)
    columns_len = len(matrix[0])

    for i in range(rows_len - 1, -1, -1):
        if matrix[i][i] == 0:
            continue  # Пропустить итерацию если ведущий элемент нулевой

        pivot_vector = matrix[i]
        for l in range(i - 1, -1, -1):
            factor = -matrix[l][i] / pivot_vector[i]
            matrix[l] = add_to_list(matrix[l], multiply_to_list(pivot_vector, factor))

    return matrix


def gaussian_elimination(matrix) -> list:
    matrix = forward_elimination(matrix)
    matrix = backward_elimination(matrix)
    return matrix


# Пример использования
matrix = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

result = gaussian_elimination(matrix)
for row in result:
    print(row)
