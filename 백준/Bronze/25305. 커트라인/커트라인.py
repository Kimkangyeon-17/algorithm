N, k = map(int, input().split())

numbers = list(map(int,input().split()))

numbers.sort(reverse=True)

cutline = numbers[k - 1]

print(cutline)