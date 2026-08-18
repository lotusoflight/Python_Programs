# Class
# class is a collections of datas(variable) and methods(behaviour)
# blueprint of object


# Object
# Instance of class or blueprint of class

# Self
# instance of object


# class Dog:
#     # global variables
#     name="shadow"
#     age=2
#     clr="golden"

#     def sound(self):
#         # local variable
#         x=3
#         print("Barking...")
#     def play(self):
#         print("playing")

# o=Dog()
# print(o.name)
# print(o.age)
# print(o.clr)
# o.name="Tiger"
# o.age=23
# o.clr="black"
# print(o.name)
# print(o.age)
# print(o.clr)
# o.sound()
# o.play()



# Constructor
# class name and method name should be same

# class A:

#     def __init__(self,x):
#         self.name=x
#         print("am constructor",self.name)

#     def show(self):
#         print("Am normal method")

#     def __str__(self):
#         # return "finish"
#         return self.name
# o=A("aruna")
# o.show()
# print(o)