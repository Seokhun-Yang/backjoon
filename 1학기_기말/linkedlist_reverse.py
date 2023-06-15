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

    def reverse(self):
        if self.length <= 1:
            return
        ahead = self.head.next
        prev = self.head
        prev.next = None
        while ahead:
            self.head = ahead
            ahead = ahead.next
            self.head.next = prev
            prev = self.head


mylist = LinkedList()
for i in range(5):
    mylist.append(i)

print("원래 리스트: ", end = " ")
print(mylist)

mylist.reverse()
print("뒤집은 리스트: ", end = " ")
print(mylist)
