# x,y,z,n = input()

# l = []

# for a in range(0,int(x)+1):
#     for b in range(0,int(y)+1):
#         for c in range(0,int(z)+1):
#             if a+b+c != int(n):
#                 l.append([a,b,c])
# print(l)

# n = int(input())
# arr = map(int, input().split())
# list=[]
# for ch in arr:
#         list.append(ch)
# min=min(list[0],list[1])
# secondmin=max(list[0],list[1])
# for i in range(2,n):
#     if list[i]<min:
#         secondmin=min
#         min=list[i]
#     elif list[i]<secondmin and min != list[i]:
#         secondmin=list[i]
#     else:
#         if secondmin == min:
#             secondmin = list[i]

# print("2. Küçük Sayı : ",str(secondmin))

# if __name__ == '__main__':

#     list=[]
#     nameList=[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         list.append([name,score])

#     min=min(list[0][1],list[1][1])
#     secondmin=max(list[0][1],list[1][1])
#     for i in range(2,len(list)):
#         if list[i][1]<min:
#             secondmin=min
#             min=list[i][1]
#         elif list[i][1]<secondmin and min != list[i][1]:
#             secondmin=list[i][1]
#         else:
#             if secondmin == min:
#                 secondmin = list[i][1]
#     for j in range(len(list)):
#         if list[j][1]==secondmin:
#             nameList.append(list[j][0])
#     nameList.sort()
#     for k in range(len(nameList)):
#         print(nameList[k])

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     toplam=0.00
#     sonuc=0.00

#     for i in range(len(scores)):
#         toplam=toplam+float(student_marks[query_name][i])
#     sonuc=float(toplam/len(scores))
#     sonuc=round(sonuc,2)
#     a=len(str(sonuc).split('.')[1])
#     if a<2:
#         print(sonuc,end="0")
#     else:
#         print(sonuc)

# regex_integer_in_range = r"[0-9]"	# Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"()"	# Do not delete 'r'.


# import re
# P = input()
# list=[]
# k=0
# for i in str(P):
#     while k<2:
#         list.append(i)
#         k+=1
#         print(list)


# print (bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# def inn(p):
#     return 100000 <= int(p) <= 999999


# def imm(p):
#     l = []
#     for i in range(len(p) - 2):
#         l.append(p[i] != p[i + 2])

#     return all(l)


# def is_valid(p):
#     return (p.isdigit() and inn(p)) and (p != "110000" and p != "137370" )# and imm(p)


# def main():
#     p = input()
#     print(is_valid(p))


# main()

# import math
# import os
# import random
# import re
# import sys


# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# m = int(first_multiple_input[1])

# matrix = []
# a=False
# for _ in range(n):
#     matrix_item = input()
#     matrix+=matrix_item


# def output(a):
#     print('This is Matrix#  %!')

# output((bool(len(re.findall("[ThisisMatrix#%!]",matrix[1]))>0)))


# ----------------------------------------------------------------------------
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# if __name__ == '__main__':
#     N = int(input())
#     islemler = []
#     secimler=[]
#     arr = []
#     for _ in range(N):
#         secim, *line = input().split()
#         secimler.append(secim)
#         islemler.append(line) 
#     #print(secimler)
#     #print(islemler)

#     for i in range(len(secimler)):
#         if secimler[i] == "print":
#             print(arr)
#         elif secimler[i] == "insert":
#             arr.insert(int(islemler[i][0]), int(islemler[i][1]))
#         elif secimler[i] == "remove":
#             arr.remove(int(islemler[i][0]))
#         elif secimler[i] == "append":
#             arr.append(int(islemler[i][0]))
#         elif secimler[i] == "sort":
#             arr.sort()
#         elif secimler[i] == "pop":
#             arr.pop()
#         elif secimler[i] == "reverse":
#             arr.reverse()                
 
#---------------------------------------------------------------------

# class main():
#     n = int(input())
#     integer_list = tuple(map(int, input().split()))
#     if __name__ == '__main__':
#         print(hash(integer_list)*-1)
    
#---------------------------------------------------------------------
# import sys
# from collections import Counter
# X = int(input())
# numberShoes=[]
# #ayakkabı numraları
# numberShoes.append(input().split())

# buy=[]
# N = int(input())
# #numara-satış sayıları
# for _ in range(N):
#     shoes = input().split()
#     buy.append(shoes)
# print(buy)
# toplamsatis=0
# print(numberShoes) 
# for i in range(N):
#     for number in numberShoes[0]:
#         if buy[i][0]==number:
#             numberShoes[0].remove(number)
#             print(number+str(i))           
#             toplamsatis+=int(buy[i][1])
#             print(str(int(buy[i][1])))
#             break
#         else:pass    
# print(numberShoes)  
# print(toplamsatis)          

#---------------------------------------------------------------------

n,m=input().split()

A=[]
B=[]

for _ in range(int(n)):
    a = input().split()
    A.append(a[0])

for _ in range(int(m)):
    b = input().split()
    B.append(b[0]) 

#print(B)
ab=[]
for i in range(len(B)):
    for j in range(len(A)):
        if A.index('a',j)==j:# print(B[i]) 
            ab.append(A.index(A[j],j)+1)
            print(ab) 
            #print(A[j])
            #break
                        
# print(str(A[1]))
# print(B)
"""
5 2
a
a
b
a
b
a
b
"""
#--------------------

# A=[2,1,5,2,3,4,2]
# a=[]
# for i in range(len(A)):
#     if A.index(2,i)==i:
#         print(A.index(2,i))
#         #print(str(i))
    
