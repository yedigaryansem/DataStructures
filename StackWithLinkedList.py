from classes.LinkedList import LinkedList


class Stack:
    def __init__(self):
        self.__in_stack = LinkedList()
        self.__stack_head = None

    def put(self, value):
        self.__stack_head = self.__in_stack.add_front(value)

    def peek(self):
        if self.is_empty():
            raise LookupError("Stack is empty")
        return self.__stack_head.value

    def pop(self):
        if self.is_empty():
            return False
        old_head = self.__stack_head
        self.__stack_head = old_head.next
        self.__in_stack.remove_node(old_head)
        return True

    def is_empty(self):
        return self.__in_stack.is_empty()

    def __repr__(self):
        return str(self.__in_stack)


s = Stack()
s.put(20)
s.put(30)
s.put(550)
print(s)
print("Removing", s.peek(), "Removed:", s.pop())
print("Removing", s.peek(), "Removed:", s.pop())
print("Removing", s.peek(), "Removed:", s.pop())
print("Removing", s.peek(), "Removed:", s.pop())
print("Removing", s.peek(), "Removed:", s.pop())
print("Removing", s.peek(), "Removed:", s.pop())




