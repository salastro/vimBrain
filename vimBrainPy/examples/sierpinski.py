# [sierpinski.b -- display Sierpinski triangle
# (c) 2016 Daniel B. Cristofani
# http://brainfuck.org/]

from ..vb import converter, interpreter

program = converter("""
++++++++[>+>++++<<-]>++>>+<[-[>>+<<-]+>>]>+[
    -<<<[
        ->[+[-]+>++>>>-<<]<[<]>>++++++[<<+++++>>-]+<<++.[-]<<
    ]>.>+[>>]>+
]
""")
interpreter(program)

# [Shows an ASCII representation of the Sierpinski triangle
# (iteration 5).]
