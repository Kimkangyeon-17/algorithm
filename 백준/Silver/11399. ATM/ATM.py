T = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

new_list = [0] * (T+1)

for i in range(1, T+1):
    new_list[i] = new_list[i-1] + numbers[i-1]

print(sum(new_list))