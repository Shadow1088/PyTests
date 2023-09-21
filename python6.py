list1 = [2600,1455,126,1568]
dict1 = {}
start_num = 0

for thing in list1:
    current_01 = []
    while thing>1:
        cele_cislo = thing//2
        zbytek = thing%2       
        current_01.append(zbytek)
        thing = cele_cislo


    current_01.append(1)
    dict1[start_num] = list(reversed(current_01))
    start_num = start_num + 1    

for thing in dict1.items():
    print(thing)



    


