# Generated from /Users/ricardolpzca/Downloads/GitHub/compiladores/antlr/prueba.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pruebaParser import pruebaParser
else:
    from pruebaParser import pruebaParser

# This class defines a complete listener for a parse tree produced by pruebaParser.
class pruebaListener(ParseTreeListener):

    # Enter a parse tree produced by pruebaParser#program.
    def enterProgram(self, ctx:pruebaParser.ProgramContext):
        pass

    # Exit a parse tree produced by pruebaParser#program.
    def exitProgram(self, ctx:pruebaParser.ProgramContext):
        pass


    # Enter a parse tree produced by pruebaParser#suma.
    def enterSuma(self, ctx:pruebaParser.SumaContext):
        pass

    # Exit a parse tree produced by pruebaParser#suma.
    def exitSuma(self, ctx:pruebaParser.SumaContext):
        pass


    # Enter a parse tree produced by pruebaParser#primaria.
    def enterPrimaria(self, ctx:pruebaParser.PrimariaContext):
        pass

    # Exit a parse tree produced by pruebaParser#primaria.
    def exitPrimaria(self, ctx:pruebaParser.PrimariaContext):
        pass


    # Enter a parse tree produced by pruebaParser#if.
    def enterIf(self, ctx:pruebaParser.IfContext):
        pass

    # Exit a parse tree produced by pruebaParser#if.
    def exitIf(self, ctx:pruebaParser.IfContext):
        pass



del pruebaParser