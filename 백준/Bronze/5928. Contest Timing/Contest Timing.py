d, h, m = list(map(int, input().split()))
total_minute = (d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11)

if total_minute < 0:
    print(-1)
else:
    print(total_minute)