t = int(input())
for _ in range(t):
    p = input()
    s = input()
    
    i, j = 0, 0
    
    valid = True

    while i < len(p) and j < len(s):
        if s[j] != p[i]:
            valid = False
            break
        if j+1 < len(s) and s[j+1] == s[j]:
            j += 2 
        else:
            j += 1  
        i += 1

    if i != len(p) or j != len(s):
        valid = False

    print("YES" if valid else "NO")
