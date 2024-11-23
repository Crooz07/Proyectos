class DequeNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):

        return self.head is None

    def insert_left(self, data):

        new_node = DequeNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_right(self, data):

        new_node = DequeNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_left(self):

        if self.is_empty():
            raise IndexError("remove from empty deque")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def remove_right(self):

        if self.is_empty():
            raise IndexError("remove from empty deque")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return data

    def peek_left(self):

        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.head.data

    def peek_right(self):

        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.tail.data


dq = Deque()
dq.insert_left(1)
dq.insert_right(2)
dq.insert_left(0)

print("Peek izquierda:", dq.peek_left())
print("Peek derecha:", dq.peek_right())
print("Eliminar izquierda:", dq.remove_left())
print("Eliminar derecha:", dq.remove_right())
