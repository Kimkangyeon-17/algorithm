n = int(input())

for i in range(n):
    s = input()
    case_num = i + 1
    if s.islower():
        print(f"#{case_num} {s} 는 소문자 입니다.")
    elif s.isupper():
        print(f"#{case_num} {s} 는 대문자 입니다.")