"""
conv.py 

conversion between latex and typst using pandoc
"""

import subprocess

def latex_to_typst(latex_str):
    r"""
    Converts a latex string (for example from `expr_to_latex`) to a typst string using `pandoc`

    Example:
    ```py
    typst_str = latex_to_typst('\\frac{4}{3 x^2}')
    assert typst_str == 'frac(4, 3 x^2)'
    ```

    NOTE: Latex string should NOT include \( and \)
    NOTE: The typst writer outputs in a verbose manner, it still displays fine in typst
    """
    cmd = subprocess.run(
        ["pandoc", "--from=latex", "--to=typst"],
        input=f"\\({ latex_str }\\)",
        capture_output=True,
        text=True,
    )
    output = str(cmd.stdout).strip()[1:-1]
    return output

def typst_to_latex(typst_str):
    r"""
    Converts a typst string to a latex string

    Example:
    ```py
    latex_str = typst_to_latex(r'(x+4)/(x^2 - x + 1)')
    assert latex_str = r'\frac{x + 4}{x^{2} - x + 1}'
    ```

    NOTE: Typst string should NOT include $ for marking a equation
    NOTE: Latex string will NOT include \( and \)
    """
    cmd = subprocess.run(
        ["pandoc", "--from=typst", "--to=latex"],
        input=f"${ typst_str }$",
        capture_output=True,
        text=True,
    )
    output = str(cmd.stdout).strip()[2:-2]
    return output
