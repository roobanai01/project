#Single Inheritance program
'''class dad():
    def phone (self):
        print("Dad's phone")
class mom():
    def food(self):
        print("Mom's Kesari")
class son(dad,mom):
    def laptop(self):
        print("Son's laptop")
rooban=son()
rooban.laptop()
rooban.phone()
rooban.food()'''

#Multilevel Inheritance program
'''class grandpa():
    def phone (self):
        print("Grandpa's Phone")
class dad(grandpa):
    def money (self):
        print("Dad's Money")
class son(dad):
    def laptop (self):
        print("Son's Laptop")
rooban=son()
rooban.laptop()
rooban.money()
rooban.phone()
kumar=dad()
kumar.money()
kumar.phone()'''

#Hierachy and Hybrid inheritance

class dad():
    def property (self):
        print("Dad's property")
class land ():
    def area(self):
        print("Main area land")
class son1(dad):
    pass
class son2(dad,land):
    pass
class son3(dad):
    pass
s1=son1()
s1.property()
s2=son2()
s2.property()
s2.area()
s3=son3()
s3.property()


