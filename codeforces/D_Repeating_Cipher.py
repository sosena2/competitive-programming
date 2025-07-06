n = int(input())
cipher = input()
new_string = ""
cur_pos = 0
for i in range(1, 55):
    cur_pos += i
    if (cur_pos - 1) < n:
        new_string += cipher[cur_pos-1]
    else:
        break
print(new_string)






