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

    def eval(self, environment: AbstractEnv):
        return environment.fetch(self.__name).eval(environment)


class AbstractEnv(ABC):

    @abstractmethod
    def fetch(self, name):
        ...

    @abstractmethod
    def bind(self, name, value):
        ...


class DictEnv(AbstractEnv):

    def __init__(self):
        self.__values = {}

    def fetch(self, name):
        return self.__values[name]

    def bind(self, name, value):
        self.__values[name] = value


class ListEnv(AbstractEnv):

    def __init__(self):
        self.__values = []

    def fetch(self, name):
        return [
            v for (k, v) in self.__values
            if k == name
        ][0]

    def bind(self, name, value):
        self.__values.insert(0, (name, value))


env = DictEnv()
env.bind("X", Num(10))
env.bind("Y", Num(11))

expr = Add(Var("X"), Mul(Num(12), Num(4)))

print(expr.eval(env))

expr = Mod(Add(Var("X"), Mul(Num(12), Num(4))), Num(13))

print(expr.eval(env))

expr = Mul(Mod(Add(Var("X"), Mul(Num(12), Num(4))), Num(13)), Var("Y"))

print(expr.eval(env))
