start = 7
blank = 0
while start > 0:
    print(" " * blank + "*" * start)
    start -= 2
    blank += 1
    if start == 0:
        print(" " * blank + "*" * start)
