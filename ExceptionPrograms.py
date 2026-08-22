# try:
#     state 
# except Exception as o:
#     state 


# print("hii")
# print("hii")
# print("hii")
# try:
#     print(a)
# except Exception as o:
#     print("error:",o)
# print("hii")
# print("hii")
# print("hii")




# types of exceptions

# arithmetic error

# try:
#     a=10
#     b=0
#     print("result is:",a//b)
# except ArithmeticError as o:
#     print(o)


# index error

# try:
#     a=[1,2,3,4]
#     print(a[11])
# except IndexError as m:
#     print(m)

# syntax error
# fer i in range(10):
#     print(i)

# nullpointer error

# try:
#     a=None
#     print(len(a))
# except Exception as m:
#     print(m)

# import error

# from abc import ABC
# from abc import XYZ
# print(XYZ)

# key error

# try:
#     a={'name':'anu','age':24}
#     print(a['city'])
# except KeyError as m:
#     print(m)

# name error

# try:
#     a=[1,2,3,4]
#     print(b)
# except NameError as m:
#     print(m)

# value error

# try:
#     a=int(input("Enter value:"))
#     print(a)
# except ValueError as m:
#     print(m)


# Type error
# try:
#     a=5
#     b='g'
#     print(a//b)
# except TypeError as o:
#     print(o)


# assert error
# a=5
# b=3
# assert a<b,"Error from custom"




# multiple exception

# try:
#     a=[2,3,4,5]
#     print(a[31]//2)
# except ArithmeticError as o:
#     print("error 1:",o)
# except IndexError as m:
#     print("error2:",m)



# Nested Exception

# try:
#     a=[1,2,3]
#     print(a[2])
#     try:
#         print(a[2]/0)
#     except Exception as o:
#         print("Inside error")
# except Exception as m:
#     print("Outside error")


# else 

# try:
#     a=5
#     b=a/2
# except Exception as o:
#     print(o)
# else:
#     print(b)



# finally(cleanup action)

# try:
#     a=5
#     b=a/0
# except Exception as o:
#     print(o)
# else:
#     print(b)
# finally:
#     print("always excuted..")


# Custom exception/user defined exception


# class Custom(Exception):
#     def __init__(self, x):
#         super().__init__(x)


# def check(m):
#     try:
#         if m>21:
#             print("eligible")
#         else:
#             raise Custom("not eligible")
#     except Exception as m:
#         print(m)
    
# check(25)
# check(13)