import sys
import bisect
input = sys.stdin.readline

s, b = map(int, input().split())
a = list(map(int, input().split()))

bases = []
for _ in range(b):
    d, g = map(int, input().split())
    bases.append((d, g))
bases.sort()

def_list = []
gold_prefix = []
curr_sum = 0
for d, g in bases:
    def_list.append(d)
    curr_sum += g
    gold_prefix.append(curr_sum)

res = []
for attack in a:
    i = bisect.bisect_right(def_list, attack)
    if i == 0:
        res.append(0)
    else:
        res.append(gold_prefix[i - 1])

print(' '.join(map(str, res)))
