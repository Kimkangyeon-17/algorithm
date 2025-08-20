count = 0
def recursion(s, l, r):
    global count
    count += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())

for tc in range(1, T+1):
    count = 0
    string = input()
    result = 0
    if isPalindrome(string) == 0:
        print(result, count)
    else:
        result = 1
        print(result, count)