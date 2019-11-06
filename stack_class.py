# Class Point
class Point:
    def __init__(self, x=0, y=0):
# x and y are called instance variables, they are unique for each instances we create
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y) ** 2) ** 0.5

    def print_point(self):
        return '[{}, {}]'.format(self.x, self.y)

    def distance_to(self, another_point):
        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5

    def mid_point_of(self, other):
        return '({}, {})'.format((self.x + other.x) / 2, (self.y + other.y) / 2)

    def calculate_equation(self, second_point):
        if self.y == second_point.y:
            return '({}, {})'.format(0, self.y)
        elif self.x == second_point.x:
            return "vertical line"
        else:
            m = (second_point.y - self.y) / (second_point.x - self.x)
            c = self.y - m * self.x
            return '({}, {})'.format(m, c)


p = Point(1, 2)
q = Point(5, 5)


## another way of priniting : using the class itself
# print(Point.calculate_equation(p, q))
# print(Point.distance_from_origin(p))

# print(p.print_point())
# print(p.distance_to(q))
# print(p.distance_from_origin())
# print(p.mid_point_of(q))
# print(p.calculate_equation(q))


## Class SMSstore

class SMSstore:
    def __init__(self, has_been_viewed, from_number, time_arrived, text_of_SMS):
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS


## ADDITIONAL: Class Employee
class Employee:
    # raise_ amount is a class variable and hence it is common to every instance
    # it is still possible to change it in one instance
    number_of_employees = 0
    raise_amount = 0.1

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@student.uhasselt.be"
        # Since this initiation runs every time we create an instance, we put it here
        #  and use the class Employee
        Employee.number_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.salary = self.salary + self.salary * self.raise_amount
        # NOte: we can access the class variable either through the class
        # itself as (Employee.raise_amount) or an instance of the class as
        # self.raise_amount


empl_1 = Employee("hab", "fiseha", 200)
empl_2 = Employee("add", "fish", 100)
## the following will give the same result = 0.1: showing that the class variable is the
# for every instance within the class
# print(Employee.raise_amount)
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)


## if we want to get a given instance as a dictionay, we can do the following :
# print(empl_1.__dict__)
# print(empl_2.__dict__)
# In the above instnces both don't contain the calss variable raise_amount, but they are
#  accessing it form the class blew
# print(Employee.__dict__)
# if we want to change the value of the class variable, we can do it as:
Employee.raise_amount = 0.5
# if we print the above print fun, the value of the class variable is change in the class
#  as well as in all the instances within the class.
# print(Employee.raise_amount)
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)
# if we want to change the value of a class variable in one instace only, say empl_1, we:
# empl_1.raise_amount = 0.2
# print(Employee.raise_amount)
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)

## Moreover, is we take the dictionary of the empl_1 instance,
#  the variable raise_amount is part of it:
# print(empl_1.__dict__)
# To print the number of employees:
# print(Employee.number_of_employees)
# print(empl_1.full_name())
# print(empl_1.email)
# print(empl_1.salary)
# empl_1.pay_raise()
# print(empl_1.salary)
message = empl_1.__dict__
message["raise_amount"] = 2.5
print(message)
message["raise_amount"] = 4
print(message)
del message["raise_amount"]
print(len(message))
for k in message.values():
    k = str(k)
    if k[0] == "h":
        print(k)
    else:
        print(0)


class Stack(object):
    """ Creating a Stack class"""

    def __init__(self):
        self._List = []

    def push(self, x):
        self._List.append(x)

    def pop(self):
        if len(self._List) < 1:
            return None
        return self._List.pop()

    def empty(self):
        return len(self._List) == 0


def fibon_stack(x):
    s = Stack()
    s.push(x)
    val = 0
    while not s.empty():
        w = s.pop()
        if w == 1:
            val += 1
        if w > 1:
            s.push(w - 2)
            s.push(w - 1)
    return val


# print(fibon_stack(4))
letters = ["a", "b", "c", "d"]


class Registery:
    def __init__(self, totalitem=0, totalprice=0):
        self.totalprice = totalprice
        self.totalitem = totalitem
        # self._totalitem = 0
        # self._totalprice = 0

    def addItem(self, price):
        self.totalitem += 1
        self.totalprice += price

    def getprice(self):
        return self.totalprice

    def getItem(self):
        return self.totalitem

    def clear(self):
        self.totalprice = 0
        self.totalitem = 0


# register = Registery()
# register.addItem(12)
# register.addItem(2.5)
# register.addItem(2)
# print(register.totalitem)
# print(register.totalprice)
# register.clear()
# print(register.totalitem)
# print(register.totalprice)
# class Bank:
#     def __init__(self, Ibalance = 0):
#         self.Ibalance = Ibalance
#     def deposite(self, amount):
#         self.Ibalance += amount
#     def withdraw(self, amount):
#
#         if self.Ibalance >= 10 and self.Ibalance < amount:
#             self.Ibalance -= 10
#         else:
#             self.Ibalance -= amount
#     def interst(self, rate):
#         self.Ibalance = self.Ibalance + (self.Ibalance *(rate/100))
#     def getBalance(self):
#         return self.Ibalance
# doc = Bank(100)
# doc.deposite(120)
# doc.deposite(230)
# doc.deposite(50)
# print(doc.getBalance())
# doc.interst(10)
# print(doc.getBalance())
# doc.withdraw(1000)
# print(doc.getBalance())

class SMSstore:

    def __init__(self, viewed):
        self._store = []
        # self.viewed = viewed
        self.msg_count = 0

    def add_new_arrivals(self, number, time, msg):
        self._store.append(tuple((number, time, msg)))

    def message_count(self):
        return len(self._store)

    # def get_unread_msgs(self):

    def get_messages(self, indx):
        if indx < len(self._store):
            return self._store[indx]
        else:
            return None


class Register:
    def __init__(self, tprice=0, tamount=0):
        self.tprice = tprice
        self.tamount = tamount

    def addItem(self, price):
        self.tprice += price
        self.tamount += 1

    def getTamount(self):
        return self.tamount

    def getTprice(self):
        return self.tprice

    def clear(self):
        self.tprice = 0
        self.tamount = 0


reg1 = Register()
reg1.addItem(12)
reg1.addItem(2.5)
reg1.addItem(2)
print(reg1.getTamount())
print(reg1.getTprice())
reg1.clear()
print(reg1.getTprice())
print(reg1.getTamount())
