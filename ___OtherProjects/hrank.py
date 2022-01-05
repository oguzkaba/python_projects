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


# ------------------------Lists----------------------------------------------------
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

# n,m=input().split()

# A=[]
# B=[]

# for _ in range(int(n)):
#     a = input().split()
#     A.append(a[0])

# for _ in range(int(m)):
#     b = input().split()
#     B.append(b[0]) 

# #print(B)
# ab=[]
# for i in range(len(B)):
#     for j in range(len(A)):
#         if A.index('a',j)==j:# print(B[i]) 
#             ab.append(A.index(A[j],j)+1)
#             print(ab) 
            #print(A[j])
            #break
                        
# print(str(A[1]))
# print(B)
# """
# 5 2
# a
# a
# b
# a
# b
# a
# b
# """
#--------------------

# A=[2,1,5,2,3,4,2]
# a=[]
# for i in range(len(A)):
#     if A.index(2,i)==i:
#         print(A.index(2,i))
#         #print(str(i))


#-----------------------------------------------------
# """
# 4
# -1
# 10
# 16
# 18
# """







# class Person:
#     def __init__(self,initialAge):
#         # Add some more code to run some checks on initialAge
#         if initialAge<0:
#             print("Age is not valid, setting age to 0.")
        
            
#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         #print(str(self.age))
#         #age=self.age
#         global age
#         if age<13:  
#             print("You are young.")

#         elif age>=13 and age<18:
#             print("You are a teenager.")

#         else:    
#             print("You are old.")

#     def yearPasses(self):
#         # Increment the age of the person in here
#         global age
#         age=age+1
#         #print("deneme: "+str(age))
        
        

# t = int(input())
# for i in range(0, t):
#     age = int(input())         
#     p = Person(age)  
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()   
#     p.amIOld()
#     print("")    

#-----------------------------------------------------

# def swap_case(s:str):
#     new=""
#     for i in range(len(s)):
#         if s[i].islower():
#             new=new+s[i].upper()
#         else:
#             new=new+s[i].lower()       
       
#     return new          

# if __name__ == '__main__':
#     s = str(input())
#     result = swap_case(s)
#     print(result)

#------------------Find a string-----------------------------------

# def count_substring(string:str, sub_string:str):
#     a=0
#     result=0
#     reslist=[]
#     for _ in range(0,len(string)):
#         result=string.find(sub_string,result+1)
#         if result==-1:
#             a=a
#             # print('Yok: '+str(a)+'Result: '+str(result))
#         else:
#             if reslist.count(result)==0:
#                 reslist.append(result)
#             # print('Liste: '+str(len(reslist)))
#             a=a+1
#             #print('Buldum: '+str(a)+'Result: '+str(result))
#     return len(reslist)



# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print('Son deger:'+str(count))

#-----------------------------------------------------
# if __name__ == '__main__':
#     s = input()

#     for i in range(len(s)):
#         if s[i].isalnum():
#             a='True'
#             break
#         else:
#             a='False'
#     print(a)        
        
#     for i in range(len(s)):
#         if s[i].isalpha():
#             a='True'
#             break
#         else:
#             a='False'
#     print(a) 
        
#     for i in range(len(s)):
#         if s[i].isdigit():
#             a='True'
#             break
#         else:
#             a='False'
#     print(a) 
        
#     for i in range(len(s)):
#         if s[i].islower():
#             a='True'
#             break
#         else:
#             a='False'
#     print(a) 
        
#     for i in range(len(s)):
#         if s[i].isupper():
#             a='True'
#             break
#         else:
#             a='False'
#     print(a) 
           

#-----------------------------------------------------

# s='.|.'

# # print(s.center(27,"-"))
# # print((s*3).center(27,"-"))
# # print((s*5).center(27,"-"))
# # print(('WELCOME').center(27,"-"))
# # print((s*5).center(27,"-"))
# # print((s*3).center(27,"-"))
# # print((s*1).center(27,"-"))

# line,width = input().split()

# for j in range(1,int(line),2):
#     print((s*j).center(int(width),"-"))

# print(('WELCOME').center(int(width),"-")) 

# for k in range(int(line)-2,0,-2):
#     print((s*k).center(int(width),"-"))   

#-----------------------------------------------------

# def print_formatted(number):
#     # your code goes here

#     width=len(str(bin(number).split('b')[-1]))+1
#     for i in range(1,number+1):
#         print(str(i).rjust(width-1)+str(oct(i).split('o')[-1]).rjust(width)+str(hex(i).split('x')[-1]).upper().rjust(width)+str(bin(i).split('b')[-1]).rjust(width))
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)    

#-----------------------------------------------------
# import string
# s=string.ascii_lowercase
# a=[]
# b=[]
# #print('-'.join(s))
# def print_rangoli(size):
#     # your code goes here
#     c=(size*2-1)+(size*2-2)
#     for i in range(int(size)):
#         a.append(s[size-1:i:-1]+s[i:size])    
#     #print(a)
    
#     for i in range(len(a)):
#         m=""
#         m='-'.join(a[i])
#         #print(m.center(c,"-"))
#         a.remove(a[i])
#         a.insert(i,m)  
#     for i in range(len(a)-1,0,-1):
#         b.append(a[i])
    
    
#     for i in b:    
#         print(str(i).center(c,"-"))
#     for i in a:    
#         print(str(i).center(c,"-"))

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
#-----------------------------------------------------
# import os

# def solve(s):
#     b=[]
#     a=str(s).split(' ')

#     for i in range(len(a)):
#         if a[i]!='':
#             #print(i)
#             #print(a[i][0])
#             if a[i][0].isdigit():
#                 # print('digit')
#                 b.append(a[i]) 
#             else:
#                 # print('NOT digit')
#                 b.append(a[i].title())
#         else:b.append('')        
#     m=""
#     for i in b:
#         m+=(i)+" "
#     print(m)
# if __name__ == '__main__':
#     #fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     #fptr.write(result + '\n')

#     #fptr.close()

#-----------------------------------------------------
#Problem Solving(Basic)

# def fizzBuzz(n):
#     # Write your code here
#     a=[]
#     for i in range(1,int(n)+1):
#         a.append(i)
#         #print(i)
    
#     for i in range(len(a)):
#         if a[i]%3==0 and a[i]%5==0:
#             print("FizzBuzz")
#         elif a[i]%3==0:
#             print("Fizz")
#         elif a[i]%5==0:
#             print("Buzz")
#         else:
#             print(a[i])


# if __name__ == '__main__':
#     n = int(input().strip())

#     fizzBuzz(n)

#-----------------------------------------------------

# T = int(input())
# mylist=[]
# for _ in range(T):
#     mylist.append(input().split())
# #print(mylist)  
# j_listeven=[]
# j_listodd=[]
# for i in range(len(mylist)):
#     i_list=mylist[i][0]
#     sonuc=''
#     j_listeven.clear()
#     j_listodd.clear()
#     for j in range(len(i_list)):
#         if j%2==0:
#             j_listeven.append(i_list[j])
#         else:    
#              j_listodd.append(i_list[j])
#     for k in range(len(j_listeven)):
#         sonuc=sonuc+j_listeven[k]
#     sonuc=sonuc+' '    
#     for l in range(len(j_listodd)):
#         sonuc=sonuc+j_listodd[l]    
        
        
#     print(sonuc)
    # print('Çift: {}'.format(j_listeven))
    # print('Tek: {}'.format(j_listodd))
        
#-----------------------------------------------------


# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())
#     arrReverse=[]
#     arr = list(map(int, input().rstrip().split()))
#     arrReverse=reversed(arr)
#     print(*arrReverse)
#-----------------------------------------------------
#The Minion Game

# def minion_game(string):
#     sesli = ['A','E','I','O','U']
#     c = 0
#     v = 0
#     string=string.upper()
 
#     n = len(string)
#     for i, l in enumerate(string):
#         if l in sesli:
#             v += n-i
#         else:
#             c += n-i
 
#     if v == c:
#         print ("Draw")
#     elif v > c:
#         print ("Kevin {}".format(v))
#     else:
#         print ("Stuart {}".format(c))

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

#-----------------------------------------------------
"""
6
aaa 123
bbb 234
ccc 545
ddd 888
eee 999
fff 111
ddd
fff
aaa
sa
d
f
"""
# n = int(input())
# names=[]  
# phoneBook=[]
# for i in range(n):
#         name,phone = input().split()
#         phoneBook.append([name,phone])        
# for _ in range(n):
#     name= input().split()
#     names.append(name)

# for i,l in enumerate(names):
#     for j in range(n):
#         if names[i][0]==phoneBook[j][0]:
#             a=("{}={}".format(phoneBook[j][0],phoneBook[j][1])) 
#             break
#         else:a=('Not found')
#     print(a)

"""
    solution-2-Fast**************************************
"""

# n = int(input())
# phonebook = dict()
# for i in range(n):
#     line = input()
#     line = line.split()
#     phonebook[line[0]] = phonebook.get(line[0],line[1])
    

# while 1:
#     try:
#         q = input()
#         if q in phonebook:
#             print(str(q) + "=" + str(phonebook[q]))
#         else:
#             print("Not found")
#     except:
#         break
#-----------------------------------------------------
# from math import ceil

# def merge_the_tools(string, k):
#     width=len(string)
#     list=[]
#     s=(width/k)
#     print(ceil(s))
#     for i in range(int(s)):
#         list.append(string[0+k*i:(k*i+1)])


#     print(list)    


# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

#-----------------------------------------------------
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
    
#     n = int(input().strip())
    
#     a=str(bin(n).split('b')[-1])
#     print(a)
#     son=[]
    
#     for i in range(len(a)):
#         s=0
#         for z in range(i,len(a)):
            
#             if a[i]==a[z]:
#                 print('s={} -->  {}=={}'.format(s,a[i],a[z]))
#                 s+=1
#                 son.append(s)
#             else:
#                 break
                 
    
#     print(max(son))                
                

# Python program to check if given
# number is power of 2 or not 
  
# Function to check if x is power of 2
# def isPowerOfTwo (x):
  
#     # First x in the below expression 
#     # is for the case when x is 0 
#     return (x and (not(x & (x - 1))) )
  
# # Driver code
# if(isPowerOfTwo(124)):
#     print('true')
# else:
#     print('false')    


# Python program to check if given
# number is power of 2 or not 
  
# Function to check if x is power of 2
# def isPowerOfTwo(n):
#     if (n == 0):
#         return False
#     while (n != 1):
#             if (n % 2 != 0):
#                 return False
#             n = n // 2
              
#     return True                


# # Driver code
# if(isPowerOfTwo(32)):
#     print('Yes')
# else:
#     print('No')
# if(isPowerOfTwo(64)):
#     print('Yes')
# else:
#     print('No')

#------------------Merge the Tools!----------------

# def merge_the_tools(string, k):
#     for i in range(0, len(string), k):
#         uniq = ''
#         for c in string[i : i+k]:
#             if (c not in uniq):
#                 uniq+=c
#         print(uniq)
    
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)


#------------------input()----------------
# s=input().split(" ")

# x=s[0]


# islem = eval(input().replace("x",x))

# k=int(s[1])
# result=0

# print(k==islem)     


#------------------Python If-Else----------------

# if __name__ == '__main__':
#     n = int(input().strip())

#     even=(n%2==0)

#     if (not even):
#         print("Weird")
#     elif  n<2 and n>=5:
#         print("Not Weird")
#     elif  n>5 and n<=20:
#         print("Weird")
#     else:
#         print("Not Weird")


#--------------------------DefaultDict Tutorial------------

# from collections import defaultdict

# n, m = map(int,input().split())

# a = defaultdict(list)
# for i in range(1, n + 1):
#     a[input()].append(i)

# for i in range(1, m + 1):
#     key = input()
#     if len(a[key]) > 0:
#         print(" ".join(str(c) for c in a[key]))
#     else:
#         print(-1)


#--------------------------Set .add()--------------------------
# n=int(input())
# list1=[]
# for _ in range(n):
#     list1.append(input())

# print(len(set(list1)))

#--------------------------List Comprehensions--------------------------

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
#     list1=[i for i in range(x+1)]
#     list2=[i for i in range(y+1)]
#     list3=[i for i in range(z+1)]

#     list=[]

#     for i in list1:
#         for j in list2:
#             for k in list3:
#                 if i+j+k!=n:
#                     list.append([i,j,k])

#     print(list)

#--------------------------Print Function--------------------------

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):
#         print(i,end="")

#--------------------------Write a function--------------------------

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if (year%4==0 and year%400==0) or  (year%4==0 and year%100!=0):
#         leap=True
#     return leap

# year = int(input())
# print(is_leap(year))