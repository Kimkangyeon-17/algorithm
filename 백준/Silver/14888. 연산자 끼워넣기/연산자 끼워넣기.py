N = int(input())

numbers = list(map(int, input().split()))

add, minus, mul, div = map(int, input().split())

max_result = float('-inf')
min_result = float('inf')

def calc(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def backtracking(idx, current, add, minus, mul, div):
    global max_result
    global min_result

    if idx == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    next_number = numbers[idx]

    if add > 0:
        new_result = calc(current, next_number, 0)
        backtracking(idx + 1, new_result, add - 1, minus, mul, div)

    if minus > 0:
        new_result = calc(current, next_number, 1)
        backtracking(idx + 1, new_result, add , minus - 1, mul, div)

    if mul > 0:
        new_result = calc(current, next_number, 2)
        backtracking(idx + 1, new_result, add, minus, mul - 1, div)

    if div > 0:
        new_result = calc(current, next_number, 3)
        backtracking(idx + 1, new_result, add, minus, mul, div - 1)

backtracking(1, numbers[0], add, minus, mul, div)

print(max_result)
print(min_result)