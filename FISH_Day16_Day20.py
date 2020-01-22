###Question-60 ->***Write a program to compute:***
##f(n)=f(n-1)+100 when n>0 and f(0)=1
# def f(n):
#     if n ==0:
#         return 0
#     return f(n-1) + 100

# n = int(input())
# print(f(n))
############################################################
##Question-61- Fibonacci Series.
# def f(n):
#     if n < 2:
#         return n
#     return f(n-1) + f(n-2)
# n = int(input())
# print(f(n))    
############################################################
####Question-62- Fibonacci Series
# def f(n):
#     if n < 2:
#         fibo[n] = n
#         return fibo[n]
#     fibo[n] = f(n-1) + f(n-2)
#     return fibo[n]    

# n = int(input())
# fibo = [0]*(n+1)
# f(n)
# fibo = [str(i) for i in fibo]
# ans = ",".join(fibo)
# print(ans)
############################################################
##Question-64- Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# def generate(n):
#     for i in range(n+1):
#         if i % 35 == 0:
#             yield i

# n = int(input())
# resp = [str(i) for i in generate(n)]
# print(",".join(resp))
############################################################
###Question-65-Please write assert statements to verify that every numbers in the list [2,4,6,8] is even.
# data = [2,4,6,8,9]
# for i in data:
#     assert i%2 ==0, "{} is not an even number".format(i)
############################################################
##Question-66- Please write aprogram which accepts basic maths expression
##console and print the evaluation result.
# expression = input()
# ans = eval(expression)
# print(ans)
############################################################
###Question-68- Please generate a random float where the value is between 10 and 100 using Python module.
# import random
# rand_num = random.uniform(10,100)
# print(rand_num)
############################################################
###Question-69- Please generate a random float where the value is in between 5 and 95.
# import random
# rand_num = random.uniform(5, 95)
# print(rand_num)
############################################################
###Day-18- Question-70
###Please write a program to output a random even number between 0 and 10 inclusive 
##using random module and list comprehension.
# import random
# resp = [i for i in range(2,11,2)]
# print(random.choice(resp))
############################################################
# ###Question-71- Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.***
# import random
# resp = [i for i in range(10,151) if i  % 35 ==0]
# print(random.choice(resp))
############################################################
###Question-72- Please write a program to generate a list with
## 5 random numbers between 100 and 200 inclusives.
# import random
# resp = random.sample(range(100,201),5)
# print(resp)
############################################################
###Question-73- Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusives.
# import random
# resp = random.sample(range(100,201,2),5)
# print(resp)
############################################################
###Question-74-Please write a program to randomly generate a list with
##5 numbers, which are div by 5 and 7, between 1 and 1000 inclusive.
# import random
# lst = [i for i in range(1,1001) if i%35 ==0]
# resp = random.sample(lst,5)
# print(resp)
############################################################
####Day-19- Question-75
##Please write a program to randomly print a integer number between 7 and 15 inclusive.
# import random
# print (random.randrange(7,16))
############################################################
###Question-76-Write a program to compress and decompress the string "hello world!hello world!hello world!"
# import zlib
# s = "hello world!hello world!hello world!hello world!"
# t = zlib.compress(s)
# print (t)
# # print(zlib.decompress(t))
############################################################
##Question-77- Write a program to print the running time of excecution of '1+1' for 100 times.
# import datetime

# before = datetime.datetime.now()
# for i in range(100):
#     x = 1 + 1
# after = datetime.datetime.now()
# execution_time = after - before
# print(execution_time.microseconds)
############################################################
###Question-78- Please write a program to shuffle and print the list [3,6,7,8].
# import random
# lst = [3,6,7,8]
# random.shuffle(lst)
# print(lst)
############################################################
###Question-79- Please write a program to generate all senteneces where subjects is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hokey","Football"]
# subjects = ["I", "You"]
# verbs = ["Play", "Love"]
# objects = ["Hockey", "Football"]

# for sub in subjects:
#     for verb in verbs:
#         for obj in objects:
#             print("{} {} {}".format(sub,verb,obj))
############################################################
###Day-20-Question-80
##Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
# def isEven(n):
#     return n%2 !=0
# li = [5,6,77,45,22,12,24]
# lst = list(filter(isEven, li))
# print(lst)
############################################################
###Quesion-81- By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].***
# li = [12,24,35,70,88,120,155]
# li  = [x for x in li if x % 35 !=0]
# print(li)
############################################################
##Question-81- By using list comprehension, please write a program to print the list
##after removing th 0th, 2nd, 4th and 6th numbers in [12,24,35,70,88,120,155].
# li = [12,24,35,70,88,120,155]
# li = [li[i] for i in range(len(li)) if i%2 !=0]
# print(li)
############################################################
###Question-82 -By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
# li = [12,24,35,70,88,120,155]
# li = [li[i] for i in range(len(li)) if i%2 !=0]
# print(li)
############################################################
###Question-83- By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i<3 or 4< i]
print(li)



