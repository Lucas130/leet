class Stack2queue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, value):
        self.push_stack.append(value)

    def pop(self):
        if not self.pop_stack:
            while (self.push_stack):
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop() if self.pop_stack else -1


class Queue2Stack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.top_value = -1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.top_value = x
        if not self.queue1:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return -1
        while self.queue1:
            item = self.queue1.pop(0)
            if self.queue1:
                self.top_value = item
                self.queue2.append(item)
            else:
                return item
        while self.queue2:
            item = self.queue2.pop(0)
            if self.queue2:
                self.top_value = item
                self.queue1.append(item)
            else:
                return item

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_value


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not self.queue1 and not self.queue2 else False

