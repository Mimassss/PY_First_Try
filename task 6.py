list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = list_numbers[-1]
for i in list_numbers:
    if i > max_:
        max_ = i
        index_max = list_numbers.index(max_)
        #print(max_, list_numbers.index(max_))
        list_numbers[-1], list_numbers[9] = list_numbers[9], list_numbers[-1]
        print(list_numbers)













