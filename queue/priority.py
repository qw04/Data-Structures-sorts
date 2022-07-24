# cook your dish here
class queue(): 

    def __init__(self,max_element,priority): 
       
        
        self.max_element = max_element 
        self.lst = [[0 for x in range(0)] for x in range(len(priority))]
        self.priority = priority
        
    def full(self):
        a = 0
        for i in range(len(priority) - 1):
            a = a + len(self.lst[i])
        return a == self.max_element

    def empty(self):
        a = 0
        for i in range(len(priority) - 1):
            a = a + len(self.lst[i])
        return a == 0 
 

    def enque(self): 
        
        if self.full() == False: 
            a = input()
            if
            self.lst.append(a)
            
            

    def deque(self): 
        
        if self.empty() == False: 
            a = self.lst.pop()
            print(a)

    def front(self):
        return self.lst[0]


if __name__ == '__main__': 
    print('just for defining class it isnt meant to be run') 
