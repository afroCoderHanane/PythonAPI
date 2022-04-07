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


ll= LinkedList()
node3 = Node(3,None)
node2 = Node(2, node3)
node1 = Node(1, node2)

ll.head =node1
ll.print_ll()
