class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
def main():
    Node1 = Node( "Apple") #head
    Node2 = Node("Orange")
    Node3 = Node("Pear")
    Node1.next = Node2
    Node2.next = Node3
    
    InsertData(Node1,'bannana',Node1.next)
    DeleteData(Node1, 'bannana')
    printList(Node1)
    
def printList(head):
    node = head 
    while node != None: 
        print(node.data)
        node = node.next


def InsertData(head,data,location):
    node = head #give the head node
    while node != None:
        if node.next == location:
            node = node.next
            NewNode = Node(data)
            NewNode.next = node.next
            node.next = NewNode
            break
        else:
            node = node.next

def DeleteData(head,data):
    current = head
    previous = None
    found = False
    while not found:
        if current.data == data:
            found = True
        else:
            previous = current
            current = current.next

    if previous == None:
        head = current.next
    else:
       previous.next = current.next

    return head


main()
