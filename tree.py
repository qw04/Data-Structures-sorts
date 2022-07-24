class Node:
    
    def __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return f'data:{self.data}\n\n\t{self.data}\'s left:{self.left}\n\t{self.data}\'s right:{self.right}\n '
    def insert(self,data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
                
        elif data >= self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
            


a = Node(5)
a.insert(3)
a.insert(7)
a.insert(1)
a.insert(9)
print(a)
            
                
