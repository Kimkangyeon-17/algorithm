T = int(input())

numbers = []
for tc in range(1, T+1):
    num = int(input())
    if num != 0:
        numbers.append(num)
    elif num == 0:
        numbers.pop()

print(sum(numbers))