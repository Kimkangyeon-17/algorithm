n = int(input())

mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

avg = sum * 100 / mymax / int(n)
print(avg)