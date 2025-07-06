from collections import Counter
def solve():
    s = input()
    t = input()
    p = input()
    c1 = Counter(s)
    c2 = Counter(t)
    c3 = Counter(p)
    diff = c2 - c1
    i = 0
    j =0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    if i!= len(s):
        print("NO")
        return
    if diff <= c3:
        print("YES")
    else:
        print("NO") 
q = int(input())
for _ in range(q):
    solve()
    
    
