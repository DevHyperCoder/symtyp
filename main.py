import sympy
import symtyp

if __name__ == "__main__":
    expr = symtyp.typst_to_expr('(x+4)^2')
    x = sympy.symbols('x')
    print(expr.subs(x, 4))

    expr = symtyp.typst_to_expr('(x+4)(x-2)')
    print(symtyp.expr_to_typst(sympy.expand(expr)))
    print(symtyp.expr_to_latex(sympy.expand(expr)))

    expr = symtyp.latex_to_expr(r'\frac{x^2 + 2x -8}{x-2}')
    print(sympy.simplify(expr))
    print(sympy.limit(expr, x, 2))
