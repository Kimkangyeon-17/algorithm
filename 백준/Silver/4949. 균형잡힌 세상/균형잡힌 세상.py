while True:
    string = input()

    if string == '.':
        break

    if string[-1] == '.':
        string = string[:-1]

    stack = []
    result = "yes"

    for w in string:
        if w in ["(", "["]:
            stack.append(w)
        elif w in [")", "]"]:
            if not stack:
                result = "no"
                break
            last = stack.pop()
            if (last == "(" and w == ")") or (last == "[" and w == "]"):
                continue
            else:
                result = "no"
                break
    if stack:
        result = "no"

    print(result)