"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""

def flatten_list(strArr):
    if not strArr:
        return []
    elif isinstance(strArr[0],list):
        return (flatten_list(strArr[0])+flatten_list(strArr[1:]))
    else:
        return [strArr[0]]+flatten_list(strArr[1:])
        
print(flatten_list(eval(input())))