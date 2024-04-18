import Node as no
class Fila:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
              
    def enqueue(self, data):
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
          
           
           
    
    def dequeue(self):
        if self.front is None:
            print("Fila Vazia")
        elif self.size == 1:
            print(self.front.data)
            self.front = None
            self.rear = None            
            self.size = 0
        else:
            print(self.front.data)
            self.front = self.front.next
            self.size -= 1
    
    def display(self):
        current = self.front
        
        if current is None:
            print("Fila Vazia")
        else:
            while current is not None:
                print(current.data, end = " ")   
                current = current.next

            
       
            
            
            
        
      


    
    