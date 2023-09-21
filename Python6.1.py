list1 = [230, 21, 56]       #########################################################################
dict1 = {}                  #         MADE BY CHATGPT, HELPED ME WITH THE python6.py                #
                            #########################################################################
for index, thing in enumerate(list1):
    binary_representation = []

    while thing > 0:
        quotient = thing // 2
        remainder = thing % 2
        binary_representation.append(remainder)
        thing = quotient

    binary_representation.reverse()
    dict1[index] = binary_representation

print(dict1)
