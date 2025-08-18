import sys
input = sys.stdin.readline

N, K = map(int, input().split())

numbers = list(map(int, input().split()))

current_sum = sum(numbers[:K])
max_sum = current_sum

for i in range(1, N - K + 1):
    current_sum = current_sum - numbers[i-1] + numbers[i + K - 1]
    max_sum = max(max_sum, current_sum)

print(max_sum)