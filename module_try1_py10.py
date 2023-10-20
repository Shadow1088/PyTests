# Created module for Python10.py

def sum0(*args):
    sum1 = 0
    for i in args:
        for j in i:  
            sum1 += j
              
    print(f"The sum of the numbers is: {sum1}")