x_index = []
y_index = []

N= int(input())
for _ in range(N):
    x, y = map(int,input().split())
    x_index.append(x)
    y_index.append(y)

x1 = max(x_index) - min(x_index)
y1 = max(y_index) - min(y_index)

print(x1 * y1)