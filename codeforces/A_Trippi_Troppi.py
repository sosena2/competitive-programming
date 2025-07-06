t = int(input())
for _ in range(t):
    new_name = ""
    old_name = list(map(str,input().split(" ")))
    for word in old_name:
        new_name += word[0]
    print(new_name)

    
    
    