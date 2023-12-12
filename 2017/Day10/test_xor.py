list = "65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22"
number_list = [int(x) for x in list.split(" ^ ")]
xor_list = number_list[0]
element = number_list[1:16]
for k in element:
    xor_list = xor_list ^ k
print(xor_list)
