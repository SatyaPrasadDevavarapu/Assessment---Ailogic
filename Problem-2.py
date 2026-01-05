n = int(input().strip())
signal = list(map(int, input().split()))
k = int(input().strip())

max_sum = 0

for i in range(n - k + 1):
    current_sum = sum(signal[i:i + k])
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)