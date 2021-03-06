import turtle
import time
from antlr4 import *

from GCodesLexer import GCodesLexer
from GCodesParser import GCodesParser
from GCodesVisitor import GCodesVisitor

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'gcode_script')

def main():
    lexer = GCodesLexer( FileStream(filename))
    token_stream = CommonTokenStream(lexer)
    parser = GCodesParser(token_stream)
    visitor = GCodesVisitor()

    while True: 
        tree = parser.start()
        if tree.expr() == None:
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)

    time.sleep(4)


if __name__ == '__main__':
    main()
