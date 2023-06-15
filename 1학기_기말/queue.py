class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("큐가 비어있어 dequeue 작업을 진행할 수 없습니다.")

    def size(self):
        return len(self.items)


# 사용 예시
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 출력: 1
print(queue.size())  # 출력: 2
