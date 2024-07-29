# symtyp - useful functions for using sympy with [ typst ](https://typst.app/) and [latex](https://www.latex-project.org/)

```py
import sympy
import symtyp

expr = symtyp.typst_to_expr('(x+4)^2')
x = sympy.symbols('x')
print(expr.subs(x, 4))
# OUTPUT: 64

expr = symtyp.typst_to_expr('(x+4)(x-2)')

print(symtyp.expr_to_typst(sympy.expand(expr)))
# OUTPUT: x^2 plus 2 x minus 8

print(symtyp.expr_to_latex(sympy.expand(expr)))
# OUTPUT: x^{2} + 2 x - 8

expr = symtyp.latex_to_expr(r'\frac{x^2 + 2x -8}{x-2}')
print(sympy.simplify(expr))
# OUTPUT: x + 4

print(sympy.limit(expr, x, 2))
# OUTPUT: 6
```


you need the following dependencies:

- `sympy`
    ```console
    pip install sympy
    ```
- `typst` compiler: [github](https://github.com/typst/typst?tab=readme-ov-file#installation)
- `pandoc`: [website](https://pandoc.org/installing.html)

TODO: Make it a actual python package one can install.



