# 노드 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 링크드 리스트 클래스
class LinkedList:
    def __init__(self):
        self.head = None

    # 링크드 리스트에 데이터를 추가하는 메서드
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # 링크드 리스트의 모든 노드 데이터를 출력하는 메서드
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next


# 사용 예시
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.print_list()  # 출력: 1 -> 2 -> 3 -> 4 ->
