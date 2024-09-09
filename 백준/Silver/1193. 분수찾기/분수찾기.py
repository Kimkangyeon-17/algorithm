X = int(input())

line = 1
count = 1

while X > count :
    line += 1
    count += line

num_in_line = count - X

if line % 2 == 0:
    n= line - num_in_line
    d = num_in_line + 1
else:
    n = num_in_line + 1
    d = line - num_in_line

# 결과 출력
print(f"{n}/{d}")