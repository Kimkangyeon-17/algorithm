def get_dial_time(letter):
    # 다이얼 시간 규칙에 따라 각 문자에 대해 시간을 계산
    if letter in 'ABC':
        return 3
    elif letter in 'DEF':
        return 4
    elif letter in 'GHI':
        return 5
    elif letter in 'JKL':
        return 6
    elif letter in 'MNO':
        return 7
    elif letter in 'PQRS':
        return 8
    elif letter in 'TUV':
        return 9
    elif letter in 'WXYZ':
        return 10
    return 0  # 만약 예외가 있을 경우

def calculate_total_time(word):
    total_time = 0
    for letter in word:
        total_time += get_dial_time(letter)
    return total_time

# 입력을 읽어오기
word = input().strip()

# 총 시간을 계산하고 출력
print(calculate_total_time(word))