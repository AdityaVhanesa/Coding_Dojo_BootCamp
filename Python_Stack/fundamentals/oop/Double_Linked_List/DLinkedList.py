from Node import node


class DList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        if not self.head:
            self.head = node(value)
            return

        current_runner = self.head
        new_node = node(value)
        while current_runner and current_runner.next:
            current_runner = current_runner.next

        new_node.previous = current_runner
        current_runner.next = new_node
        self.length += 1

        return self

    def shift(self, value):

        new_node = node(value)
        new_node.next, self.head = self.head, new_node
        if new_node.next:
            new_node.next.previous = self.head

        self.length += 1
        return self

    def unshift(self):
        if self.length == 1:
            self.head = None
            return

        current_head = self.head
        self.head = current_head.next
        self.head.previous = None
        self.length -= 1

        return self

    def pop(self):
        current_runner = self.head
        if not self.length:
            return
        elif self.length == 1:
            self.unshift()
        else:
            while current_runner.next.next is not None:
                current_runner = current_runner.next
            current_runner.next = None
            self.length -= 1

        return self

    def find_middle_node(self):
        if self.head is None:
            return None

        slow_runner = self.head
        fast_runner = self.head

        while fast_runner and fast_runner.next:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next

        return slow_runner

    def drop_duplicates(self):
        if self.head is None:
            return None

        runner_1 = self.head

        while runner_1 and runner_1.next:
            runner_2 = runner_1.next
            while runner_2:
                if runner_1.value == runner_2.value:
                    temp = runner_2.next
                    self.drop_node(runner_2)
                    runner_2 = temp
                else:
                    runner_2 = runner_2.next
            runner_1 = runner_1.next

    @staticmethod
    def drop_node( removal_node ):
        previous_node = removal_node.previous
        next_node = removal_node.next
        if previous_node and next_node:
            previous_node.next = next_node
            next_node.previous = previous_node
        elif previous_node and not next_node:
            previous_node.next = None
        elif not previous_node and next_node:
            next_node.previous = None

    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.value) + "->", end="")
            temp = temp.next
        print("NULL")


T = DList()
T.push("Kevin")
T.push("Elizabeth")
T.push("Elizabeth")
T.push("Kevin")
T.push("Aditya")
T.push("Kevin")
T.push("Nick")
T.push("Jason")
T.push("Elizabeth")
T.print_list()
T.drop_duplicates()
T.print_list()

