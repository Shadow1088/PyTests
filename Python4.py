# # var1 = "BLah..Blajh!!    blah_"

# # print (str(var1.rstrip("_")))
# comment_string = '#....... Section 3.2.1 Issue #32 .......'
# comment_string.strip('.#! ')
# # print(comment_string.strip('.#! '))
# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#     if x < 18:
#         print ("False")
#     else:
#         return x

# adults = filter(myFunc, ages)

# for x in adults:
#     print(x)

# set_comp = {num for num in range (100)}
# dict_comp = {num:num for num in range (100)}
# tuple_comp = tuple(num for num in range(100))
# print(dict_comp)
# print (set_comp)
# print(tuple_comp)





# dict_comp = {letters:num for letters in "ABCDE" for num in range(1,6)}
# print(dict_comp)

# inventory = ["screws", "nails", "hammers","Nails2","Hammers2"]
# inv = [12,13,15,8,6]
# inv_list = list(zip(inventory, inv))

# print(sorted(inv_list, key = lambda num: num[0]))
# print(sorted(inv_list, key = lambda item_len: len(item_len[0]), reverse=True))



# dict1 = {0: "I love you", 1: "Stop", 2: "LIAR!", 3:"Come back", 4:"Now"}

# order = [1,4,3,0,2]

# final = sorted(order, key = lambda key: dict1[1])
# print([dict1[value] for value in final])

# def_points = {"hp": 100, "armor": 30}

# def bullet_hit():
#     if def_points["armor"] <= 49:
#         def_points.update({"hp":0})
#     elif def_points["armor"] >=50:
#         def_points.update({"armor":0})





# print(def_points)
# bullet_hit()
# print(def_points)
    
# pp = ["a",'d','e','b','f','c']
# op = [1,2,4,0,5,2]

# list = [x for x in op]
# print (sorted(zip(op, pp)))


# the_list = [ 1,2,6,4,82,5,2, "a","ab", 45,1234,"aaaa"]
# # for x in the_list:
# #     if isinstance(x, str) == True:
# #         print (x)

# better_list = [string for string in the_list if isinstance(string,str)]
# # print(the_list)
# print(better_list)



# list1 = [1,2,3,4,5,6,7,8,9,9]
# list2 = [num for num in list1 if num < 4]
# print(list(list2))

# file = open("test.txt")
# print(list(file))
# file.close()


# print("AA")

# with open("test.txt") as file1:
#     print (list(file1))

    
# with open("test.txt") as file1:
#     print (file1.read())

# with open("test.txt", "a") as test_file:
#     for line in test_file:
#         if line == "9":
#             test_file.write("ez")




##################################################################################################################
#                                                FILE HANDLING                                                   #
##################################################################################################################



# def ez():

#     file_path = "test.txt"
#     new_content = []

#     with open(file_path, "r") as test_file:
#         lines = test_file.readlines()

#         for index, line in enumerate(lines, start=1):
#             if index == 9:
#                 line = line.strip() + " ez\n"  # Append " ez" to the line
#             new_content.append(line)

#     with open(file_path, "w") as test_file:
#         test_file.writelines(new_content)

# ez()

#
# gpt ver
##########
# mine
#

hp = 1000
wood = 10
iron = 7
kills = 2

def save():
    save_file_name = "save_file.txt"
    new_content = []
    
    with open(save_file_name) as save_file:
        lines = save_file.readlines()

        for line in lines:

            if "hp =" in line:
                
                new_hp = hp

                modified_line = f"hp = {new_hp}\n"
                
                new_content.append(modified_line)

            
            elif "wood =" in line:

                new_wood = wood

                modified_line = f"wood = {new_wood}\n"
                new_content.append(modified_line)


            elif "iron =" in line: 
                index = 0

                #current_iron = int(line[index + 6:])

                new_iron = iron 

                modified_line = line[:index] + f"iron = {new_iron}\n"
                new_content.append(modified_line)
           
            
            elif "kills =" in line:
                index = line.index("kills =")
                
                #current_kills = int(line[index + 7:])

                new_kills = kills

                modified_line = line[:index] + f"kills = {new_kills}\n"
                new_content.append(modified_line)


            else:
                new_content.append(line)
    


    with open(save_file_name, "w") as save_file:
        save_file.writelines(new_content)


def fish():
    global hp 
    hp = hp + 50
    return hp



save()


    

