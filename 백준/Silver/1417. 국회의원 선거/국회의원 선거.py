import sys

input = sys.stdin.readline


N = int(input())
candidates = []
for i in range(N):
    vote = int(input())
    candidates.append(vote)

if N == 1:
    print(0)
else:
    dasom_votes = candidates[0]
    others_votes = candidates[1:]

    maesu = 0

    while True:
        max_vote = max(others_votes)

        if dasom_votes > max_vote:
            break

        max_idx = others_votes.index(max_vote)
        others_votes[max_idx] -= 1
        dasom_votes += 1
        maesu += 1

    print(maesu)
