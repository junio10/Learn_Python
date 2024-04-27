import NodeArvore as no
class Arvore:
    def __init__(self, no):
        self.root = no
                
    def insert_Recursive(self, data, root):
        if root is None:
            return no.NodeArvore(data, root) 
        if root.data > data:
           root.left = self.insert_Recursive(data, root.left)
        else:
           root.right = self.insert_Recursive(data, root.right)
        return root
           
    def insert(self, data):
         self.root = self.insert_Recursive(data, self.root)
         
    def delete(self, data, root):
        if root is not None:
           if root.data == data:
               root = None
               if root.left is not None or root.right is not None:
                   #para saber em qual filho do pai mexer no da direito ou na esquerda
                   if root.ant.left.data == data:
                       #fazer caso de substituicao recursiva
                       root.ant.left = root.left
                   else:                       
                       return
           else:
               self.delete(data, root.left)
               self.delete(data, root.right)
         
    def preOrder(self, root):
        if root is not None:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)
            
    def inOrder(self,root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)
            
    def posOrder(self, root):
        if root is not None:
            self.posOrder(root.left)
            self.posOrder(root.right)
            print(root.data)
           
   


    