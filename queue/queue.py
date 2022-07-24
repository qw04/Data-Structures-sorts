class queue(): 
    ''' 
    abstract datastructure 
    ''' 
    def __init__(self,max_element): 
        ''' 
        - max element 
        - lst 
        - head 
        - tail 
        ''' 
        self.max_element = max_element 
        self.head = 0 
        self.tail = -1 
        self.lst = []
        
    def full(self): 
        ''' 
        checks if full 
        ''' 
        return self.tail == self.max_element - 1 

    def empty(self): 
        ''' 
        checks if empty 
        ''' 
        return self.head == self.tail + 1 
 

    def enque(self): 
        ''' 
        supposed to enqueue 
        ''' 
        if self.full() == False: 
            self.tail = self.tail + 1 
            objct = str(input('object:')) 
            self.lst.append(objct) 

    def deque(self): 
        ''' 
        supposed to dequeue 
        ''' 
        if self.empty() == False: 
            self.head = self.head + 1 

if __name__ == '__main__': 
    print('just for defining class it isnt meant to be run') 
