# inheritance --code reusabilty

# 5 types
# single
'''
one to one process
A
|
B

'''


# multiple
# one to many process
'''
A
|
B
|
C
|
.
'''


# multilevel
# many to one process
'''
 A  B
  \/
  C

'''

# Hirarchical
# one to many process
'''
     A
    /|\
   B C D
'''


# Hybird
# more than 2inheirtance
'''
A
|
B  C
 \/
 D
'''



# class A:
#     a=4
#     b=3
#     def dis(self):
#         print("res",self.a+self.b)

# class B(A):
#     def data(self):
#         print("REs",self.a-self.b)

# o=B()
# o.dis()
# o.data()

'''
class A:
    a=5

class B:
    b=3

class C(A,B):
    c=0
    def data(self):
        self.c=self.a*self.b
        print("area of rectange is:",self.c)

o=C()
o.data()


'''

# aggregation(is a relationship)-->single inheritance
# composition(has a relationship)


class Engine:
    def __init__(self,x):
       self.engine=x

    def start(self):
        print("Engine started from",self.engine)


class Car:
    def __init__(self,a,b,c):
        self.name=a
        self.yr=b
        self.engine=Engine(c)

    def move(self):
        self.engine.start()
        print(f"car name is{self.name} car yr is {self.yr} car was moving..")


o=Car("baleno","2021","highend")
o.move()
