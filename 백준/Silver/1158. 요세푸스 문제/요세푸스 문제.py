N, K = map(int, input().split())

arr = [int(x) for x in range(1, N+1)]
new_arr = []

now_idx = 0

while arr:
    now_idx = (now_idx + K - 1) % len(arr)
    new_arr.append(arr.pop(now_idx))


print('<' + ', '.join(map(str, new_arr)) + '>')