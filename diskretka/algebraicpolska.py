priority = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3,
}

def polska_postfix(string:str) -> str:
    stack = list()
    result = str()
    for i in string:
        if i.isdigit():
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
                stack.append(i)
    while(len(stack)>0):
        result += stack.pop()
    return result

print(polska_postfix("3+4*2/(1-5)^2"))