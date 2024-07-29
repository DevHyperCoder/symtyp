from symtyp.conv import *
import sympy


def expr_to_latex(expr):
    r"""
    Converts a sympy expr to a latex string using `sympy.latex`

    NOTE: Latex string will NOT include \( and \)
    """
    latex_str = sympy.latex(expr)

    return latex_str

def latex_to_expr(latex_str):
    r"""
    Converts a latex string to a sympy expr

    NOTE: Latex string should NOT include \( and \)
    """
    from sympy.parsing.latex import parse_latex

    return parse_latex(latex_str)

def expr_to_typst(expr):
    r"""
    Converts a sympy expr to typst string
    """

    return latex_to_typst(expr_to_latex(expr))

def typst_to_expr(typst_str):
    """
    Converts a typst string to a sympy expr

    NOTE: Typst string should NOT include $ for marking a equation
    """

    return latex_to_expr(typst_to_latex(typst_str))

