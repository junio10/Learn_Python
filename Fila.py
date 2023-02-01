import Node as no
class Fila:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
              
    def push(self, data):
        new_node = no.Node(data)
        
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.size += 1
        
        elif self.size == 1:
            self.front.next = new_node
            self.rear = new_node
            self.size += 1
        else:
            current = self.front
            while current is not None:
                prevNode = current
                current = current.next
            
            prevNode.next = new_node
            self.rear = new_node
            self.size += 1
          
           
           
    
    def pop(self):
        if self.front is None:
            print("Fila Vazia")
        elif self.size == 1:
            self.front = None
            self.rear = None
            self.size = 0
        else:
            self.front = self.front.next
            self.front.size -= 1
    
    def Display(self):
        current = self.front
        
        if current is None:
            print("Fila Vazia")
        else:
            while current is not None:
                print(current.data, end = " ")   
                current = current.next

            
       
            
            
            
        
      


    
    