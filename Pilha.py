import Node as no

class Pilha:
    def __init__(self):
        self.top = None
    
    def Empty(self):
        if self.top is None:
            return True
        
    def Empilhar(self, data):
        new_node = no.Node(data)
        current = self.top
        if current == None:
            self.top = new_node
        else:
            while current != None:
                prevNode = current
                current = current.next
            
            prevNode.next = new_node    
            
    
    def Display(self):
        current = self.top
        
        if self.top == None:
            print("Pilha vazia")
        else:
            while current != None:
                print(current.data)
                current = current.next
            
    def Desempilhar(self):
        current = self.top
             
        if current is None:
            print("Pilha vazia")
        else:
            while current.next != None:
                prevNode = current
                current = current.next
            
            prevNode.next = None
            
                   
        

            


           
