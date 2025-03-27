# class Account:
#     def __init__(self, balance,account_no):
#         self.balance = balance
#         self.account = account_no
    
#     def devit(self, amount):
#         self.balance -= amount
#         print(amount, 'was devited.','Total amount is:', self.balance)
    
#     def credit(self, amount):
#         self.balance += amount
#         print(amount, 'was credited.','Total amount is:', self.balance)


# ac1 = Account(int(input('enter amount:')) ,int(input('enter account_no:')))

# if (ac1.account != 12345):
#     print('wrong account no..')

# else:
#     ac1.devit(1000)
#     ac1.credit(500)
#     ac1.credit(50000)
#     ac1.devit(10000)
    
# class car:
#     @staticmethod
#     def start():
#         print('car started..')

#     @staticmethod
#     def stop():
#         print('car stopped..')

# class toyotacar:
#     def __init__ (self,name):
#         self.name =name
# class wasiy(car,toyotacar):
#     def __init__ (self , color):
#         self. color = color


# car1 = wasiy('black')
# print(car1.color)
# print(car1.start())
# print(car1.stop())

# class person:
#     name = 'annonymous'
#     @classmethod
#     def changename (cls, name):
#         cls.name = name

# p1 = person()
# p1.changename('wasiy')
# print(p1.name)

# class student:
#     def __init__(self,phy,chem,math):
#         self.phy= phy
#         self.chem = chem 
#         self.math = math
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) /3) + '%'
        
# s1 = student(98,99,96)
# print(s1. percentage)
# s1.phy = 86
# print(s1. percentage)
    

# class complex:
#     def __init__(self,real, img):
#         self.real = real
#         self. img  = img 

#     def complexnum(self):
#         print (self.real,'i +', self.img , 'j')

#     def __add__(self,com2):
#         newreal = self. real + com2.real
#         newimg = self. img + com2.img 
#         return complex(newreal, newimg) 

# com1 = complex(1,4)
# com2 = complex(3,6)

# com3 = com1 + com2
# com3 . complexnum()


# class Circle:
#     def __init__(self, radius):
#         self .radius = radius

#     def area(self):
#         area =(22/7) * self.radius ** 2
#         return area
#     def perimeter(self):
#         perimeter = 2 * (22/7) * self . radius
#         return perimeter
#     @property
#     def valuearea(self):
#         area =(22/7) * self.radius ** 2
#         return area 
#     @property
#     def valueperimeter(self):
#         perimeter = 2 * (22/7) * self . radius
#         return  perimeter

# c1 = Circle (46)
# print(c1.valueperimeter)
# print (c1. valuearea)



######  It started when I watch cahi aur code OOPs video . but I can't contunue.
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model


#     def get_brand(self):
#         return self.brand +'!'
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# my_tesla = ElectricCar("Tesla", "Model S", '100KWh')
# print(my_tesla.model)
# print(my_tesla.full_name())


# my_car = Car('Toyota','Corrola')
# print(my_car.full_name())
