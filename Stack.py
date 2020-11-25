class Stack:
    def __init__(self):
        self.__in_stack = []

    def put(self, value):
        self.__in_stack.append(value)

    def peek(self):
        if not self.is_empty():
            return self.__in_stack[len(self.__in_stack) - 1]
        return None

    def pop(self):
        del self.__in_stack[-1]

    def is_empty(self):
        if not self.__in_stack:
            return True
        return False


a = Stack()
print(a.is_empty())
a.put(5)
print(a.is_empty())
print(a.peek())
a.pop()
print(a.peek())
