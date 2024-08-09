def seven_find(dwarfs):
    total = sum(dwarfs)
    target = total - 100

    for i in range(len(dwarfs)):
        for j in range(i + 1, len(dwarfs)):
            if dwarfs[i] + dwarfs[j] == target:
                dwarf1, dwarf2 = dwarfs[i], dwarfs[j]
                dwarfs.remove(dwarf1)
                dwarfs.remove(dwarf2)
                return dwarfs

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

result = seven_find(dwarfs)

for dwarf in result:
    print(dwarf)