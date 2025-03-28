class Node:
    def __init__(self, data):
        self.data = data    # 데이터 저장
        self.next = None    # 다음 노드를 가리키는 포인터


class LinkedList:
    def __init__(self):
        self.head = None  # 첫 번째 노드(헤드)를 저장

    def append(self, data):
        """리스트 끝에 데이터 추가"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """리스트 앞에 데이터 추가"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """데이터 삭제"""
        if not self.head:
            return
        
        # 삭제할 노드가 헤드인 경우
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        """데이터 검색"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        """연결 리스트 출력"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
