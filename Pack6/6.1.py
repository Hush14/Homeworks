import dlb


class DoublyLinkedCircularList(dlb.DoublyLinkedBase):
    def __init__(self):
        self._header = dlb._Node(None, None, None)
        self._header._prev = self._header
        self._header._next = self._header
        self._size = 0

    def add_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        self._insert_between(e, self._header._prev, self._header)

    def cut_first(self):
        if self.is_empty():
            raise dlb.Empty('List is empty')
        else:
            self._delete_node(self._header._next)

    def cut_last(self):
        if self.is_empty():
            raise dlb.Empty('List is empty')
        else:
            self._delete_node(self._header._prev)

    def __str__(self):
        s = '['
        if self._size != 0:
            t = self._header._next
            s += str(t._element)
            while t._next._element != None:
                t = t._next
                s += ' ' + str(t._element)
        s += ']'
        return s


a = DoublyLinkedCircularList()
a.add_first('ZAMAY')
a.cut_first()
a.add_first('ANTIHYPE')
a.add_last('GNOYNIJ')
a.cut_last()
a.add_last('RENESSANS')

x = a._header._next
print('Example: ')
k = 0
while k < 3:
    if x._element != None:
        print(x._element)
    x = x._next
    if x._element == None:
        k += 1

print('List: ', a)
