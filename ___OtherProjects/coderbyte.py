"""First Factorial"""
# def FirstFactorial(num):

#   # code goes here
#   result=1
#   for i in range(2,num+1):
#     result*=i
#   return result

# # keep this function call here 
# print(FirstFactorial(input()))   


"""First Reverse"""

# def FirstReverse(strParam):

# #   # code goes here
# #   list=[]
# # # """Solution-1"""
# #   list[:0]=strParam
# # # """Solution-2"""
# # #   for i in strParam:
# # #       list.append(i)
# #   list.reverse() 
# #   strParam="" 
# # """Solution-1"""
# # #   for z in list:
# # #       strParam+=z
# # """Solution-2"""
# #   strParam=strParam.join(list)  
# #"""Short Code"""

#   return sorted(strParam[::-1])

# # keep this function call here 
# print(FirstReverse(input()))

"""Bracket Matcher"""

# def BracketMatcher(str):

#   count = 0
#   for c in str:
#     if c == '(':
#       count += 1
#     elif c == ')':
#       count -= 1
#     if count < 0: return 0

#   return 1 if count == 0 else 0

# # keep this function call here 
# print(BracketMatcher(input()))

"""Min Window Substring"""
# from collections import Counter


# def TreeConstructor(strArr):

#   links = [eval(s) for s in strArr]
#   children, parents = zip(*links)

#   counter_c = Counter(children)
#   counter_p = Counter(parents)
  
#   for c in counter_p.values():
#     if c > 2:
#       return "false"

#   return "true"

# # keep this function call here 
# print(TreeConstructor(input()))
    
  
"""Find Intersection""" 

# def FindIntersection(strArr):
  
#     setOne = set(strArr[0].split(", "))
#     setTwo = set(strArr[1].split(", "))

#     result = sorted(list(setOne.intersection(setTwo)), key=lambda str: int(str))
    
#     return ','.join(result) if len(result) > 0 else False

# print(FindIntersection(["17, 18, 20s", "1, 4, 9, 10, 20"]))
  
"""Find LongestWord""" 

# def LongestWord(sen):
#     nw = ""
#     for i in sen:
#       if i.isalnum() :
#         nw += i
#       else :
#         print(i)
#         nw += " "
#     print(str(len(max(nw.split(),key=len))))    
#     return max(nw.split(),key=len)
# print(LongestWord(input()))

"""Find Tamkare mi?""" 

# sayi=int(input())

# sqrt_sayi=sayi**0.5
# pow_sayi=int(sqrt_sayi)*int(sqrt_sayi)

# if pow_sayi==sayi:
#     print('True')
# else:
#     print('False')    

"""Codeland Kullanıcı Adı Doğrulaması"""

def CodelandUsernameValidation(str):
  leng=len(str)
  if 4<= leng <= 25:
    import re 
    l=re.findall('\W',str)
    if len(l)==0:
      i=re.findall("_$",str)
      if len(i)==0:
        return "true"
      else:
        return "false"
    else:
      return "false"
  else:
    return "false"
    
# keep this function call here 
print(CodelandUsernameValidation(input()))