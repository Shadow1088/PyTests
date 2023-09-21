# #test_list = [1,2,3,4]
# #print (str(test_list).strip("[]").replace(",",""))

# my_set = {1,2,3,4,5}
# print(tuple(my_set)[2])

# my_set2 = {5,6}
# print(my_set.union(my_set2)) # it takes all the stuff from both sets and ignores dupes
# print(my_set.intersection(my_set2)) # takes only stuff that matches in both sets

# test_list = [43,45,56,89,78,56,12,23,45,78,56,23]
# print(len(test_list))
# print (len(set(test_list)))
# print(len(test_list) == len(set(test_list)))

# e_dict = {1:"one",2:"two",3:"three"}
# print(1 in e_dict)
# print("four" in e_dict.values())


# print(bool(456123215)) #Nothing, "None" or 0 = False // everything else = True  (( even the -1 ))

# money = 100
# hungry = True
# bored = True

# if money > 80 and hungry == True:
#     print("lets eat")
# elif bored == True:
#     print("lets eat")



# x = 1
# if x in ["a"]:
#     print("yes")
#     if x in ["a",1]:
#         print("yes2")



# #############################################

# #          NESTING           #

# #############################################

# #excercise

# money1 = 500
# hungry = False
# bored = True

# if money1 > 200:
#     print("yes I have got the money")
#     if hungry == True:
#         print("yes I am hungry")
#         if bored == True:
#             print("lets eat2")


# ##  MATCH  ##


# mood = 'bored' 
            
# match mood:
#     case "hungry":
#         print("h")
#     case "thirsty":
#         print("t")
#     case _:
#         print("else")




# grade = 55

# match grade:
#     case 1:
#         print("nice")
#     case 2:
#         print("well")
#     case 3:
#         print("bro")
#     case 4:
#         print("idiot")
#     case 5:
#         print("kys")
#     case _:
#         print("invalid")

# #x = 0
# #while x < 101:
#  #   print(x)
#   #  x += 2

# my_list = []
# x = 0
# while x < 101:
#     my_list.append(x)
#     x = x + 2
#     if x == 58:
#        x = x + 2
# if 100 in my_list:
#         print(my_list)


# #while x < 100:
#     #if x == 0:
#      #   x += 1
#     #print(list(x))
#     #x += 2
 
# def greeter(name, day,  greet = "Hello"):
#     print(str(f"{greet} {name}, its {day}."))

# greeter(name = "Alex", day = "Tuesday")


# def a(*everything):
#     print (everything)

# a(1,2,34,5,6)

# a = 10

# def A():
#     a = 2; a+=2
#     print (a)

# A()

# a = 2

# def test(b, a):
#     b = a + 2
    
#     return b
# print (test(2,3))

# multiplier = 2
# calculated = False

# def calculator(arg1):
#     global calculated
#     result = arg1 * multiplier
#     calculated = True
#     return result

# print (calculator(3))

# sort([1,5,3,4,2], )

# is_greater_than_five = lambda x: "Hello" if x > 5 else "bye"
# print(is_greater_than_five(5))



# # list1 = [1,4,3,5,6,4,5,8,2,6,4,5,6,3,1,5,2,4]
# # for i in list1: 
# #     print(i)

# inventory = ["screws", "nails", "hammers"]
# inv = [12,13,15]

# # for number in zip(inventory, inv):
# #     print(number[1])

# # for id, name in enumerate(inventory):
# #     print(f"{name} [{id}] - inventory: {number}")
# #     # print(name, id)

# # and name, inv1 in zip(inventory):

# for id, tuple in enumerate(zip(inventory,inv)):
#     print(f"{tuple[0]} [{id}] - inv. {tuple[1]}")

# even = float


# the_list = []
# for i in range(0,100):
#     if i%2 == 0:
#         the_list.append(i)

# print(the_list)


# the_list = []
# for i in range(0, 100):
#     if (i/2).is_integer():
#         the_list.append(i)

# print(the_list)

list1 = [1,2,3,4.56,8.7253,452.4,"look","bro","I can code", 8,25,3.25,3.1453,0.315225]
words = []
# for word in list1:
#     if not isinstance(word, int):
#         words.append(word)
#     else:
#         continue

# for is_float in words:
#     if isinstance(is_float, float):
#         words.remove(is_float)
#     else:
#         continue

for word in list1:
    if isinstance(word, str):
        words.append(word)

print(words)

# LIST COMPREHENSION
my_list = [(adds_num,adds_num*2) if adds_num <=10 else 0 for adds_num in range(0,100)]
my_list = [zeros for zeros in my_list if zeros != 0]

print(my_list)


inventory = ["screws", "nails", "hammers","3","4"]
inv = [12,13,15,8,6]
restore = [(name, number) for name, number in zip(inventory, inv) if number < 10]
print(restore)


letters = ["a","b","c","d","e","f","g","h"]
numbers = [1,2,3,4,5,6,7,8]
chess_board = [[f"{letter}{number}" for number in range(1,9)] for letter in "ABCDEFGH"[::-1]]
for row in chess_board:
    print(row)



























