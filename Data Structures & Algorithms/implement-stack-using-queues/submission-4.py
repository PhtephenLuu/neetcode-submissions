class MyStack:

    def __init__(self):
        self.elements = deque() 

    def push(self, x: int) -> None:
        self.elements.append(x)
        for i in range(len(self.elements) - 1): 
            self.elements.append(self.elements.popleft())

    def pop(self) -> int:
        return self.elements.popleft()

    def top(self) -> int:
        return self.elements[0]
        

    def empty(self) -> bool:
        return len(self.elements) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()