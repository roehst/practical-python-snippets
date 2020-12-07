#!python3

from abc import ABC, abstractmethod, abstractproperty


class AbstractStack(ABC):

    @abstractmethod
    def push(self, value):
        ...

    @abstractmethod
    def pop(self):
        ...

    @abstractproperty
    def size(self):
        ...

    @property
    def empty(self):
        return self.size == 0


class ListBackedStack(AbstractStack):

    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        item = self._items[-1]
        self._items = self._items[:-1]
        return item

    @property
    def size(self):
        return len(self._items)


class ArrayBackedStack(AbstractStack):

    def __init__(self, capacity=1000):
        self._items = [None] * capacity
        self._capacity = capacity
        self._cur = 0

    def push(self, value):
        self._items[self._cur] = value
        self._cur += 1

    def pop(self):
        self._cur -= 1
        return self._items[self._cur]

    @property
    def size(self):
        return self._cur


def test_implementation(stack: AbstractStack):

    stack.push(1)
    stack.push(2)

    assert not stack.empty

    assert stack.pop() == 2
    assert stack.pop() == 1

    assert stack.empty


test_implementation(ListBackedStack())
test_implementation(ArrayBackedStack())
