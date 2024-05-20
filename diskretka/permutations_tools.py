def generate_permutations(lst):
    if len(lst) == 0:
        return [[]]
    perms = []
    for i in range(len(lst)):
        elem = lst[i]
        rest_elems = lst[:i] + lst[i+1:]
        for perm in generate_permutations(rest_elems):
            perms.append([elem] + perm)
    return perms

def generate_binary_combinations(n):
    if n == 0:
        return ['']
    smaller_combinations = generate_binary_combinations(n - 1)
    return ['0' + combo for combo in smaller_combinations] + ['1' + combo for combo in smaller_combinations]
