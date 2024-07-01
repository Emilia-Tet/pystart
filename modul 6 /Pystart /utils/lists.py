def add_lists(list1, list2):
    if len(list2) < len(list1):
        for i in range(len(list1) - len(list2)):
            list2.append(0)

    elif len(list2) > len(list1):
        for i in range(len(list2) - len(list1)):
            list2.append(0)
    return [x+y for x, y in zip(list1, list2)]
