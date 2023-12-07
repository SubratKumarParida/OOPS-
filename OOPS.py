#!/usr/bin/env python
# coding: utf-8

# In[26]:


def used_car_price(car_year, car_brand, kmeters):
    if car_year == 2020:
        if 10000 < kmeters <= 15000:# If I is less than meters AND limeters is Less than or equal to 15K
            if car_brand =="Honda Amaze":
                print('Rs 690,000 - Rs 750,000')
            elif car_brand == "Hyundai Creta":
                print('rs 945,000 - rs 10,80,000')
            else: 
                print ("No Stuck right now, please visit after few days")
                     
        elif 15001 < kmeters <= 25000: 
            if car_brand == 'Honda Amaze': 
                print('Rs 500,000 - Rs 600,000')
            elif car_brand=="Hyundai Creta": 
                print('rs 845,000 - rs 980,000')
            else:
                print ("No Stock right now, please visit after few days")
        else:
            print ("No Stocks")

    elif car_year == 2021:
        if 10000< kmeters <= 15000: #TF 10K is less than kacters AND kmeters is less than or equal to 15K
            if car_brand == 'Honda Amaze' :
                   print('Rs 790,000 Rs 858,000')
            elif car_brand=='Hyundai Creta': 
                    print('rs 10,45,000 - rs 11,80,000')


            else:
                print ("No Stock right now, please visit after few days")
        else:
            print ("No Stock right now, please visit after few days")
    
    else:
        print ("Sorry, We dont keep car's older than 2020")
 
   


# In[20]:


used_car_price(2021, "Hyundai Creta",11000)
used_car_price(2021, "BMW",11000)
used_car_price(2020, "BMW",1000)


# # OOPS(object oriented programmings)
# 

# In[8]:


class Phone:
    def call(self):
        print("call utha re")
    def game(self):
        print("game khelo")


# In[9]:


p1 = Phone()


# In[10]:


p1.call()
p1.game()


# In[6]:


class Phone:
    def set_color(self,color):#initialize
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    
    def call(self):
        print("call utha re")
    def game(self):
        print("game khelo")
            


# In[7]:


p2 = Phone()
p2.set_color("white")
p2.set_cost(25000)


# In[9]:


p2.show_color()
#p2.show_cost()


# # CONSTRUCTOR(INITIALIZES OBJECTS nothing but [__init__] )

# In[11]:


class Emp:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def emp_details(self):
        print("name of the emp is:",self.name)
        print("age of the emp is:",self.age )
        print("salary of the emp is:",self.salary)
        print("gender of the emp is:",self.gender)


# In[13]:


e1 = Emp("Subrat",21,1000000,"Male")


# In[14]:


e1.emp_details()


# # INHERITANCE(one class derive the properties of  other class)

# In[15]:


class vehicle:#parent_class
    def __init__(self,milage,cost):
        self.milage = milage
        self.cost = cost
    def show_details(self):
        print("Vehicle")
        print("the milage of the car is:",self.milage)
        print("the cost of the car is:",self.cost)


# In[17]:


v1 = vehicle(15,2000000)
v1.show_details()


# In[25]:


class car(vehicle):#inherited class or child class
    def show_car(self):
        print("The car name is :TATA HARRIER")


# In[26]:


c1 = car(15,2000000)#child class can call parents class method its the examole
c1.show_details()
c1.show_car()


# # OVERRIDDING(by init method)

# In[29]:


class car(vehicle):
    def __init__(self,milage,cost,tyre,hp):
        super().__init__(milage,cost)#super keyword used for calling the parent class methods
        self.tyre = tyre
        self.hp = hp
    def show_car_details(self):
        print("CRETA")
        print("number of tyres:",self.tyre)
        print("the horse power is:",self.hp)
    


# In[30]:


c3 = car(20,1200000,4,3000)
c3.show_details()#call parent class method 


# In[31]:


c3.show_car_details()


# # MULTIPLE INHERITANCE

# In[32]:


class parent1:
    def assign_str_one(self,str1):
        self.str1 = str1
    def show_string_one(self):
        return self.str1
    


# In[33]:


class parent2:
    def assign_str_two(self,str2):
        self.str2 = str2
    def show_string_two(self):
        return self.str2
    


# In[34]:


class child(parent1,parent2):
    def assign_str_three(self,str3):
        self.str3 = str3
    def show_string_three(self):
        return self.str3
    


# In[35]:


mera_beta = child()


# In[40]:


mera_beta.assign_str_one("parent1 ka aulad hun")
mera_beta.assign_str_two("parent2 ka aulad hun")
mera_beta.assign_str_three("iska dodo baap")


# In[37]:


mera_beta.show_string_one()


# In[38]:


mera_beta.show_string_two()


# In[41]:


mera_beta.show_string_three()


# # diamond interface problem / deadly diamond

# In[49]:


class A:
    
    def explore(self):
        print("A ka explorer hun")
class B(A):
    #pass
    def explore(self):
        print("B ka explorer hun")
class C(A):
    #pass
    def explore(self):
        print("C ka explorer hun")
class D(B,C):         #multiple inheritance
    pass

d = D()
d.explore()


# # polymorphism

# In[5]:


#CLASS LEVEL POLYMERPHISIM
class A:
    def p(self):
        return "function p in A"
class B:
    def p(self,fn=""):
        print("function p in B",fn)
    
a = A()
b = B()
b.p("sai")

#for i in (a,b):
   # print(i.p())#function that runs depends on the object
#print("*"*30)

#x = a
#print(x.p())

x = b
print(x.p())


# In[6]:


#when ever we writting method name with same sign in parent and child class called method overriding
class A:
    def Disp(self):
        print("its parent class method")
class B(A):
    def Disp(self):
        super().Disp()
        print("its child class method")
b=B()
b.Disp()


# # polymerphisim weds inheritance

# In[59]:


import math

class Shape:
    def __init__(self, color="black", filled=False):
        self.__color = color
        self.__filled = filled
    
    def get_color(self):
        return self.__color
    
    
    def set_color(self, color):
        self.__color = color
    
    def get_filled(self):
        return self.__filled
    
    def set_filled(self, filled):
        self.__filled = filled

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
    
    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = length
    
    def get_breadth(self):
        return self.__breadth
    
    def set_breadth(self, breadth):
        self.__breadth = breadth
    
    def get_area(self):
        return "the area of rectangle is:", self.__length * self.__breadth
    
    def get_perimeter(self):
        return "the perimeter of rectangle is:", 2 * (self.__length + self.__breadth)

class Circle(Shape): 
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
        
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
   
    def get_area(self):
        return "the area of circle is:", math.pi * self.__radius ** 2
    
    def get_perimeter(self):
        return "the perimeter of circle is:", 2 * math.pi * self.__radius

s = Shape()
r = Rectangle(10, 20)
c = Circle(5)

for i in (s, r, c):
    print(i.get_color())

for i in (r, c):
    print(i.get_area())


# In[2]:


class Account:
    def __init__(self,name = input("Enter your name:"),
                 last_name = input("Enter your last name:"),
                 city = input("Enter your city name:"),
                 user_id = int(input("Enter your user_id:")),
                 password = input("Enter your password:"),
                 phone =  int(input("Enter your phone no:"))):
        
        self.name = name
        self.last_name = last_name
        self.city = city
        self.user_id = user_id
        self.password = password
        self.phone = phone
        
    def login(self):
        attempts = 1
        
        while True:
            signin = int(input("Enter your user_id:"))
            password = input("Enter your password:")
            
            if signin == self.user_id and password == self.password:
                print('Succesfully logged In ')
                break
            else:
                if attempts==3:
                    print("maximum attempts reached, call the customer service to reset the password")
                    break
                else:
                    print("user ID and Password is Invalid")
                    attempts+=1
                    continue
              


# In[3]:


l = Account()
l.login()


# In[4]:


class User_Account(Account):
    def __init__(self,acc_number,balance,*args):
        super(User_Account,self).__init__(*args)
        self.acc_number = acc_number
        self.balance = balance
        
    def user_details(self):
        account = int(input("Enter your account_id:"))
        if account == self.acc_number:
            print('Name:',self.name)
            print('Acc num:',self.acc_number)
            print('Your Balance :',self.balance)
            print('Your phone num:',self.phone)
            
            #break
        else:
            print('Account number is not valid')
            #continue
            
    def deposite(self):
        print('Your prv balance is :',self.balance)
        add_cash = int(input('deposite cash='))
        self.balance += add_cash
        print('\n SBI BANK:RS',add_cash,'deposite to your acc',self.acc_number,'and your current balance is',self.balance)
        
    def transfer(self):
        print('Your prv balance is :',self.balance)
        withdraw = int(input('hoe much you tranfer:'))
        if withdraw <= self.balance:
            self.balance -= withdraw
            print('\n SBI BANK:RS',withdraw,'withdraw from your acc',self.acc_number,'and your current balance is',self.balance)
        else:
            print('bhosadike jaake apna shakal mirror pe dekh')
            


# In[11]:


bank_details = User_Account(123456,0)


# In[7]:


bank_details.login()


# In[8]:


bank_details.user_details()


# In[9]:


bank_details.deposite()


# # ENCAPSULATION

# In[32]:


class Products:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class ShoppingCart:
    def __init__(self):
        self.my_items=[]
    
    def add_items(self,item):
        self.my_items.append(item)
        print(f"Added '{item.name}'to the cart")
    
    def display_Cart(self):
        print("all items in shopping cart")
        for item in self.my_items:
            print(f"{item.name}:RS :{item.price}")
    
    def get_total_price(self):
        total_price = sum(item.price for item in self.my_items)
        return total_price
        


# In[28]:


item_tv = Products("TV",50000)
item_sofa = Products("Sofa",15000)


# In[29]:


cart = ShoppingCart()
cart.add_items(item_tv)
cart.add_items(item_sofa)


# In[30]:


total_price = cart.get_total_price()
print('Total Price is:RS',total_price)


# In[31]:


cart.display_Cart()


# # subrat

# In[13]:


a=5
a=3
print("the number",a)


# In[1]:


print(5+5)


# In[2]:


print("5"+"5")


# In[ ]:




