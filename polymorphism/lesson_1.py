class Node:
    def __init__(self, value, node=None):
        self.next = node
        self.value = value

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def __repr__(self):
        acc = []
        current = self
        while current is not None:
            acc.append(current.get_value())
            current = current.get_next()
        return str(tuple(acc))


numbers = Node(1, Node(2, Node(3)))  # (1, 2, 3)
# print(numbers)
# print(numbers.get_value())  # 1
# print(numbers.get_next().get_value())   # 2
# print(numbers.get_next().get_next().get_value())    # 3
# print(numbers.get_next().get_next().get_next() is None)


def reverse(singly_linked_list):
    res = []
    value = singly_linked_list.get_value()
    next_list = singly_linked_list.get_next()
    res.append(value)
    while next_list is not None:
        value = next_list.get_value()
        next_list = next_list.get_next()
        res.append(value)

    def inner(list_):
        value = list_[-1]
        list_ = list_[:-1]
        if list_:
            return Node(value, inner(list_))
        else:
            return Node(value)

    value = res[-1]
    list_ = res[:-1]
    return Node(value, inner(list_))


print(reverse(numbers))
print(type(reverse(numbers)))
