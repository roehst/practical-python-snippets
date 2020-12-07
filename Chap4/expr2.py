#!python3

from abc import ABC, abstractmethod

class Expr(ABC):

    @abstractmethod
    def eval(self, environment):
        ...

class Num(Expr):

    def __init__(self, value):
        self.__value = value

    def eval(self, environment):
        return self

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return "Num(" + str(self.__value) + ")"

class BinOp(Expr):

    def __init__(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2

    def eval(self, environment):
        return Num(
            self.op(self.__value1.eval(environment).value, 
                    self.__value2.eval(environment).value)
        )

    @abstractmethod
    def op(self, a, b):
        ...

class Add(BinOp):

    def op(self, a, b):
        return a + b

class Mul(BinOp):

    def op(self, a, b):
        return a * b

class Mod(BinOp):

    def op(self, a, b):
        return a % b        

class Var(Expr):

    def __init__(self, name):
        self.__name = name

    def eval(self, environment):
        return environment[self.__name].eval(environment)


env = {
    "X": Num(10)
}

expr = Add(Var("X"), Mul(Num(12), Num(4)))

print(expr.eval(env))

expr = Mod(Add(Var("X"), Mul(Num(12), Num(4))), Num(13))

print(expr.eval(env))