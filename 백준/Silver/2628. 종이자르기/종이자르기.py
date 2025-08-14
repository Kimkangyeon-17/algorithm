col, row = map(int, input().split())
N = int(input())

row_lst = []
col_lst = []

for _ in range(N):
    num, w = map(int, input().split())
    if num == 0:
        row_lst.append(w)
    else:
        col_lst.append(w)

row_lst.extend([0, row])
col_lst.extend([0, col])

row_lst = sorted(list(set(row_lst)))
col_lst = sorted(list(set(col_lst)))

max_row_gap = 0
for i in range(len(row_lst)-1):
    gap = row_lst[i+1] - row_lst[i]
    max_row_gap = max(max_row_gap, gap)

max_col_gap = 0
for i in range(len(col_lst)-1):
    gap = col_lst[i+1] - col_lst[i]
    max_col_gap = max(max_col_gap, gap)

print(max_row_gap * max_col_gap)

