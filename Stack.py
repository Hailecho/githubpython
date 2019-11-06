# creating a stack class

class Stack(object):
    """ Creating a Stack class"""
    def __init__(self):
        self._List = []
    def push(self, x):
        self._List.append(x)
    def pop(self):
        return self._List.pop()
    def empty(self):
        return len(self._List) == 0

# Test using pytest or mypy