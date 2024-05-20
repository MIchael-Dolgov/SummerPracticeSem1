# Составить рекурсивную функцию подсчета количества x(m) разбиений натурального числа m,
# то есть его представлений в виде суммы натуральных чисел

def rec_div(n):
    if n == 1:
        return 1
    count = 1
    d = 2
    f = False
    while d <= n and not f:
        if n % d == 0:
            while n % d == 0:
                count += 1
                n //= d
            f = True
        d += 1
    count *= rec_div(n)
    return count

n = int(input())

if type(n) != int or n <= 0:
    print("Число не является натуральным!")
else:
    print(rec_div(n))
