from random import randint

start = -10
stop = 10
count = 15
list_numbers = [randint(start, stop) for _ in range(count)]

print(list_numbers)
