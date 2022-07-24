class circular_queue():
    '''
    abstract becomes real
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
        self.n = 0
    def __str__(self):
        return ' '.join(self.lst) + f'\nhead:{self.head}\ntail:{self.tail}'

        
    def full(self):
        '''
        checks if full
        '''
        if self.n>3:
        	return self.tail == self.head - 1
        else:
        	return self.tail == self.max_element - 1

    def empty(self):
        '''
        big problem here if n > 3 then the condition for full and empty list is the same 
        '''
        return self.head == self.tail + 1
        

    def enque(self):
        '''
        supposed to enqueue
        '''
        if self.full() == False:
            objct = str(input('object:'))
            if self.n > 3:
                if self.head - 1 > 0:
                    self.tail = (self.tail+1)%4
                    self.lst[self.tail] = objct
                else:
                    self.lst[self.tail] = objct
            else:
                self.lst.append(objct)
                self.n = self.n +1
                self.tail = (self.tail + 1)
            
    def deque(self):
        '''
        supposed to dequeue
        '''
        if self.empty() == False:
            self.head = self.head + 1


if __name__ == '__main__':
    a = circular_queue(4)
