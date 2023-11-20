import numpy as np


def solveSystemFour(l_r=None):
    MtrA = np.zeros((16, 16))
    list_sp = [
        [0],
        [0, 1],
        [0, 2],
        [0, 2, 1, 3],
        [0, 4],
        [0, 4, 1, 5],
        [0, 4, 2, 6],
        [0, 4, 2, 1, 6, 5, 3, 7],
        [0, 8],
        [0, 8, 1, 9],
        [0, 8, 2, 10],
        [0, 8, 2, 1, 10, 9, 3, 11],
        [0, 8, 4, 12],
        [0, 8, 4, 1, 12, 9, 5, 13],
        [0, 8, 4, 2, 12, 10, 6, 14],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    ]
    for i in range(16):
        for j in list_sp[i]:
            MtrA[i][j] = 1
    colB = np.zeros(16)
    if l_r is None:
        for i in range(16):
            b = int(input(f"Enter value for b[{i}] : "))
            colB[i] = b
    else:
        colB = l_r
    res = np.linalg.solve(MtrA, colB)
    print("ket qua: ", res, "")
    return res


def solveSystemThree():
    MtrA = np.zeros((8, 8))
    list_sp = [
        [0],
        [0, 1],
        [0, 2],
        [0, 2, 1, 3],
        [0, 4],
        [0, 4, 1, 5],
        [0, 4, 2, 6],
        [0, 4, 2, 1, 6, 5, 3, 7],
    ]
    for i in range(8):
        for j in list_sp[i]:
            MtrA[i][j] = 1
    colB = np.zeros(8)
    for i in range(8):
        b = int(input(f"Enter value for b[{i}] : "))
        colB[i] = b
    res = np.linalg.solve(MtrA, colB)


#  print(res)


# solveSystemFour()


def process():
    length = int(input("length of list hs: "))
    l_hs = [0] * length
    for i in range(length):
        j = int(input(f"Enter value for f[{i}]"))
        l_hs[i] = j
    list_zero = [0] * 16
    for num in l_hs:
        r_t = 0
        while num >= 1:
            t = int(num % 10)
            r_t += 2 ** (4 - t)
            num = int(num / 10)

        list_zero[r_t] = 1
    list_res = []
    for k in range(16):
        binary_list = [int(i) for i in bin(k)[2:]]
        temp = 4 - len(binary_list)
        binary_list = [0] * temp + binary_list
        x1, x2, x3, x4 = binary_list
        res = (
            list_zero[0]
            + list_zero[1] * x4
            + list_zero[2] * x3
            + list_zero[3] * x3 * x4
            + list_zero[4] * x2
            + list_zero[5] * x2 * x4
            + list_zero[6] * x2 * x3
            + list_zero[7] * x2 * x3 * x4
            + list_zero[8] * x1
            + list_zero[9] * x1 * x4
            + list_zero[10] * x1 * x3
            + list_zero[11] * x1 * x3 * x4
            + list_zero[12] * x1 * x2
            + list_zero[13] * x1 * x2 * x4
            + list_zero[14] * x1 * x2 * x3
            + list_zero[15] * x1 * x2 * x3 * x4
        )

        list_res.append(res % 2)
    #    print(res % 2)
    return list_res


def process2():
    list_res = []
    for k in range(16):
        binary_list = [int(i) for i in bin(k)[2:]]
        temp = 4 - len(binary_list)
        binary_list = [0] * temp + binary_list
        x1, x2, x3, x4 = binary_list

        res = (~x1 & x3) | (x1 & ~x2 & ~x3) | (x1 & ~x3 & x4 | x2 & ~x3 & x4)
        list_res.append(res)
    #    print(res % 2)
    return list_res


def CheckLiner(l_in=None):
    l_res = solveSystemFour(l_in)
    l_res %= 2
    fill = list(set(range(16)) - set([1, 2, 4, 8]))
    for num in fill:
        if l_res[num] != 0:
            return False
    return True


# l_r = solveSystemFour()
# l_r = process2()
# print(l_r)
# print(CheckLiner())

print(process2())
