class Stack(): 
    def __init__(self,max_elements): 
        self.max_elements = max_elements
        self.stack = [] 
    
    def __str__(self):
        return f'{self.stack}'
    
    def push(self,item): 
        if not(self.isfull()):
            print(f"{item} added") 
            self.stack.append(item) 
        else:
            print('Overflow error')

    def remove(self):
        if not(self.isempty()): 
            a = self.stack.pop()
            print(a,"popped") 
        else:
            print('Underflow error')

    def isfull(self): 
        return len(self.stack) == self.max_elements 

    def isempty(self): 
        return len(self.stack) == 0 
    
    def peek(self): 
        print("the top most item is{}".format(self.stack[len(self.stack)-1]))  

if __name__ == '__main__': 
    print('not meant to be run')
    print('only meant to be imported')