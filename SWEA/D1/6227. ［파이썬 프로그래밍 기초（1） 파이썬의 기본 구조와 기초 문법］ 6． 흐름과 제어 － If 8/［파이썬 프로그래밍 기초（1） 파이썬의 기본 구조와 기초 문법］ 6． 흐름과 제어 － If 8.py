result = []
for i in range(100, 301):
    hundred = i // 100
    tens = (i // 10) % 10
    units = i % 10
    
    if hundred % 2 == 0 and tens % 2 == 0 and units % 2 == 0:
        result.append(i)
        
print(','.join(map(str, result)))