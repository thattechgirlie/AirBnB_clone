#!/usr/bin/python3
"""Define the HBnB console"""

import cmd
import re
from shlex import split

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    s_brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if s_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl

        else:
            lexer = split(arg[:curly_braces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
