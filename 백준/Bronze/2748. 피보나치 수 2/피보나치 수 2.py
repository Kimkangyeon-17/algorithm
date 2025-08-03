n = int(input())

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    f0 = 0  # 0번째
    f1 = 1  # 1번째
    current = 0  # n번째

    for i in range(2, n + 1):
        current = f0 + f1
        f0 = f1
        f1 = current

    return f1


print(fibo(n))
