N, S = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0

def dfs(index, current_sum, selected_count):
    global count

    if index == N:
        if selected_count > 0 and current_sum == S:
            count += 1
        return

    dfs(index +1, current_sum + numbers[index], selected_count + 1)
    dfs(index +1, current_sum, selected_count)

dfs(0, 0, 0)

print(count)