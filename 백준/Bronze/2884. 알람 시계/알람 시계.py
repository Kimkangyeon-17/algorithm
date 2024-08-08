def calctime(start_h, start_m):
    Total_m = start_h * 60 + start_m
    Wake_t = Total_m -45
    Wake_h = (Wake_t // 60) % 24
    Wake_t = Wake_t % 60
    return (Wake_h, Wake_t)

start_h, start_m = map(int,input().strip().split())

Wake_h, Wake_t = calctime(start_h, start_m)

print(f"{Wake_h} {Wake_t}")