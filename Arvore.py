import NodeArvore as no
class arvore:
    def _init_(self, no):
        self.root = no
        
    def insert(self, node, data):
        if node is None:
           new_node = no.NodeArvore(self, data, node.ant)
        if self.root._data < data:
           self.root.esq = no.NodeArvore(self, self.root.esq, data)
        else:
           self.root.dir = no.NodeArvore(self, self.root.dir, data)
    