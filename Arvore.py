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
           
   


    