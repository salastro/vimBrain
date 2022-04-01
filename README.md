# vimBrain
![vimBrain](vimBrain.png)

vimBrain is a brainfuck-based vim-inspired esoteric programming language.
## vimBrainPy
Currently, the only interpreter available is written in Python.
### Goals
There are few goals that the current Python interpreter tries to achieve:
1. Beautiful: the code structure should "look" beautiful (hence the use of
   `match-case` statements).
2. Minimal: whatever is being done should be done in as few lines of codes as
   possible as long it does not make the code "look" ugly (hence the use of
   inline `if-else` statements and semicolons).
3. Independent: no libraries should be used for whatever purpose.
### Examples
To run examples type `python -m vimBrainPy.examples.<whatever>` in the
repository's home directory.
