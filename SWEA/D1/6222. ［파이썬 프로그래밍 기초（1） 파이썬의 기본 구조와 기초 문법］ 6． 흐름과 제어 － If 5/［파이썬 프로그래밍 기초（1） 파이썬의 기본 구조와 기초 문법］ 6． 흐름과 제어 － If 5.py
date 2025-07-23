s = input()

if s.islower():
    print(f'{s}(ASCII: {ord(s)}) => {s.upper()}(ASCII: {ord(s.upper())})')
elif s.isupper():
    print(f'{s}(ASCII: {ord(s)}) => {s.lower()}(ASCII: {ord(s.lower())})')