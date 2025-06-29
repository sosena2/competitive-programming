t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    left = 0
    right = len(arr) - 1
    score = 0
    while left < right:
        if arr[left] + arr[right] == k:
            score += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] > k:
            right -= 1
        elif arr[left] + arr[right] < k:
            left += 1
    print(score)



