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

#-----------------------------------------------------

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

def minion_game(string:str):
    # your code goes here
    vowel =['A','E','I','O','U']
    v=[]
    c=[]
    ss=[]
    son=[]
    soon=[]
    spoints=0
    kpoints=0
    string=string.upper()
    for i in string:
        if i in vowel:
            v.append(i)
        else:
            c.append(i)    
    v=list(set(v)) 
    c=list(set(c)) 
    for i in string:#string to list
        ss.append(i)
    for h in range(len(string)+1):
        for g in range(1,len(string)+1):
            if len(ss[h:g])==0 :
                pass
            else:son.append(ss[h:g])        
    for t in range(len(son)):
        hece=""
        for y in range(len(son[t])):
            hece=hece+son[t][y] 
        soon.append(hece)
    # print(len(son))
    print(soon)
    for vi in v:#sesli başlangıç/başlangıçlar
        kpoints+=soon.count(vi)
    for ci in c:#sessiz başlangıç/başlangıçlar
        #spoints+=soon.count(ci)    
            aranacak=0
            for z in range(len(soon)):
                aranacak=soon.count(ci)
            print('aranacak:'+str(aranacak))
            # spoints+=soon.count(aranacak)
            # print(soon.count(aranacak))


    print('Stuart Points: {}'.format(str(spoints)))
    print('Kevin Points: {}'.format(str(kpoints)))

if __name__ == '__main__':
    s = input()
    minion_game(s)