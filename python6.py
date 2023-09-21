list1 = [2600,1455,126,1568]  #numbers you want in binary code
dict1 = {}
start_num = 0 #key in dict1

for thing in list1:
    current_01 = []
    while thing>1:
        cele_cislo = thing//2  #while the number is not below 1 it divides the number
        zbytek = thing%2       # if the number is not odd, here is remainder found
        current_01.append(zbytek) #the remainder is appended to the current_01 which is later added whole to the dictionary
        thing = cele_cislo #the thing is number


    current_01.append(1) # this basically makes the while loop work like: thing>=1
    dict1[start_num] = list(reversed(current_01)) 
    start_num = start_num + 1  #updates the key in dict1

for thing in dict1.items():
    print(thing)



    


