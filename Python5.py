import math
count = []
max_num = 0
spaces = 0


row_count = int(input("How many rows do you want? "))

for i in range(1, row_count+1):
    if i%2 == 1:
        print(math.floor((row_count-i)/2)*" "+i*"*")
        count.append(i)
        max_num = i
        spaces = round(max_num/2)

for i in range(3):
    trunk = int((max_num-1)/2)
    trunk = trunk - 1 + trunk % 2
    print(int(((max_num-trunk)/2))*" "+trunk*"*")







