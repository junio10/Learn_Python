import Node as no
   
class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   
   def Insert(self, Data):
       
      new_Node = no.Node(Data)
      
      if self.head == None:
         self.head = new_Node
         self.tail = new_Node
         
      else:
         self.tail.next = new_Node

          
   def Delete(self, data):
    
      if self.head == None:
         print("Linked List is Empty")
      else:      
         current = self.head
         
         if current.data == data:
            self.head = current.next
         else:
               while current.data != data:
                  prevNode = current
                  current = current.next
               
               prevNode.next = current


   def Display(self):
      current = self.head
      if current is None:
         print("Linked List is Empty")
      else:                
         while current != None:
            print(current.data, end = " ")
            current = current.next

            

                  
         
         
      

            
            

         
      