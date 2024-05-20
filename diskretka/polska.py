from string import ascii_uppercase

priority = {
    '&' : 1,
    '|' : 1,
    '~' : 2,
}

binary = ['&', '|']
unary = ['~']


def polska_postfix(string:str) -> str:
    """
        O Kurwa, ya perdole
        Prioriteti:
        1) )
        2) ~(not)
        3) &/| (and/or)
        4) (
    """
    stack = list()
    result = str()
    for i in string:
        if i in ascii_uppercase:
            result += i
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                try:
                    var = stack.pop()
                    while(len(stack) > 0 and var != '('):
                        result += var
                        var = stack.pop()
                except:
                    raise "Incorrect () in expression"
            elif i in priority.keys():
                while(len(stack)>0 and not(stack[-1] == '(') and priority[stack[-1]] >= priority[i]):
                    result += stack.pop()
                else:
                    stack.append(i)
    while(len(stack)>0):
        result += stack.pop()
    return result


def preprocessor(polska_expression:str, values:dict)->list:
    """Returns preprocessed expression"""
    polska_expression = list(polska_expression)
    for i in range(len(polska_expression)):
        if polska_expression[i] in values.keys():
            polska_expression[i] = int(values[polska_expression[i]])
    return polska_expression


def matcher(operation, stack) -> int:
    """Requires python3.10 or above"""
    match operation:
        case '&':
            var1 = int(stack.pop())
            var2 = int(stack.pop())
            return var1 and var2
        case '|':
            var1 = int(stack.pop())
            var2 = int(stack.pop())
            return var1 or var2
        case '~':
            var = int(stack.pop())
            return not(var)


def compute(preproced_polska:list) -> int:
    stack = []
    for i in preproced_polska:
        if type(i) == type(int(1)):
            stack.append(i)
        else:
            stack.append(matcher(i, stack))
    return stack.pop()


def evaluate(expression:str, values:dict) -> int:
    return compute(preprocessor(polska_postfix(expression), values))


#print(polska_postfix("(A&B)&A|~C"))
#print(preprocessor(polska_postfix("(A&B)&A|~C"), {"A":1, "B":0, "C":0}))
#print(compute(preprocessor(polska_postfix("(A&B)&A|~C"), {"A":1, "B":0, "C":0})))

