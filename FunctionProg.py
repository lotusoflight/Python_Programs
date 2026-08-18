# print("hii")
# print("hii")
# print("hello")
# print("hii")


# input()
# int()
# str()
# list()
# set()
# tuple()
# dict()
# type()



# def dis():
#     print("hello")


# print("hi")
# print("hi")
# print("hi")
# dis()
# print("hi")



'''
userdefined function

returntype function
 1. with return type and with argument
 2. with return type and without argument

 not return type function
  1. without return type and with argument
  2. without return type and without argument


'''


# def show():
#     print("hello")

# show()

# def show(x,y):
#     print("res",x+y)

# show(2,10)



# def demo():
#     return "anu","priya"

# # print(demo())
# a,b=demo()
# print(a,b)



# def data(x,y):
#     return x+y

# print("res:",data(10,20))


# global variable
# a=10
# def data(x):
#     # local variable
#     b=29
#     print(x)
#     print(a)
#     print(b)

# data(30)
# print("Oustide calling variable")
# print(a)
# print(b)




# Pass by value (does not original value)

# a=30
# def data(x):
#     x+=10
#     print(x)

# print(a)
# data(a)
# print(a)

#pass by referance (change/modify the original value) 

# a=[10,20]
# def data(x):
#     x.append(30)
#     print(x)

# print(a)
# data(a)
# print(a)




# lambda function

# def data():
#     definition

# x=lambda x,y,z:x+y*z
# print(x(2,3,4))


# partial function

# from functools import partial
# def data(a,b,c,d,e):
#     print(a+b+c+d+e)

# # data(5,8,9)

# x=partial(data,2,3)
# x(3,4,5)



# Recursion function (function calls itself)
# def data(x):
#     if x<1:
#         return 1
#     else:
#         return x*data(x-1)

# print("the factorial value is:",data(5))




