#Дан ДДФ в виде формулы в базисе И-ИЛИ-НЕ, построить и вывести таблицу
#истинности данной функции.
# Пример: (A&B)&A|~C
from string import ascii_uppercase

from polska import evaluate
from permutations_tools import generate_binary_combinations

print("Введите вашу ДДФ: ")
string = input().replace(" ", "").strip()
letters = list()

for i in string:
    if i in ascii_uppercase and i not in letters:
        letters.append(i)
letters.sort()

letters_with_values = dict()
for keys in letters:
    print(keys, end="   ")
    letters_with_values[keys] = 0
print("ДДФ")
for combs in generate_binary_combinations(len(letters)):
    print()
    for i in range(len(combs)):
        print(combs[i], end="   ")
        letters_with_values[letters[i]] = combs[i]
    print(evaluate(string, letters_with_values))
