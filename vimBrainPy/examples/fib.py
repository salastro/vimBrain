from ..vb import converter, interpreter

program = converter("""
>++++++++++>+>+[
    [+++++[>++++++++<-]>.<++++++[>--------<-]+<<<]>.>>[
        [-]<[>+<-]>>[<<+>+>-]<[>+<-[>+<-[>+<-[>+<-[>+<-[>+<-
            [>+<-[>+<-[>+<-[>[-]>+>+<<<-[>+<-]]]]]]]]]]]+>>>
    ]<<<
]
""")
interpreter(program)

# This program doesn't terminate; you will have to kill it.
# Daniel B Cristofani (cristofdathevanetdotcom)
# http://www.hevanet.com/cristofd/brainfuck/
