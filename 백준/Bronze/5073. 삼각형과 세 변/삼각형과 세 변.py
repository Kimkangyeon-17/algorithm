while True:

    x, y, z = map(int, input().split())\

    if x == 0 and y == 0 and z == 0:
        break

    A = sorted([x, y, z])

    if A[2] >= A[0] + A[1]:
        print('Invalid')

    elif x == y == z:
        print('Equilateral')

    elif x == y or y == z or x == z:
        print('Isosceles')

    else:
        print('Scalene')