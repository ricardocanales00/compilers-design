from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

import asm

class DataGenerator(marzoListener):
    def __init__(self):
        self.r = ''
        self.stack = []