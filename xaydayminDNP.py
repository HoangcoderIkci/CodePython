import math


def count_and_find_ones(lst):
    count = 0
    position = -1
    for i in range(len(lst)):
        if lst[i] == 1:
            count += 1
            if position == -1:
                position = i
    return count, position


def convert_to_binary(num):
    binary = bin(num)[2:]  # Chuyển số sang chuỗi nhị phân và bỏ đi ký tự '0b' ở đầu
    binary_list = list(binary)  # Chuyển chuỗi thành danh sách
    res = []
    for b in binary_list:
        res.append(int(b))
    return res


def add_lists(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append((x + y) % 2)
    return result


def chia_nhom_theo_chu_so_1(lst):
    len_lst = len(lst)
    so_nhom = int(math.log(len_lst, 2)) + 1
    lst_nhom = [[] for i in range(so_nhom)]
    for i in range(len_lst):
        if lst[i] == 1:
            temp = convert_to_binary(i)
            do_lech = so_nhom - 1 - len(temp)
            if do_lech:
                temp = [0] * do_lech + temp
            so_cs_1 = temp.count(1)
            lst_nhom[so_cs_1].append(temp)
    return lst_nhom


def tach_phan_tu_hop_le(kho_hien_tai, set_fill):
    res = set()
    for r in kho_hien_tai:
        for elem in r:
            if tuple(elem) not in set_fill:
                res.add(tuple(elem))
    return list(res)


def tao_lai_kho(lst_nhom, set_after):
    for r in range(len(lst_nhom)):
        lst_nhom[r] = []
    for elem in set_after:
        ct = list(elem).count(1)
        lst_nhom[ct].append(list(elem))
    return lst_nhom


def check_hang_xom_so_2(lst1, lst2):
    if 2 in lst1 and 2 in lst2:
        for i in range(len(lst1)):
            if lst1[i] == 2 and lst2[i] != 2:
                return False
    return True


def print_ket_qua_dang_poly(lst_res):
    for elem in lst_res:
        for i in range(len(elem)):
            if elem[i] == 1:
                print(f"X{i+1}", end="")
            elif elem[i] == 0:
                print(f"~X{i+1}", end="")
        print(end="  V  ")
    print()


def print_ket_qua_dang_poly2(lst_res, rac, i):
    print("================================ buoc ", i)
    for elem1 in lst_res:
        for elem in elem1:
            print(elem)
        print("================================")
    print("================================ rac --------------------------------")
    for elem in rac:
        print(elem)
    print("================================ end rac --------------------------------")
    print("================================ end buoc ", i)
    print("\n\n")


def main_process(lst_values):
    len_lst = len(lst_values)
    so_nhom = int(math.log(len_lst, 2)) + 1
    lst_res = []
    lst_nhom = chia_nhom_theo_chu_so_1(lst_values)
    kho_hien_tai = list(lst_nhom.copy())
    set_rac = set()
    set_after = set()
    while True:
        for i in range(so_nhom - 1):
            for elem1 in lst_nhom[i]:
                for elem2 in lst_nhom[i + 1]:
                    if check_hang_xom_so_2(elem1, elem2) == False:
                        continue
                    temp = add_lists(elem1, elem2)
                    so_cs_1, first_index_1 = count_and_find_ones(temp)
                    if so_cs_1 == 1:
                        set_rac.add(tuple(elem1))
                        set_rac.add(tuple(elem2))
                        el_cp = elem1.copy()
                        el_cp[first_index_1] = 2
                        set_after.add(tuple(el_cp))
        lst_res += tach_phan_tu_hop_le(lst_nhom, set_rac)
        print_ket_qua_dang_poly2(lst_nhom, set_rac, i)
        lst_nhom = tao_lai_kho(lst_nhom, set_after)

        set_rac.clear()
        if set_after == set():
            break
        set_after.clear()
    return lst_res


l = [0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
print_ket_qua_dang_poly(main_process(l))
