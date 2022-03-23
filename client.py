from antlr import *
import sys

def GenCode(pruebaListener):
    def enterProgram(self, ctx:pruebaParser.ProgramContext):
        print(".text")

    def exitPrimaria(self, ctx:pruebaParser.ProgramContext):
        print("load $1, " + ctx.Numero)
    
    def exitSuma(self, ctx:pruebaParser.SumaContext):
        print("ADD")

def main():
    parser = marzoParser(CommonTokenStream(marzoLexer(FileStream("input.txt"))))
    tree = parser.program()



    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(declarations, tree)


if _name_ = '_main_':
    main()