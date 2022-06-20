class Node:
    def __init__(self,value=None,next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_ll(self):
        result = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            result+=f"{node.value}->"
            if node.next_node is None:
                result+="None"
            node = node.next_node

        print(result)

    def convert_to_list(self):
        container = []
        if self.head is None:
            return container
        node = self.head
        while node:
            container.append(node.value)
            node = node.next_node
        return container
        
    def insertFront(self,data):
        if self.head is None:
            self.head=Node(data,None) 
            self.last_node= self.head
        else:
            node1= Node(data,self.head)
            self.head = node1
    
    def insertEnd(self, data):
        if self.head is None:
            self.insertFront(data)
        else:
            node = Node(data, None)
            self.last_node.next_node = node
            self.last_node = node
            
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.value["id"] is int(user_id):
                return node.value
            node = node.next_node
        return None

ll= LinkedList()
#ll.insertFront(2)
#ll.insertFront(1)
ll.insertEnd(3)
ll.insertEnd(4)
ll.insertFront(2)
#node3 = Node(3,None)
#node2 = Node(2, node3)
#node1 = Node(1, node2)

#ll.head =node1
ll.print_ll()
