# Calculator using module_try1_py10.py
# I am aware of sum() function, but I wanted to try it this way.

import module_try1_py10 as mtp

print("Write the numbers: ")

sum_list = []
while True:
    
    x = input()
    print("okay, whats next? (end to exit)")
    if x.isdigit():
        sum_list.append(int(x))
   
    else:
        print(f" -> input: {x}"); print(" -> Not a number")
        
        break


mtp.sum0(sum_list)

