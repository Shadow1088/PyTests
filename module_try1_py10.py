def sum0(*args):
    working_list = []
    for b in args:
        working_list.append(b)

    total = 0
    for element in working_list:
        total += int(element)

    return total
