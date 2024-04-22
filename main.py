import ListaEnacadeada as lista
import Pilha as pilha
import Fila as fila
import Pilha as stack
import Arvore as arvore
import NodeArvore as no
# lista = lista.LinkedList()
# fila = fila.Fila()
#
# ### stack ####
#
# stack = stack.Pilha()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print("LIFO")
# stack.pop()
# stack.pop()
#
# print("fila")
# ## fila
# fila.enqueue(1)
# fila.enqueue(2)
# fila.enqueue(3)
# fila.display()
# print("FIFO", end="\n")
# fila.dequeue()
# fila.dequeue()
# fila.dequeue()
node = None
node = no.NodeArvore(10, None)
tree = arvore.Arvore(node)
#print(tree.root.data)
tree.insert(5)



