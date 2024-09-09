N= int(input())
for _ in range(N):
    C = int(input())
    Quater = C // 25
    C %= 25

    Dime = C // 10
    C %= 10

    Nickel = C // 5
    C %= 5

    Penny = C

    print(Quater, Dime, Nickel, Penny)