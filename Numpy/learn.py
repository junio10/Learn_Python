import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print("linha 0 do a: ", a[0])

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
arr = np.sort(arr)
print(arr)
print("tamanho do array: ", arr.size)
print("Dimensao do array: ", arr.ndim)
print("Modelo do array", arr.shape)

arr = np.array([32,4,43,221,1,11,18,10])
b = arr.reshape((4,2))
print(b)

print("fatiamento[inicio:fim:passo]")
#fatiamento em python
#[inicio : fim : incremento]

#inicio
# O elemento no índice início é incluído no resultado. 
# Se não for especificado, por padrão é 0 (o início da lista).

#fim:
#O elemento no índice fim não é incluído no resultado. 
# Se não for especificado, por padrão é o comprimento total da lista.

#passo: 
# Opcional. Determina o incremento entre os índices. 
# Se não for especificado, por padrão é 1.

# Criando uma lista de exemplo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#indexacao inversa
print(lista[-1], lista[-2], lista[-3], lista[-4], lista[-5])

# Fatiamento básico
print(lista[2:5])  # Saída: [2, 3, 4]

# Fatiamento com início e fim
print(lista[2:8])  # Saída: [2, 3, 4, 5, 6, 7]

# Fatiamento com passo
print(lista[1:9:2])  # Saída: [1, 3, 5, 7]

# Fatiamento omitindo início (começa do início da lista)
print(lista[:5])  # Saída: [0, 1, 2, 3, 4]

# Fatiamento omitindo fim (até o final da lista)
print(lista[5:])  # Saída: [5, 6, 7, 8, 9]

# Fatiamento reverso
print(lista[::-1])  # Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(lista[-8::]) # Saída: [[2, 3, 4, 5, 6, 7, 8, 9]




a = np.array([[1,2],[3,4]])

b = np.array([[4,3],[2,1]])

c= np.dot(a,b)

print(c)

d=a*b

print(d)

