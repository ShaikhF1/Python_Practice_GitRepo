###Question-38- Write a program to print the first half values in one line
##and the last half values in one line.
tpl = (1,2,3,4,5,6,7,8,9,10)

# for i in range(0,5):
#     print(tpl[i], end ='')
# print()
# for i in range(5,10):
#     print(tpl[i], end = '')    

# ###Solution-2
# lst1, lst2 = [],[]

# for i in range(0,5):
#     lst1.append(tpl[i])

# for i in range(5,10):
#     lst2.append(tpl[i])

# print(lst1)
# print(lst2)    
################################################################################
###Question-39-Write a program to generate and print another tuple
##whose values are even numbers in the given tuple.
# tpl1 = tuple(filter(lambda x: x%2==0, tpl))
# print(tpl1)
################################################################################
##Question-40- Write a program which accepts a string as i\p to print "Yes".
##If the string is "yes" or "YES" or "Yes", otherwise print "No".
# s = input()
# if s.lower() == 'yes':
#     print('Yes')
# else:
#     print('No')    
################################################################################
###Question-41- Write a program which can map() to make a
## list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
# li = [1,2,3,4,5,6,7,8,9,10]
# sqNumbers = map(lambda x: x**2, li)
# print(list(sqNumbers))
################################################################################
##Question-43-Write a program which can filter() to make a list
##whose elements are even number between 1 and 20(both included).
# def even(x):
#     return x%2 == 0

# evenNumbers = filter(even, range(1,21))
# print(list(evenNumbers))
################################################################################
##Question-44- Write a program whcih can map() to make a list whoe elements
###are square of numbers between 1 and 20(both included).
# def sqr(x):
#     return x*x
# sqNumbers = list(map(sqr, range(1,21)))
# print(sqNumbers)
################################################################################
##Question-45- Define a class American which has a static method called printNationality.
# class American():
#     @staticmethod
#     def printNationality():
#         print("I am American")

# american =  American()
# american.printNationality()
# American.printNationality()
################################################################################
##Question-46- Define a class named American and its subclass NewYorker.
# class American():
#     pass
# class NewYorker(American):
#     pass

# american = American()
# newyorker = NewYorker()
# print(american)
# print(newyorker)
################################################################################
###Quesion-47-Define a class names Circle which can be constructed by a radius. The Circle calss has a method
##which can compute the area.
# class Circle():
#     def __init__(self,r):
#         self.radius =  r

#     def area(self):
#         return 3.1416 * (self.radius**2)
# circle = Circle(5)
# print(circle.area())
################################################################################
###Question-48-Define a class named Rectangle which can be constructed by a length 
##and width. The Rectangle class has a method which can compuet the area.
# class Rectangle():
#     def __init__(self,l,w):
#         self.length = l
#         self.width = w

#     def area(self):
#         return self.length*self.width    
# rect = Rectangle(2,4)
# print(rect.area)
################################################################################
###Question-49-Define a class named Shape and its subclass Square.
##The square class has an init function which takes a length as argument.
##Both classes have a area function which can print the area of the shape where
##shape's area is 0 by default.
# class Shape():
#     def __init__(self):
#         pass
#     def area(self):
#         return 0 

# class Square(Shape):
#     def __init__(self,length=0):
#         Shape.__init__(self)
#         self.length = length
    
#     def area(self):
#         return self.length*self.length

# Asqr = Square(5)
# print(Asqr.area())
# print(Square().area())
################################################################################
# ##Question-51- Write a function to compute 5/0 and use exception.
# def divide():
#     return 5/0
# try:
#     divide()
# except ZeroDivisionError as ze:
#     print("Why on earth you are dividinf a number by ZERO..!")
# except:
#     print("Any otehr exception.")        
################################################################################
###Question-52- Define a custom exception, we need to define a class inherited from exception.
# class CustomException(Exception):
#     def __init__(self,message):
#         self.message = message
# num = int(input())
# try:
#     if num < 10:
#         raise CustomException("Input is less than 10")
#     elif num > 10:
#         raise CustomException("Input is greater than 10")
# except CustomException as ce:
#     print("The error raised: " + ce.message)
################################################################################
##Question-53-Write a program to print the username of a given address. Bith usernames and compnay
##names are composed of letters only.
# email = "firojshaikh56@gmail.com"
# email - email.split('@')
# print(email[0])
##########################
# import re
# email = 'firojshaikh56@gmail.com'
# pattern = '(\w+)@\w+.com'
# ans = re.findall(pattern, email)
# print(ans)
################################################################################
###Question-54- Write a program to print the company b=name of a given email address.
##Both user names and company names are composed of letters only.
# import re
# email = 'firojshaikh56@gmail.com'
# pattern = '(\w+)@\w+.com'
# pattern = "\w+@(\w+).com"
# pattern = '(\w+)@(\w+).com'
# ans = re.findall(pattern, email)
# print(ans)
################################################################################
##Question-57- Write a program to read an ASCII string and to convert 
## it to a unicode string encoded by utf-8.
# s = input()
# u = s.encode('utf-8')
# print(u)
################################################################################
###Question-58- Write a special comment to indicate a python source code
##file is in unicode format.
'''Python
# -*- conding: utf-8 -*-
'''
################################################################################
###***Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).***
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i/(i+1)

print(round(sum, 2))








