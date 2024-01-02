N = int(input())
requests = list(map(int, input().split()))
total_budget = int(input())

start, end = 0, max(requests)

while start <= end:
    mid = (start + end) // 2
    allocated = sum(min(request, mid) for request in requests)

    if allocated > total_budget:
        end = mid - 1
    else:
        start = mid + 1

print(end) 