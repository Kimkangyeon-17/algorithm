round = int(input())

for _ in range(round):
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))

    a_num = a_lst.pop(0)
    b_num = b_lst.pop(0)

    a_star = a_lst.count(4)
    b_star = b_lst.count(4)

    a_circle = a_lst.count(3)
    b_circle = b_lst.count(3)

    a_square = a_lst.count(2)
    b_square = b_lst.count(2)


    a_triangle = a_lst.count(1)
    b_triangle = b_lst.count(1)



    if a_star > b_star:
        print("A")
    elif a_star < b_star:
        print("B")

    else:
        if a_circle > b_circle:
            print("A")
        elif a_circle < b_circle:
            print("B")
        else:
            if a_square > b_square:
                print("A")
            elif a_square < b_square:
                print("B")
            else:
                if a_triangle > b_triangle:
                    print("A")
                elif a_triangle < b_triangle:
                    print("B")
                else:
                    print("D")