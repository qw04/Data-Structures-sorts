from math import sqrt

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n


class hashTable:
    def __init__(self):
        self.size = 101
        self.table = [[None] for x in range(101)]

    def hashingFunction(self,value):
        value = list(str(value**2))
        l = len(value)
        if l == 1:
            key = int('0'+str(value[0]))

        elif l == 2:
            key = int(str(value[0]) + str(value[1]))
            return key
        else:
            if l%2 == 0:
                key = int(str(value[int(l/2)])+str(value[int((l/2)+1)]))
            else:
                x = int((l-1/2))- 1
                key = int(str(value[x-1])+str(value[x]))
        return key

    def checkError(self):
        bol = False
        for i in range(len(self.table)):
            if self.table[i] == [None]:
                bol = True
        return not(bol)
    
    def insertValue(self,value):
        if self.checkError():
            raise OverflowError('no space left')
        else:
            key = self.hashingFunction(value)
            generator = prime_generator()
            position = key % 101
            bol = True
            while bol:
                position = (position + next(generator))%(101)
                if (self.table[position] != [None]) or (self.table[position] != 'Deleted'):
                    bol = False
                
                
                
            self.table[position] = value
        
    def search(self,value):
        key = self.hashingFunction(value)
        generator = prime_generator()
        n = 0
        position = key % 101
        bol = True
        while self.table[position] != value:
            position = (position + next(generator))%(101)
            n = n+1 
            if (self.table[position] == [None]) or (n == 101):
                bol = False
                break
            
        if bol == True:
            return position
        else:
            return 'not found'
            

    def delete(self,value):
        a = self.search(value)
        if a == 'not found':
            print('underflow error')

        else:
            self.table[a] = 'Deleted'
        

    def __str__(self):
       return f'{self.table}'

    

a = hashTable()


