"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""


import itertools
 
List_1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] #List to be flattened
 
List_flat = list(itertools.chain(*List_1))
 
print(List_flat)
