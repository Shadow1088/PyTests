


# #list \\ changeable and ORDERED !!  []  !!
# my_list = [1,2,3,4]

# my_list.reverse()
# my_list.append(5)

# print(my_list)

# #tuple \\ !!UNchangeable!!, ORDERED !!  ()  !!
# my_tuple = (1,2,3,1.5, "something", [7,8,9])
# # append X - the tuple is unchangeable, you cannot add, remove anything in it

# print(my_list[2])
# print(my_tuple[5][0])
# print(my_tuple[-3])

# excercise_list = ["first entry",[123,456,[0,"Hello :)"]], "bye"]
# print(excercise_list[1][2][1])


# test_list = [1,2,3,4]
# print(test_list[1:3])

# #set?





# # dictionaries {"key":"value"}

# Armor_dict = {"Iron helmet":50, "Uranium pants":75}
# Armor = sum(Armor_dict.values())
# HP = 100



# test_dict = {"HP":HP, "Armor":Armor}
# print (str(test_dict).strip("{}").replace("'", ""))
# print (str(Armor_dict).strip("()").replace("'", ""))


# hit0 = True

# if hit0 == True and Armor == 0:
#     test_dict.update({"HP":HP-25})
# elif hit0 == True and Armor != 0:
#     test_dict.update({"Armor":Armor-25})



# print (str(test_dict).strip("{}").replace("'", ""))
# print (str(Armor_dict).strip("()").replace("'", ""))




#.get returns "None" if the key does not exist


# FUNCTIONS #
import random


Armor_dict = {"Iron helmet":50, "Uranium pants":75}
Armor = sum(Armor_dict.values())
HP = 100

Armor_box_dict = {"Blue Talisman":200, "Shadowed Cloak":20, "Spiky gloves":30}
Armor_box_poss = random.choice(list(Armor_box_dict.items()))

test_dict = {"HP":HP, "Armor":Armor}

def hit():
    test_dict.update({"Armor":Armor-25})
    if Armor == 0:
        test_dict.update({"HP":HP-25})


def Armor_box():
    print (str(f"Armor box obtained, you have received {Armor_box_poss[0]}"))
    print (str(f"Added {Armor_box_poss[1]} armor"))

Armor_box()

Armor_dict[Armor_box_poss[0]] = Armor_box_poss[1]
print (Armor_dict)
# print(HP)
# print(Armor)
# print (str(test_dict).strip("{}").replace("'", ""))
# print (str(Armor_dict).strip("() {}").replace("'", ""))

# print(Armor_box_poss)
# if Armor_box_poss[0] in Armor_box_dict:
#     print("yes")
# else:
#     print("no")
# Armor_box_obtained1 = {Armor_box_poss[0]:Armor_box_poss[1]}
# print(str(Armor_box_obtained1))





    


