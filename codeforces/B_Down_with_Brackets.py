t = int(input())
for _ in range(t):
    s = input()
    count = 0
    valid = False
    for i in range(1, len(s) - 1):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            valid = True
            break
    if valid or count != 0:
        print("YES")
    else:
        print("NO")

