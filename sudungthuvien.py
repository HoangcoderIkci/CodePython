# from sympy.logic.boolalg import simplify_logic, And, Or, Not
# from sympy import symbols

# # Khai báo biến
# x1, x2, x3, x4 = symbols("x1 x2 x3 x4")

# # Định nghĩa hàm Boolean của bạn tại đây
# # Ví dụ: f = (x và không y và không z) hoặc (không x và y và không z) hoặc (không x và không y và z)
# f = Or(
#     And(not (x1), Not(x4)),
#     And(Not(x2), x1, x3),
#     And(Not(x2), x1, x4),
#     And((x1), x3, x4),
# )

# # Tối giản hàm Boolean và in ra DNF tối thiểu
# dnf_min = simplify_logic(f, form="dnf")
# print(f"DNF tối thiểu của hàm Boolean là: {dnf_min}")

# # Để kiểm tra điểm chết, chúng ta sẽ kiểm tra xem có tồn tại bất kỳ sự kết hợp nào của biến
# # mà tại đó hàm Boolean f trả về True hay không.
# if not f.subs({x1: False, x2: False, x3: False, x4: False}):
#     print("Có ít nhất một điểm chết.")
# else:
#     print("Không có điểm chết.")


from sympy.logic.boolalg import And, Or, Not, simplify_logic
from sympy import symbols


# Sử dụng lại hàm từ đoạn mã trước
def boolean_function_from_values(var_list, values):
    n = len(var_list)
    if len(values) != 2**n:
        raise ValueError("Độ dài của danh sách giá trị không phù hợp với số biến.")

    expression = None
    for i, value in enumerate(values):
        if value:
            minterm = [
                Not(var) if bit == "0" else var
                for var, bit in zip(var_list, bin(i)[2:].zfill(n))
            ]
            minterm_expression = And(*minterm)
            if expression is None:
                expression = minterm_expression
            else:
                expression = Or(expression, minterm_expression)
    return expression


# Số biến (n) và danh sách giá trị cho hàm Boolean
n_vars = 11
variables = symbols(" ".join([f"x{i+1}" for i in range(n_vars)]))
from random import choice


def tao_list_ngau_nhien(n):
    return [choice([0, 1]) for _ in range(n)]


values_list = tao_list_ngau_nhien(2**n_vars)

# Tạo biểu thức Boolean
boolean_expression = boolean_function_from_values(variables, values_list)

# Tối giản hàm Boolean để tìm DNF tối thiểu
dnf_minimized = simplify_logic(boolean_expression, form="dnf")
# Mở file để ghi dữ liệu vào
with open("ketqua.txt", "a", encoding="utf-8") as f:
    # Ghi kết quả vào file
    f.write("\n\n\n")
    f.write("Đây là kết quả của bạn: " + str(dnf_minimized))
# Xuất ra DNF tối thiểu
# print(f"DNF tối thiểu của hàm Boolean là: {dnf_minimized}")
