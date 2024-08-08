def calctotal_hour(Start_h,Start_m,Duration_m):
    Start_total_m = Start_h * 60 + Start_m
    end_total_m = Start_total_m + Duration_m
    end_h = (end_total_m // 60) % 24
    end_m = end_total_m % 60
    return end_h, end_m

Start_h, Start_m = map(int, input().strip().split())
Duration_m = int(input().strip())

end_h, end_m = calctotal_hour(Start_h, Start_m, Duration_m)

print(F"{end_h} {end_m}")