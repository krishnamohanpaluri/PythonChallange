#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = -6
b = -6
print(a is b)


# In[3]:


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))

class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def get_deal_price(self):
        return self.deal_price

    def display_product_details(self):
        print("{} {}".format(self.name, self.price))

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months
      
    def get_warranty(self):
        return self.warranty_in_months

    def display_product_details(self):
        super().display_product_details()      
        print("Warranty {} months".format(self.warranty_in_months))

tv = ElectronicItem("TV", 45000, 40000, 3.5, 12)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(tv, 1)
order.display_order_details()


# In[4]:


class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

p = B(1, 2)
q = C(1, 3, 2)
is_same = p.y == q.y
print(is_same)


# In[5]:


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))

class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def get_deal_price(self):
        return self.deal_price

    def display_product_details(self):
        print("{} {}".format(self.name, self.price))

class ElectronicItem(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months
      
    def get_warranty(self):
        return self.warranty_in_months

    def display_product_details(self):
        super().display_product_details()      
        print("Warranty {} months".format(self.warranty_in_months))

tv = ElectronicItem("TV", 45000, 40000, 3.5)
tv.set_warranty(12)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(tv, 1)
order.display_order_details()


# In[6]:


class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

class C(A):
    def __init__(self, x, z):
        super().__init__(x)
        self.z = z

p = B(1, 2)
q = C(1, 3)
is_same = p.x == q.x
print(is_same)


# In[7]:


class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

p = B(x=1, y=2)
q = C(x=1, z=3, y=2)
is_same = p.y == q.y
print(is_same)


# In[8]:


class A:
    def __init__(self, x):
        self.x = x

    def update_value(self, y):
        self.x = y

class B(A):
    def __init__(self, x):
        super().__init__(x)

p = B(20)
p.update_value(25)
print(p.x)


# In[9]:


class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x):
        super().__init__(x)
        
class C(B):
    def __init__(self, x):
        super().__init__(x)

p = C(20)
q = B(2)


# In[10]:


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print("Total Bill: {}".format(total_bill))


class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def get_deal_price(self):
        return self.deal_price

class ElectronicItem(Product):
    pass

class GroceryItem(Product):
    pass

milk = GroceryItem("Milk", 40, 25, 3.5)
tv = ElectronicItem("TV", 45000, 40000, 3.5)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(milk, 2)
order.add_item(tv, 1)
order.display_total_bill()


# In[11]:


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print("Total Bill: {}".format(total_bill))


class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

class ElectronicItem(Product):
    pass

class GroceryItem(Product):
    pass

milk = GroceryItem("Milk", 40, 25, 3.5)
tv = ElectronicItem("TV", 45000, 40000, 3.5)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(milk, 2)
order.add_item(tv, 1)
order.display_total_bill()


# In[12]:


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))

class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def get_deal_price(self):
        return self.deal_price

    def display_product_details(self):
        print("{} {}".format(self.name, self.price))

class ElectronicItem(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months
      
    def get_warranty(self):
        return self.warranty_in_months

    def display_product_details(self):
        self.display_product_details()      
        print("Warranty {} months".format(self.warranty_in_months))

tv = ElectronicItem("TV", 45000, 40000, 3.5)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(tv, 1)
order.display_order_details()


# In[13]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def perimeter(self):
        return self.length * 4

box_1 = Square(4)
print(box_1.perimeter())


# In[14]:


class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x):
        super().__init__(x)
        
class C(B):
    def __init__(self, x):
        super().__init__(x)

p = C(20)
q = B(2)


# In[15]:


n = int(input())
for i in range(1, n+1):
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i - 2)
        numbers = "1 " + hollow_spaces + (str(i) + " ")
        print(numbers)
    else:
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers + (str(j) + " ")
        print(numbers)


# In[22]:


n = int(input())
a = n%100
print(a)


# In[29]:


word = input()

for char in word:
    if char.islower():
        char = char.upper()
    else:
        char = char.lower()
    print(char, end='')


# In[25]:


word = input()
print(word.islower())


# In[ ]:




