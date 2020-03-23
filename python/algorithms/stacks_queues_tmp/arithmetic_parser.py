
def is_number(s):
    try:
        return float(s)
    except:
        return None


def to_operator(s):
    if s == '+': return lambda a, b: a + b
    if s == '-': return lambda a, b: a - b
    if s == '*': return lambda a, b: a * b
    if s == '/': return lambda a, b: a / b
    return None


def parse(expression):
    num_stack = list()
    operator_stack = list()
    for s in expression:
        if is_number(s):
            num_stack.append(float(s))
        elif to_operator(s) is not None:
            operator_stack.append(to_operator(s))
        elif s == ')':
            a = num_stack.pop()
            b = num_stack.pop()
            f = operator_stack.pop()
            num_stack.append(f(a, b))

    return num_stack.pop()



if __name__ == "__main__":

    expression = '(((2*5) + 1) + 2)'
    result = parse(expression)
    print('result: {}'.format(result))
