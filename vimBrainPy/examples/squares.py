from ..vb import converter, interpreter

program = converter("""
++++[>+++++<-]>[<+++++>-]+<+[
    >[>+>+<<-]++>>[<<+>>-]>>>[-]++>[-]+
    >>>+[[-]++++++>>>]<<<[[<++++++++<++>>-]+<.<[>----<-]<]
    <<[>>>>>[>>>[-]+++++++++<[>-<-]+++++++++>[-[<->-]+[<<<]]<[>+<-]>]<<-]<<-
]
""")
interpreter(program)

# [Outputs square numbers from 0 to 10000.
# Daniel B Cristofani (cristofdathevanetdotcom)
# http://www.hevanet.com/cristofd/brainfuck/]
