N = int(input())

arr = list(map(int, input().split()))
if N == 1:
    print(1)
else:
    max_count = 1
    increase_count = 1
    decrease_count = 1


    for i in range(1, N):
        if arr[i] > arr[i-1]:
            increase_count += 1
            decrease_count = 1

        elif arr[i] < arr[i-1]:
            decrease_count += 1
            increase_count = 1

        else:
            increase_count += 1
            decrease_count += 1
        max_count = max(max_count, increase_count,decrease_count)

    print(max_count)