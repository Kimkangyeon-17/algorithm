def isFrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i ==0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))

count = 0
for num in numbers:
    if isFrime(num):
        count += 1

print(count)