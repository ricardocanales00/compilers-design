from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

class GenCode(marzoListener):

    def __init__(self):
        self.r = ''
        self.stack []
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        self.r += asm.tpl_start;

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        print("load $1, " + ctx.Numero().getText())

    def exitSuma(self, ctx:marzoParser.SumaContext):
        self.stack.append(
            asm.tpl.substitute(
                right=self.stack.pop(),
                left=self.stack.pop()
            )
        )
