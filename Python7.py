import random 

list1 = [num for num in range(50)]
after_list1 = [num for num in random.sample(list1,15)]

for i in after_list1:
    
    if i<=5 and i != 0:
        print(i*" "+5*"*")
    elif i>5 and i<51:
        if i%2 == 1:
            print(i*" "+(8*"*"))
        else:
            print(5*" "+8*"*")
    elif i == 0:
        print("***********************")
    

print(after_list1)


    