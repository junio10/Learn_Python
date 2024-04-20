import NodeArvore as no
class Arvore:
    def __init__(self, no):
        self.root = no
                
    def insert_Recursive(self, data, root):
        if root is None:
            return no.NodeArvore(data, root) 
        if self.root._data < data:
           self.root.esq = insert_Recursive(self, data, root.esq)
        else:
           self.root.dir = insert_Recursive(self, data, root.esq)
        return root
           
    def insert(self, data):
         self.root = insert_Recursive(self, data, self.root)
           
   


    