class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("스택이 비어 있어 pop 작업을 진행할 수 없습니다.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("스택이 비어 있어 peek 작업을 진행할 수 없습니다.")

    def size(self):
        return len(self.items)


# 사용 예시
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 출력: 3
print(stack.peek())  # 출력: 2
