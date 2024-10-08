a, b, c, d, e, f = map(int, input().split())

denominator = a * e - b * d

X = (c * e - b * f) //denominator
Y = (a * f - c * d) //denominator
print(X, Y)