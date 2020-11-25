from classes.LinkedList import LinkedList, Node


def ass_node():
    N = Node(1)
    # b = Node(2, a)
    # c = Node(3, a, b)
    # assert1(a.value == 1, "newly created node''s value is wrong")
    assert N.value == 1
    assert N.next is None
    assert N.prev is None
    print("Node is ok")


def ass_is_empty():
    LL = LinkedList()
    assert LL.is_empty()
    print("is_empty is ok")
    # not all results were tested
    LL.add_back(1)
    LL.add_back(1)
    LL.add_back(1)
    LL.add_back(1)
    assert LL.is_empty() is False


def ass_add_back():
    LL = LinkedList()
    first = 1
    second = 2
    fn = LL.add_back(first)
    sn = LL.add_back(second)
    assert fn.prev is None
    assert fn.next == sn
    assert sn.next is None
    print("add_back is ok")

    assert sn.prev == fn
    tn = LL.add_back(3)
    # assert


def ass_add_front():
    LL = LinkedList()
    first = 1
    second = 2
    fn = LL.add_front(first)
    assert fn.prev is None
    assert fn.next is None
    sn = LL.add_front(second)
    assert fn.prev == sn
    assert fn.next is None
    assert sn.prev is None
    print("add_front is ok")

    assert sn.next == fn
    # tn
    # assert


def ass_remove_node():
    ll = LinkedList()
    first = 1
    fn = ll.add_front(first)
    ll.remove_node(fn)
    assert ll.is_empty()
    print("remove_node is ok")

    ll = LinkedList()
    f = ll.add_back(1)
    s = ll.add_back(1)
    t = ll.add_back(1)
    assert ll.find_first(1) == f
    ll.remove_node(f)
    assert ll.find_first(1) == s


def ass_find_first():
    a = LinkedList()
    a.add_back(1)
    a.add_back(2)
    assert a.find_first(1).value == 1
    print("find_first is ok")

    # add front
    # assert find first


def ass_add_after():
    print("Creating new list")
    ll = LinkedList()
    print("addback 1")
    fn = ll.add_back(1)
    print("addback 2")
    sn = ll.add_back(2)
    print(ll)
    tn = ll.add_after(fn, 3)
    assert fn.next == tn
    assert sn.prev == tn
    assert tn.next == sn
    assert tn.prev == fn
    print("add_after is ok")


def ass_add_before():
    ll = LinkedList()
    fn = ll.add_back(1)
    sn = ll.add_back(2)
    assert fn.next == sn
    assert sn.prev == fn
    tn = ll.add_before(sn, 3)
    assert fn.next == tn
    assert sn.prev == tn
    print("add_before is ok")


def ass_find_next():
    ll = LinkedList()
    k = ll.add_front(44)
    fn = ll.add_back(1)
    sn = ll.add_back(2)
    tn = ll.add_back(1)
    assert ll.find_next(sn, 0) is None
    assert ll.find_next(sn, 1) == tn
    print("find_next is ok")
    assert ll.find_next(tn, 1) == tn
    assert ll.find_next(k, 1) == fn


def ass_get_at():
    ll = LinkedList()
    # a.add_front(None)
    assert ll.get_at(2) is None
    fn = ll.add_back(1)
    sn = ll.add_back(2)
    tn = ll.add_back(1)
    assert ll.get_at(2) == tn
    print("get_at is ok")


def linked_list_tester():
    ass_is_empty()
    ass_add_back()
    ass_add_front()
    ass_remove_node()
    ass_find_first()
    ass_add_after()
    ass_add_before()
    ass_find_next()
    ass_get_at()


linked_list_tester()


def assert1(b, message):
    if not b:
        raise AssertionError(message)
