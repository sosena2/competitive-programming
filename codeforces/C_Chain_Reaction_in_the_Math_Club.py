from collections import defaultdict

n, m = map(int, input().split())
laces = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    laces[a].add(b)
    laces[b].add(a)

groups = 0

while True:
    r = []

    for stud in range(1, n + 1):
        if len(laces[stud]) == 1:
            r.append(stud)

    if not r:
        break  

    for stud in r:
        if laces[stud]:
            neighbor = laces[stud].pop()
            laces[neighbor].remove(stud)

    groups += 1

print(groups)

    

