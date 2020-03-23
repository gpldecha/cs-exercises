def largestRectangleAreaTmp(heights):
    stack = [-1]
    maxArea = 0

    for i in range(len(heights)):
        # we are saving indexes in stack that is why we comparing last element in stack
        # with current height to check if last element in stack not bigger then
        # current element
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            lastElementIndex = stack.pop()
            l = (i - stack[-1] - 1)
            print('lastElementIndex: {}  stack[-1]: {}  i: {}  lenght: {}'.format(lastElementIndex, stack[-1], i, l))
            maxArea = max(maxArea, heights[lastElementIndex] * l)
        stack.append(i)

        # we went through all elements of heights array
        # let's check if we have something left in stack
    print('popping remaining')
    print('stack: {}'.format(stack))
    while stack[-1] != -1:
        lastElementIndex = stack.pop()
        l = len(heights) - stack[-1] - 1
        print('lastElementIndex: {} l: {}'.format(lastElementIndex, l))
        maxArea = max(maxArea, heights[lastElementIndex] * l)

    return maxArea

def largestRectangleArea(h):
    stack = list()
    max_area = 0
    for i in range(len(h)):
        print(' - ')
        print('i: {}'.format(i))
        print(stack)
        j = i
        height = h[i]
        while stack and stack[-1][1] > height:
            j, last = stack.pop()
            l = (i - j)
            print('h: {} i: {} j: {} l: {}'.format(h[j], i, j, l))
            area = last*l
            max_area = max(max_area, area)
        stack.append((j, height))

    print('popping remaining')
    print('stack: {}'.format(stack))
    # pop the remaining items from the stack
    while stack:
        j, last = stack.pop()
        l = (len(h) - j)
        print('h: {} i: {} j: {} l: {}'.format(h[j], i, j, l))
        area = last*l
        max_area = max(max_area, area)
    return max_area

def largestRectangle_discussion_solution(h):
    h.append(0)
    stack = []
    maxArea = 0
    print('start')
    for i, height in enumerate(h):
        print(' - ')
        print('i: {}'.format(i))
        print(stack)
        j = i
        while stack and stack[-1][1] > height:
            j, last = stack.pop()
            area = (i - j) * last
            print('last: {} i: {} j: {} h: {}'.format(last, i, j, h[j]))
            if area > maxArea:
                maxArea = area
        stack.append((j, height))

    return maxArea


if __name__ == "__main__":

    #h = [2, 3, 4, 2]
    h = [1, 2, 3, 4, 5]
    h = [11, 11, 10, 10, 10]
    #print(largestRectangleArea(h))
    print(largestRectangleArea(h))
    print(' ')
    print(largestRectangle_discussion_solution(h))
