dict_dec = {num for num in range(1, 16)}
dict_bin = {bin(num) for num in range(1, 16)}
dict_oct = {oct(num) for num in range(1, 16)}
dict_hex = {hex(num) for num in range(1,16)}

dict_dec_bin = {key: value for key, value in zip(dict_dec, dict_bin)}
print(dict_dec_bin)