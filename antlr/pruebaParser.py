# Generated from /Users/ricardolpzca/Downloads/GitHub/compiladores/antlr/prueba.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4\37\n\4\3\4\2\3\4\5\2\4\6\2\2")
        buf.write("\2 \2\t\3\2\2\2\4\r\3\2\2\2\6\30\3\2\2\2\b\n\5\4\3\2\t")
        buf.write("\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3")
        buf.write("\3\2\2\2\r\16\b\3\1\2\16\17\7\7\2\2\17\25\3\2\2\2\20\21")
        buf.write("\f\4\2\2\21\22\7\3\2\2\22\24\5\4\3\5\23\20\3\2\2\2\24")
        buf.write("\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\5\3\2\2\2\27")
        buf.write("\25\3\2\2\2\30\31\7\4\2\2\31\32\5\4\3\2\32\33\7\5\2\2")
        buf.write("\33\36\5\6\4\2\34\35\7\6\2\2\35\37\5\6\4\2\36\34\3\2\2")
        buf.write("\2\36\37\3\2\2\2\37\7\3\2\2\2\5\13\25\36")
        return buf.getvalue()


class pruebaParser ( Parser ):

    grammarFileName = "prueba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'if'", "'then'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Numero", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Numero=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pruebaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return pruebaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = pruebaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.expression(0)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==pruebaParser.Numero):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pruebaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pruebaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pruebaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pruebaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(pruebaParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pruebaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = pruebaParser.PrimariaContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 12
            self.match(pruebaParser.Numero)
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pruebaParser.SumaContext(self, pruebaParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 14
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 15
                    self.match(pruebaParser.T__0)
                    self.state = 16
                    self.expression(3) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pruebaParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pruebaParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(pruebaParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.StatementContext)
            else:
                return self.getTypedRuleContext(pruebaParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = pruebaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            localctx = pruebaParser.IfContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(pruebaParser.T__1)
            self.state = 23
            self.expression(0)
            self.state = 24
            self.match(pruebaParser.T__2)
            self.state = 25
            self.statement()
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 26
                self.match(pruebaParser.T__3)
                self.state = 27
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




