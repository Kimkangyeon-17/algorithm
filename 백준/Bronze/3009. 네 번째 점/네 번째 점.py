x_cords = []
y_cords = []

for _ in range(3):
    x, y = map(int, input().split())
    x_cords.append(x)
    y_cords.append(y)

if x_cords.count(x_cords[0]) == 1:
    x4  = x_cords[0]
elif x_cords.count(x_cords[1]) == 1:
    x4 = x_cords[1]
else:
    x4 = x_cords[2]

if y_cords.count(y_cords[0]) == 1:
    y4 = y_cords[0]
elif y_cords.count(y_cords[1]) == 1:
    y4 = y_cords[1]
else:
    y4 = y_cords[2]

print(x4, y4)