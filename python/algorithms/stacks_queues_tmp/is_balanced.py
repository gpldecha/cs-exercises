def is_valid_closing(a, b):
    if a == '(' and b == ')': return True
    if a == '[' and b == ']': return True
    if a == '{' and b == '}': return True
    return False


# def is_balanced(expression):
#     if len(expression) <= 1: return 'NO'
#     if len(expression) % 2 != 0: return 'NO'
#     # build list
#     brackets = [[expression[0], 1]]
#     for i in range(1, len(expression)):
#         s = expression[i]
#         if s == brackets[-1][0]:
#             brackets[-1][1] += 1
#         else:
#             brackets.append([s, 1])
#     i = 0
#     j = len(brackets) - 1
#     print(brackets)
#     while i < j:
#         print('{} {}'.format(i, j))
#         print(brackets[i])
#         print(brackets[j])
#         print()
#         if not is_valid_closing(brackets[i][0], brackets[j][0]): return 'NO'
#         if brackets[i][1] != brackets[j][1]: return 'NO'
#         i += 1
#         j -= 1
#     return 'YES'


def is_open(a):
    if a == '{': return True
    if a == '(': return True
    if a == '[': return True
    return False


def is_balanced_stacks(expression):
    expression = expression.lstrip().rstrip()
    if len(expression) <= 1: return 'NO'
    if len(expression) % 2 != 0: return 'NO'

    bracket = str(expression[0])
    if not is_open(bracket): return 'NO'
    stacks = [[bracket]]
    for i in range(1, len(expression)):
        bracket = expression[i]
        if len(stacks):
            previous_bracket = stacks[-1][-1]
        else:
            previous_bracket = None

        if is_open(bracket):
            if previous_bracket is None:
                if not is_open(bracket): return 'NO'
                stacks.append([bracket])
            elif bracket == previous_bracket:
                stacks[-1].append(bracket)
            else:
                stacks.append([bracket])
        else:
            if not is_valid_closing(previous_bracket, bracket): return 'NO'
            stacks[-1].pop()
            if len(stacks[-1]) == 0:
                stacks.pop()
    if len(stacks) != 0: return 'NO'
    return 'YES'


if __name__ == '__main__':
    f = open('input09.txt', 'r')
    e = open('expected_output.txt', 'r')
    count = 0
    f.readline()
    for i, line in enumerate(f):
        expected_result = e.readline().lstrip().rstrip()
        result = is_balanced_stacks(line)
        if result != expected_result:
            print('{} result: {}  expected: {}'.format(i, result, expected_result))
            print('input: {}'.format(line))
            break
    f.close()


    expression1 = '{(([])[])[]}'
    expression2 = '{(([])[])[]]}'
    expression3 = '{(([])[])[]}[]'
    expression4 = '[([{{}}]{[[][][([[]]){[]}{}]]}[]{{}}{})[[]]]{{}}(()[[[[[(){}[]]({}{[]})[][[][]]]]{}]{[{}]{[{[][](()({{()}}){([]({({{[]}([([()]{()[[([({{{[]{(){}}[][]({{[([])()](())([{[]([()]{})}]){}([]){()}{}[]([[()]])}()})[{}]}()}(())}){{}()}[]]{{}})]][[]({{[{}]}})({{}({{[]{()}([][{[()]}]{})}()})}{{}}{})]()(){}}(()({()}[([](){[]()}[])])[])[])][{[{[]}]{}([])}]()(()))}){([{}])}[(([]){[]{}})]{}({}{})}){}({{}([][](){{[][{()([[{}()]]{()}{{}{[()]}})[()[]{}](){[{}()[]][{{}}{[{}][]()}[]](())[[][]][]()}}[({}([[{([]){}}]()([()(){}]){([()]())}](()))(()))]]{}()[][{[{}(([]){([()]{()()}([{}][[[]{[[(({([([]){()[]}]){(())}[]}))][((([]{})[{}[[()]({({[()[]]{}(()[{}[][[{}][][]({()}[{([])}][])]][]{})([])}){}{((){})}}){[]}[]()(()(()))(()[{{}}]){}({{{((()([](()[][]{}){({})}{(([{({{}})}]))})))}}})]]))]]}]]))})]}]}})}))})}]}}])'
    print(is_balanced_stacks(expression4))
