# Generated from /Users/ricardolpzca/Downloads/GitHub/compiladores/antlr/prueba.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pruebaParser import pruebaParser
else:
    from pruebaParser import pruebaParser

# This class defines a complete generic visitor for a parse tree produced by pruebaParser.

class pruebaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pruebaParser#program.
    def visitProgram(self, ctx:pruebaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#suma.
    def visitSuma(self, ctx:pruebaParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#primaria.
    def visitPrimaria(self, ctx:pruebaParser.PrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#if.
    def visitIf(self, ctx:pruebaParser.IfContext):
        return self.visitChildren(ctx)



del pruebaParser