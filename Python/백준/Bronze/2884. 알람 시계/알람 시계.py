from datetime import datetime, timedelta

h, m = map(int, input().split())
allam = datetime(2024, 1, 1, h, m)

ans = allam - timedelta(minutes=45)

print(ans.hour, ans.minute)