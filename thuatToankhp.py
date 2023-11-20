import random

my_list = [1] * 256
for i in range(50):
    my_list[i] = random.choice([0, 1])
# my_list = [1] * 256
# my_list[3] = 0
# my_list[14] = 0
# my_list[6] = 0
so_an = 8


def create_list_l(l_gia_tri_hs):
    list_l = []
    l_gia_tri_cot_0 = []
    for ind, elem in enumerate(l_gia_tri_hs):
        if elem == 0:
            l_gia_tri_cot_0.append(ind)
            binary_list = [int(i) for i in bin(ind)[2:]]
            temp = so_an - len(binary_list)
            binary_list = [0] * temp + binary_list
            l_temp = []
            k = 1
            for el in binary_list:
                if el == 0:
                    l_temp.append({k})
                else:
                    l_temp.append({-k})
                k += 1
            # print(l_temp)
            list_l.append(l_temp)
    return list_l, l_gia_tri_cot_0


################################################################ nhập giá trị đầu vào ở đây và sửa số ẩn ở dòng 1.
# my_list =  [0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
list_l, l_gia_tri_cot_0 = create_list_l(my_list)


########################################################################
def check_set_none(my_set):
    lst = list(my_set)
    for elem in lst:
        if -elem in my_set:
            return False
    return True


def phep_nhan_2_list(list1, list2):
    res = []
    for elem1 in list1:
        for elem2 in list2:
            temp = elem1 | elem2
            if check_set_none(temp) == False:
                continue
            if temp not in res:
                res.append(elem1 | elem2)
    return res


def buoc_2_rut_gon_sau_khi_nhan(l1):
    k = 0
    while k < len(l1):
        t = l1[k]
        for i in range(len(l1)):
            if i != k and l1[k].issubset(l1[i]):
                l1.pop(i)
                k = -1
                break
        k += 1
    # print(l1)
    return l1


def cong_hai_set(s1, s2):
    if s1.issubset(s2):
        return 2
    if s2.issubset(s1):
        return 1
    return -1


def support_create_table(l_duong, l3):
    list_cot = []
    l_res = []
    for k in l3:
        binary_list = [int(i) for i in bin(k)[2:]]
        temp = so_an - len(binary_list)
        binary_list = [0] * temp + binary_list
        list_cot.append(binary_list)

    check = 1
    for elem in list_cot:
        check = 1
        for k in l_duong:
            if k > 0:
                if elem[k - 1] != 1:
                    check = 0
                    break
            else:
                if elem[-k - 1] != 0:
                    check = 0
                    break
        l_res.append(check)
    l_r = []
    for ind, elem in enumerate(l_res):
        if elem:
            # print(ind)
            l_r.append(ind + 1)

    for i in range(len(l_res)):
        print(f"{i+1} : {l_res[i]}", end="   ")
    print()
    return l_r


def create_table(cok_knp):
    # print(cok_knp)
    table_res = []
    x_res = []
    for elem_set in cok_knp:
        x_res.append(list(elem_set))
        l_ho_tro = [x for x in range(2**so_an) if x not in l_gia_tri_cot_0]
        table_res.append(
            # support_create_table(list(elem_set), [2, 4, 8, 3, 5, 9, 7, 11])
            support_create_table(list(elem_set), l_ho_tro)
        )
    return table_res, x_res


def main_process(lst):
    while len(lst) > 1:
        temp = phep_nhan_2_list(lst[0], lst[1])
        lst.remove(lst[0])
        lst.remove(lst[0])
        lst.append(temp)
    cok_knp = buoc_2_rut_gon_sau_khi_nhan(lst[0])
    return create_table(cok_knp)


# l1 = [{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {-9}, {10}, {-11}]
# l2 = [{1}, {2}, {-3}, {4}, {5}, {6}, {7}, {8}, {9}, {-10}, {11}]
# l3 = [{-1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {-9}, {10}, {-11}]
# l4 = [{1}, {-2}, {-3}, {4}, {5}, {6}, {7}, {8}, {9}, {-10}, {11}]
# l5 = [{1}, {2}, {-3}, {4}, {5}, {6}, {7}, {8}, {-9}, {10}, {-11}]
# l6 = [{1}, {2}, {-3}, {-4}, {-5}, {6}, {7}, {8}, {9}, {-10}, {11}]
# l1 = [{1}, {2}, {3}, {4}]
# l2 = [{1}, {2}, {3}, {-4}]
# l3 = [{1}, {-2}, {-3}, {4}]
# l4 = [{-1}, {2}, {-3}, {4}]
# l5 = [{-1}, {-2}, {3}, {4}]
# l6 = [{-1}, {-2}, {3}, {-4}]
# l7 = [{-1}, {-2}, {-3}, {4}]
# l8 = [{-1}, {-2}, {-3}, {-4}]


table, x = main_process(list_l)
l_cot_da_check = set()
l_row_thoa_man = []
n = len(x)


def check_dk1(row_i, l_cot_da_check):
    # global l_cot_da_check
    check = False
    set_temp = set()
    for elem in table[row_i]:
        if elem not in l_cot_da_check:
            check = True
            set_temp.add(elem)
            l_cot_da_check.add(elem)
    # print(l_cot_da_check)
    return check, set_temp, l_cot_da_check


def xoa_hang_i(set_temp, l_cot_da_check):
    # print(l_cot_da_check)
    # print(set_temp)
    l_cot_da_check = l_cot_da_check - set_temp
    return l_cot_da_check


def test(i, k, l_cot_da_check):
    for j in range(k, n):
        ok, set_temp, l_cot_da_check = check_dk1(j, l_cot_da_check)
        if ok:
            l_row_thoa_man.append(j + 1)
            l_cot_da_check = test(i + 1, j + 1, l_cot_da_check)
            l_row_thoa_man.pop(i)
            l_cot_da_check = xoa_hang_i(set_temp, l_cot_da_check)
    if len(l_cot_da_check) == 2**so_an - len(l_gia_tri_cot_0):
        for num_row in l_row_thoa_man:
            print(x[num_row - 1], end="  ")
        print()
    return l_cot_da_check


test(0, 0, l_cot_da_check)
