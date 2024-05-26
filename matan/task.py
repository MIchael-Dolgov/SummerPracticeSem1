# Составить рекурсивную функцию подсчета количества x(m) разбиений натурального числа m,
# то есть его представлений в виде суммы натуральных чисел

def count_partitions(n, m=None):
    if m is None:
        m = n  # Начальная установка n равной m
    if n == 0:
        return 1  # Единственное разбиение 0 — пустое разбиение
    if n < 0 or m == 0:
        return 0  # Нет разбиений для отрицательных чисел или при отсутствии положительных слагаемых

    # Разбиения с наибольшим числом n и без него
    return count_partitions(n, m - 1) + count_partitions(n - m, m)

# Пример использования:
n = int(input("Введите натуральное число: "))

if type(n) != int or n <= 0:
    print("Число не является натуральным!")
else:
    print(count_partitions(n))
