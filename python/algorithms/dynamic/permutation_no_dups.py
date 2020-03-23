def generate_sequence(a_str, b_str):
    result = list()
    for i in range(len(b_str)+1):
        d = list(b_str)
        d.insert(i, a_str)
        result.append(''.join(d))
    return result

def permutations(a):
    if len(a) == 0: return []
    if len(a) == 1:
        return [a]
    if len(a) == 2:
        return [a, a[::-1]]

    result = list()
    b = list(a)
    body = list(a)
    head = body.pop(0)
    body = ''.join(body)
    perma = permutations(body)
    for p in perma:
        result.extend(generate_sequence(head, p))

    return result





if __name__ == "__main__":

    # result = generate_sequence('3', '12')
    # print(result)

    result = permutations('1234')
    print(len(result))
    for r in result:
        print(r)
