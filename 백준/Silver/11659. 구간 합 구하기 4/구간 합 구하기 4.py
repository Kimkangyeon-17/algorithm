import sys
input = sys.stdin.readline

suNo, quiNo = map(int,input().split())

numbers = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quiNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])