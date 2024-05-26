import copy

from pprint import pprint

def transpose(matrix):
    return list(map(list, zip(*matrix)))
def add_to_list(vector1, vector2):
    return [i + j for i, j in zip(vector1, vector2)]

def multiply_to_list(vector, num):
    return [i * num for i in vector]

def E_matrix_nxn(num:int)->list:
    E = [[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        E[i][i] = 1
    return E


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
def gauss_jordan_ellimination(matrix)->list:
    """для [1,0] - справа номер строки главной переменной"""
    matrix = gaussian_elimination(matrix)
    pivot_vars = list()
    equation_coiffecents = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                pivot_vars.append([matrix[i][j],j])
                matrix[i][j] = 0
                break
        equation_coiffecents.append(multiply_to_list(matrix[i], -1))

    for i in range(len(pivot_vars)):
        if pivot_vars[i][0] == 0:
            continue
        if pivot_vars[i][0] < 0:
            pivot_vars[i][0] = -pivot_vars[i][0]
            equation_coiffecents[i] = multiply_to_list(equation_coiffecents[i], -1)
        equation_coiffecents[i] = multiply_to_list(equation_coiffecents[i], 1/pivot_vars[i][0])
        pivot_vars[i][0]= 1

    E = E_matrix_nxn(len(matrix[0]) - len(pivot_vars))
    ortohnal_vectors = list()
    Ej = 0
    Ei = 0
    # Вычислимое значение главных переменных
    for i in range(len(pivot_vars)):
        pivot_vars[i].append(None)
    # Цикл для подсчёта каждого ортогонального вектора по теореме ФСР
    for k in range(len(matrix[0]) - len(pivot_vars)):
        temporary_matrix = copy.deepcopy(equation_coiffecents)
        new_vector = [0 for _ in range(len(temporary_matrix[0]))]
        # Циклы для выислеления текущего ортогонального вектора
        for j in range(len(temporary_matrix[0]) - 1, len(pivot_vars) - 1, -1):
            for i in range(len(temporary_matrix) - 1, -1, -1):
                temporary_matrix[i][j] = temporary_matrix[i][j] * E[Ei][Ej]
            new_vector[j] = E[Ei][Ej]
            Ej += 1
        Ei += 1
        Ej = 0

        for i in range(len(pivot_vars)-1, -1, -1):
            pivot_vars[i][2] = sum(temporary_matrix[i])
            for ji in range(len(pivot_vars)-1, -1, -1):
                temporary_matrix[ji][pivot_vars[i][1]] = temporary_matrix[ji][pivot_vars[i][1]]*pivot_vars[i][2]
        for line in pivot_vars:
            new_vector[line[1]] = line[2]
        ortohnal_vectors.append(new_vector)
    return ortohnal_vectors

# Пример использования
"""
rows = [
    [2,1,3,-1],
    [7,4,3,-3],
    [1,1,-6,0],
    [5,7,7,8]
]
"""

def app():
    rows = list()
    n = int(input("Введите количество используемых векторов: "))
    m = int(input("Введите количество коэффицентов используемых векторов: "))
    for i in range(n):
        vector = input(f"Введите ваш {i} вектор, разделяя коэффиценты пробелом: ").split(" ")
        if(len(vector) < m):
            print("Данный вектор не соответствует заявленому количеству коэффицентов вектора!")
            exit(1)
        vector = [int(x) for x in vector]
        rows.append(vector)
    print("Исходные векторы: ")
    pprint(gaussian_elimination(rows))
    print()
    print("Ортогональные векторы: ")
    pprint(gauss_jordan_ellimination(rows))

if __name__ == '__main__':
    try:
        app()
    except:
        print("Что-то пошло не так")
        exit(1)
else:
    raise "It's not a module"
