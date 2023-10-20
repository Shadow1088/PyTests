# Calculator using module_try1_py10.py
# I am aware of sum() function, but I wanted to try it this way.

import module_try1_py10 as mtp

print("The numbers: ")

sum_list = []
while True:
    x = input()
    if x.isdigit():
        sum_list.append(int(x))
   
    else:
        print(f" -> input: {x}"); print(" -> Not a number")
        
        break


mtp.sum0(sum_list)

