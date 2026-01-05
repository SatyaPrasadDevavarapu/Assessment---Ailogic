def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for current in intervals:
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            merged[-1][1] = max(merged[-1][1], current[1])
    return merged

n = int(input().strip())
intervals = []

for i in range(n):
    start, end = map(int,input().strip().split())
    intervals.append([start,end])

result = merge_intervals(intervals)
for interval in result:
    print(interval[0], interval[1])