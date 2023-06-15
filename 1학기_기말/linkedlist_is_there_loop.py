class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = n
        self.length += 1


def is_there_loop(_list):
    node1 = node2 = _list.head
    while node1 and node1.next:
        node1 = node1.next.next  # 첫째 노드는 두 칸씩 이동
        node2 = node2.next  # 둘째 노드는 한 칸씩 이동
        if node1 == node2:
            return True
    return False


mylist = LinkedList()

for i in list(map(int, input().split())):
    mylist.append(i)

node = mylist.head

while node.next:
    node = node.next

node.next = mylist.head.next  # 순환 만들기
node = mylist.head

for _ in range(4):  # 그냥 출력하면 무한 루프이므로, 출력을 제한
    print(node.data, end=" -> ")
    node = node.next

print(node.data)
print(is_there_loop(mylist))
