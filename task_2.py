list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение 5-го по порядку элемента средним арифметическим
all = sum(list_numbers)
qty = len(list_numbers)
mid = (all/qty)
list_numbers[4] = mid
print(list_numbers)
