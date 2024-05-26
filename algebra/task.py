def transpose(matrix):
    """Транспонирует матрицу"""
    return list(map(list, zip(*matrix)))

# Функция для вычисления скалярного произведения
def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))


# Функция для вычитания векторов
def subtract_vectors(vec1, vec2):
    return [x - y for x, y in zip(vec1, vec2)]

# Функция для деления вектора на скаляр
def scalar_divide(vec, scalar):
    return [x / scalar for x in vec]


# Функция ортогонализации Грама-Шмидта
def gram_schmidt(matrix):
    orthogonal = []
    for vec in matrix:
        for ortho_vec in orthogonal:
            projection_length = dot_product(vec, ortho_vec) / dot_product(ortho_vec, ortho_vec)
            vec = subtract_vectors(vec, [x * projection_length for x in ortho_vec])
        orthogonal.append(vec)
    return orthogonal


# Функция для нахождения ортогонального дополнения
def orthogonal_complement(matrix):
    n = len(matrix[0])
    k = len(matrix)

    # Получаем ортогональные векторы из матрицы A
    orthogonal_basis = gram_schmidt(matrix)

    # Добавляем ортогональные дополнения
    complement_basis = []
    for i in range(n):
        complement_vector = [1 if j == i else 0 for j in range(n)]
        for ortho_vec in orthogonal_basis:
            projection_length = dot_product(complement_vector, ortho_vec) / dot_product(ortho_vec, ortho_vec)
            complement_vector = subtract_vectors(complement_vector, [x * projection_length for x in ortho_vec])
        complement_basis.append(complement_vector)

    return [vec for vec in complement_basis if any(x != 0 for x in vec)]


# Пример использования
A = [
    [1, 2, 3, 3],
    [4, 5, 6, 5],
]

complement = orthogonal_complement(A)
for vec in complement:
    print(vec)
