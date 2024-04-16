import Node as no

class Pilha:
    def __init__(self):
        self.top = None
        self.tail = None
        self.length = None
    
    def Empty(self):
        if self.top is None:
            return True
       
    def push(self,data):
         node = no.Node(data)
         if self.tail is None:
             self.tail = node
             self.top = node            
             self.length = 1;   
         else:
            self.tail.next = node
            self.tail = node
            self.length += 1
             
            
    def pop(self):
        if self.top is None:
            print("Empty")
        elif self.length == 1:
            print(self.tail.data)
            self.top = None
            self.tail = None
            self.ant = None
            self.length = 0
        else:
            aux = self.top
            ant = None
            while aux.next is not None:
                ant = aux
                aux = aux.next
            print(aux.data)
            ant.next = None
            self.tail = ant
            
            
                
              
    
            
                   
        

            


           
