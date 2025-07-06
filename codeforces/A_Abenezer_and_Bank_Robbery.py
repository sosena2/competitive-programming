a, b, c = map(int, input().split())
notes = int(input())
banknotes_arr = list(map(int, input().split()))
count = 0
for i in range(len(banknotes_arr)):
    if banknotes_arr[i] > b and banknotes_arr[i] < c:
        count += 1
print(count)
