N = int(input())

if N == 1:
    print(1)
else:
    room = 1
    count = 1

    while N > room:
        room += 6 * count
        count += 1

    print(count)