class Stack:

    def __init__(self):
        self.__elements = []
        self.__last_index = -1

    def put(self, value):
        if len(self.__elements) - 1 == self.__last_index:
            self.__elements.append(value)
            self.__last_index += 1
        else:
            self.__last_index += 1
            self.__elements[self.__last_index] = value

    def peek(self):
        if not self.is_empty():
            return self.__elements[self.__last_index]
        return None

    def pop(self):
        if self.is_empty():
            raise LookupError("Stack is empty")
        self.__elements[self.__last_index] = None
        self.__last_index -= 1

    def is_empty(self):
        return self.__last_index == -1

