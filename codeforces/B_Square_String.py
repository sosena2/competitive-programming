t = int(input())
for _ in range(t):
    string = input()
    if len(string) % 2!=0:
        print("NO")
    else:
        valid = True
        left = 0
        right = len(string)//2
        while left < right and right < len(string):
            if string[left] != string[right]:
                valid = False
                break
            else:
                left += 1
                right +=1 
        if valid == False:
            print("NO")
        else:
            print("YES")