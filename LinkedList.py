# doubly linked list implementation
class Node:
    def __init__(self, value=None, next_ptr=None, prev_ptr=None):
        self.value = value
        self.next = next_ptr
        self.prev = prev_ptr

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.__head = None

    def get_at(self, index):
        if self.is_empty():
            return None
        if index < 0:
            raise IndexError("No such index: " + str(index))
        curr_index = 0
        curr = self.__head
        while curr_index != index:
            curr = curr.next
            curr_index += 1
            if curr is None:
                raise IndexError("No such index: " + str(index))
        return curr

    def is_empty(self):
        return self.__head is None

    def add_back(self, value):
        if self.is_empty():
            self.__head = Node(value)
            return self.__head
        else:
            curr = self.__head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)
            curr.next.prev = curr
            return curr.next

    def add_front(self, value):
        if self.is_empty():
            self.__head = Node(value)
        else:
            cur = Node(value)
            cur.next = self.__head
            self.__head.prev = cur
            self.__head = cur
        return self.__head

    def remove_node(self, node):
        if node.next is None and node.prev is None and self.__head == node:
            self.__head = None
            return
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node == self.__head:
            self.__head = self.__head.next

    # the first Node in LinkedList with value equal to the given
    # None - if no such node
    def find_first(self, value):
        if self.is_empty():
            return None
        curr = self.__head
        if curr.value == value:
            return curr
        while curr.next is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def add_after(self, node, value):
        curr = Node(value)
        if node.next is not None:
            node.next.prev = curr
            curr.next = node.next
        node.next = curr
        curr.prev = node
        return curr

    def add_before(self, node, value):
        curr = Node(value)
        if node.prev is not None:
            node.prev.next = curr
            curr.prev = node.prev
        curr.next = node
        node.prev = curr
        return curr

    def find_next(self, node, value):
        if node is None:
            return None
        while node is not None:
            if node.value == value:
                return node
            node = node.next
        return None

    def __repr__(self):
        a = "Hola! "
        curr = self.__head
        while curr is not None:
            a += str(curr)
            curr = curr.next
            a += ' '
        return a









# #
# ll = LinkedList()
# n = ll.add_back(10)
# search_value = 22
# ll.add_back(search_value)
# ll.add_back(9999)
# ll.add_back(9992)
# ll.add_back(333)
# ll.add_back(search_value)
# ll.add_after(n, 55)
# ll.add_back(797979)
# ll.add_back(search_value)
# ll.add_back(search_value)
# print("List:", ll)
# print(ll.get_at(11))
# exit()
# # n22 = ll.find_first(22)
# # print("n22:", n22)
# # print("n22.next:", n22.next)
# # n22 = ll.find_next(n22.next, 22)
# # print("n22:", n22)
# # print("n22.next:", n22.next)
#
# #
# count = 0
# a = ll.find_first(search_value)
# while a is not None:
#     count += 1
#     print(a, a.next)
#     a = ll.find_next(a.next, search_value)
# print(count)
#
#
# #
# exit()
# print(ll.is_empty())
# first_node = ll.add_back(10)
# # ll.remove_node(first_node)
# ll.find_first(3)
# print(ll.is_empty())
# ll.add_back(55)
# print(ll.is_empty())
# n = ll.add_back(111)
# print(n)
#
# ll.add_back(666)
# print(ll.is_empty())
# print(str(first_node))
#
# n = ll.find_first(55)
# print(n)
# print(n.next)
#
# print(ll.find_first(10))

# value = 10
# ll.add_back(value)
# node = ll.add_front(value)
# print(node.value)
# ll.remove_node(node)
# new_added_node = ll.add_after(node, value)  # add new node after given node and return newly created node
# new_added_node = ll.add_before(node, value)
# print(ll)
