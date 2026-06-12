from sympy import symbols, sympify, integrate, E, log, latex, oo
import matplotlib.pyplot as plt
import matplotlib as mpl
import re

mpl.rcParams['font.family'] = 'Hiragino Sans'
mpl.rcParams['mathtext.fontset'] = 'stix'

def parse_limit(value):
    value = value.strip()
    if value in ["inf", "+inf", "∞"]:
        return oo
    if value in ["-inf", "-∞"]:
        return -oo
    if value in ["0", "+0"]:
        return 0
    if value == "-0":
        return 0
    return sympify(value)

# ---- 入力式 ----
expr_str = input("関数を入力してください: ")

# 式に出てくる未定義の文字をすべてシンボルとして定義
symbols_names = set(re.findall(r"[a-zA-Z]+", expr_str)) - {"e"}  # eは定数
locals_dict = {name: symbols(name) for name in symbols_names}
locals_dict["e"] = E
locals_dict["log"] = log
expr = sympify(expr_str, locals=locals_dict)

# 積分変数を決定
symbols_in_expr = [s for s in expr.free_symbols if s != E]
if len(symbols_in_expr) == 0:
    print("変数が見つかりません。")
    exit()

elif len(symbols_in_expr) > 1:
    print("複数の変数が見つかりました:", symbols_in_expr)
    var_name = input("どの変数で積分しますか？: ")
    var = locals_dict.get(var_name)
    if var is None:
        print(f"変数 {var_name} は式に含まれていません。終了します。")
        exit()
else:
    var = symbols_in_expr[0]
    print(f"検出された変数: {var}")

# ---- 不定積分 ----
F0 = expr
F1 = integrate(F0, var)
F2 = integrate(F1, var)
F3 = integrate(F2, var)

# ---- 定積分区間 ----
print("\n=== 定積分の区間を指定してください ===")
a_str = input("下限 a = ")
b_str = input("上限 b = ")
a = parse_limit(a_str)
b = parse_limit(b_str)

# ---- 定積分 ----
I0 = integrate(F0, (var, a, b))
I1 = integrate(F1, (var, a, b))
I2 = integrate(F2, (var, a, b))
I3 = integrate(F3, (var, a, b))

# ---- TeX表示 ----
tex_str = (
    r"$F_0(%s)= %s$" "\n"
    r"$F_1(%s)= %s + C_1$" "\n"
    r"$F_2(%s)= %s + C_2$" "\n"
    r"$F_3(%s)= %s + C_3$" "\n\n"
    r"$\int_{%s}^{%s} F_0(%s)\,dx = %s$" "\n"
    r"$\int_{%s}^{%s} F_1(%s)\,dx = %s$" "\n"
    r"$\int_{%s}^{%s} F_2(%s)\,dx = %s$" "\n"
    r"$\int_{%s}^{%s} F_3(%s)\,dx = %s$"
) % (
    var, latex(F0),
    var, latex(F1),
    var, latex(F2),
    var, latex(F3),
    a_str, b_str, var, latex(I0),
    a_str, b_str, var, latex(I1),
    a_str, b_str, var, latex(I2),
    a_str, b_str, var, latex(I3),
)

plt.figure(figsize=(15, 12))
plt.axis("off")
plt.text(0.05, 0.95, tex_str, fontsize=20, va="top", ha="left")
plt.title("積分結果（不定積分 + 定積分）")
plt.show()
