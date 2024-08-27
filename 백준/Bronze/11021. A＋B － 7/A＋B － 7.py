import sys
input = sys.stdin.readline

T = int(input().strip())

results = []

for i in range(1, T + 1):
    A, B = map(int, input().strip().split())

    results.append(f"Case #{i}: {A + B}")

print("\n".join(results))