while True:
    n = int(input())
    if n == -1:
        break

    A = []
    for i in range( 1, n // 2 + 1):
        if n % i == 0:
            A.append(i)

    if sum(A) == n:
        print(f"{n} = {' + '.join(map(str, A))}")
    else:
        print(f"{n} is NOT perfect.")