# Encapsulation(security)
# 

# access modifier/specifier
'''
public ---> nope underscore
protected --->  _(single underscore)
private ---->  __(double underscore)----->Encapsulation
'''


# class A:
#     a="public"
#     _b="protected"
#     __c="private"

#     def dis(self):
#         print("am public method")
#     def _data(self):
#         print("am protected method")
#         self.__show()
#     def __show(self):
#         print("am private method")

# o=A()
# print(o.a)
# print(o._b)
# # print(o.__c)

# o.dis()
# o._data()
# # o.__show()




# priavte access from outside the class using the inbuilt
# methods of setter(set-assign) & getter(get- receive)


class A:
    name="anu"
    __age=21

    def dis(self):
        print("name is:",self.name)
        print("age is:",self.__age)
    def getdata(self):
        return self.__age
    def setdata(self,x):
        self.__age=x

o=A()
o.dis()
o.name="priya"
o.setdata(10)
# o.__age=25
o.dis()
# print(o.name)
# print(o.__age)
o.setdata(10)
print(o.getdata())
