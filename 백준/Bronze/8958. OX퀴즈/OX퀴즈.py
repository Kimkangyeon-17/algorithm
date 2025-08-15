T = int(input())

for tc in range(1, T+1):
    OX = list(input())

    count_list = []

    count = 0
    for answer in OX:
        if answer == 'O':
            count += 1
            count_list.append(count)
        else:
            count = 0

    print(sum(count_list))