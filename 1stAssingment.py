class Counter():
    val = 0
    
    def incr(self):
        self.val +=1
        
    def decr(self):
        self.val -=1
        
    def incrby(self,n):
        self.val += n  
              
    def decrby(self,n):
        self.val -= n
            
vimal = Counter()
vimal.incr()
print(vimal.val)

vimal.decr()
print(vimal.val)

vimal.decrby(30)
print(vimal.val)

vimal.incrby(45)
print(vimal.val)
        