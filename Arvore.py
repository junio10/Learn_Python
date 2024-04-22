import NodeArvore as no
class Arvore:
    def __init__(self, no):
        self.root = no
                
    def insert_Recursive(self, data, root):
        if root is None:
            return no.NodeArvore(data, root) 
        if root.data > data:
           self.root.esq = self.insert_Recursive(data, root.left)
        else:
           self.root.dir = self.insert_Recursive(data, root.right)
        return root
           
    def insert(self, data):
         self.root = self.insert_Recursive(data, self.root)
           
   


    