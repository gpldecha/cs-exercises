
def is_valid(s1, s2):
    if s1 == '{' and s2 == '}': return True
    if s1 == '[' and s2 == ']': return True
    if s1 == '(' and s2 == ')': return True
    return False

# Complete the isBalanced function below.
def isBalanced(s):
    if len(s) == 0: return 'NO'
    if len(s) % 2 != 0: return 'NO'
    i = 0
    j = len(s) - 1
    steps = (len(s) - 2)/2


if __name__ == "__main__":
    isBalanced('{[()]}')
