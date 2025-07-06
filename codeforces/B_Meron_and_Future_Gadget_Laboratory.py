n = int(input())
lab = []
for _ in range(n):
    a=list(map(int, input().split()))
    lab.append(a)
good = True
for i in range(n):
    for j in range(n):
        if lab[i][j] == 1:
            continue
        valid = False
        for k in range(n):  
            for l in range(n):  
                if lab[i][k] + lab[l][j] == lab[i][j]:
                    valid = True
                    break
            if valid:
                break
        if not valid:
            good = False
            break
    if not good:
        break

print("Yes" if good else "No")

