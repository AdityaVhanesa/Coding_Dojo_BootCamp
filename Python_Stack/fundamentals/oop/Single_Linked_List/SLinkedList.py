from node import Node
import time


class SList:
    def __init__(self):
        self.head = None
        self.length = 0

    def shift(self, value):
        new_node = Node(value)
        current_head = self.head
        new_node.next, self.head = current_head, new_node
        self.length += 1
        return self

    def push(self, value):
        if self.head is None:
            self.shift(value)
        else:
            new_node = Node(value)
            runner = self.head
            while runner.next is not None:
                runner = runner.next
            runner.next = new_node

        self.length += 1
        return self

    def unshift(self):
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        return current_head

    def pop(self):
        if not self.length:
            return self.head

        second_last_head = self.head
        if self.length == 1:
            self.unshift()
        else:
            while second_last_head.next.next is not None:
                second_last_head = second_last_head.next

        last_head = second_last_head.next
        second_last_head.next = None
        self.length -= 1
        return last_head

    def remove_val(self, value):
        previous_node = None
        current_node = self.head
        if current_node is None:
            return

        isMatch = False
        while current_node.next is not None:
            if current_node.value == value:
                isMatch = True
                break
            previous_node = current_node
            current_node = current_node.next
        else:
            if not isMatch and current_node.value == value:
                isMatch = True

        if previous_node is None and isMatch:
            self.unshift()
        elif isMatch:
            temp_node = current_node.next
            previous_node.next = temp_node
            self.length -= 1
        else:
            return

    def insert_at(self, value, n):
        if not n:
            self.shift(value)
            return

        if n == self.length:
            self.push(value)
            return

        previous_node = None
        current_node = self.head
        count = 0
        while count != n - 1:
            current_node = current_node.next
            count += 1

        temp_node = current_node.next
        current_node.next = Node(value)
        current_node.next.next = temp_node





