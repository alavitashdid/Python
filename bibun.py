from sympy import sympify, diff, E, latex
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Hiragino Sans'  # ← 日本語フォント
mpl.rcParams['mathtext.fontset'] = 'stix'      # ← 数式フォント

expr_str = input("関数を入力してください: ")

locals_dict = {"e": E}
expr = sympify(expr_str, locals=locals_dict)

symbols_in_expr = [s for s in expr.free_symbols if s != E]

if len(symbols_in_expr) == 0:
    print("変数が見つかりません。")

else:
    if len(symbols_in_expr) > 1:
        print("複数の変数が見つかりました:", symbols_in_expr)
        var_name = input("どの変数で微分しますか？: ")

        var = None
        for s in symbols_in_expr:
            if str(s) == var_name:
                var = s
                break

        if var is None:
            print(f"変数 {var_name} は式に含まれていません。終了します。")
            exit()

    else:
        var = symbols_in_expr[0]
        print(f"検出された変数: {var}")

    # 微分の計算
    f0 = expr
    f1 = diff(expr, var)
    f2 = diff(expr, var, 2)
    f3 = diff(expr, var, 3)

    # ターミナル出力
    print("0階微分:", f0)
    print("1階微分:", f1)
    print("2階微分:", f2)
    print("3階微分:", f3)

    # --- ここから TeX 表示（別ウィンドウ） ---
    tex_str = (
        r"$f(%s)= %s$" "\n"
        r"$f'(%s)= %s$" "\n"
        r"$f''(%s)= %s$" "\n"
        r"$f'''(%s)= %s$"
    ) % (
        var, latex(f0),
        var, latex(f1),
        var, latex(f2),
        var, latex(f3)
    )

    plt.figure(figsize=(15, 10))
    plt.axis("off")  # 枠線を消す
    plt.text(0.05, 0.9, tex_str, fontsize=20, va="center", ha="left")
    plt.title("微分結果（TeX 表記）")
    plt.show()
