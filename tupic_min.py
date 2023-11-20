# binary_list = [int(i) for i in bin(k)[2:]]
#         temp = 4 - len(binary_list)
#         binary_list = [0] * temp + binary_list
def support_create_table(l_duong, l3):
    list_cot = []
    l_res = []
    for k in l3:
        binary_list = [int(i) for i in bin(k)[2:]]
        temp = 4 - len(binary_list)
        binary_list = [0] * temp + binary_list
        list_cot.append(binary_list)
    # print(list_cot)

    check = True
    for elem in list_cot:
        check = True
        for k in l_duong:
            if k > 0:
                if elem[k - 1] != 1:
                    check = False
                    break
            else:
                if elem[-k - 1] != 0:
                    check = False
                    break
        l_res.append(check)
    for i in range(len(l_res)):
        print(f"{i+1} : {l_res[i]}", end="   ")
    print()


support_create_table([1, -2, -3], [2, 4, 8, 3, 5, 9, 7, 11])
# a = 13
# for i in range(31):
#     # a = 17
#     b = 17
#     x = 27
#     # print(x, end="   ")
#     y = (a * x + b) % 31
#     # print(y, end="  ")
#     k = 1
#     while y != x:
#         y = (a * y + b) % 31
#         k += 1
#         # print(y, end="  ")
#         #   print()
#     print(k, end="  ")
#     print()

# for i in range(31):
#     print((i**2 - 19 * i + 18) % 31)
