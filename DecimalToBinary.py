# DECIMAL TO BINARY CONVERSION

list1 = [11, 15, 156]  #  Add to list number you want to have converted
dict1 = {}             #  Storage for final results
start_num = 0          #  Starting index for dict1

for i in list1:
    current_01 = []
    while i>=1:
        whole_num = i//2
        remainder = i%2       
        current_01.append(remainder)
        i = whole_num          # divide by 2 till i > 1 and append remainder to list
    
    dict1[start_num] = list(reversed(current_01))  # have to be reversed to get correct order
    start_num = start_num + 1    

for conversion in dict1.items():
    print(conversion)



    


