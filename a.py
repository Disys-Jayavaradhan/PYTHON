class laptop:
    def __init__(self,a,b,c):
        self.brand= a
        self.ram=b
        self.rom=c

    def config(self):
        print('the lapt is', self.brand, self.ram, self.rom)

customer1 = laptop('lenovo',4,250)
customer2 = laptop('dell',8,249)
customer3 = laptop('thinkpad',4,500)

customer1.config()
customer2.config()
customer3.config()


class phone:
    def __init__(self, A, B, C):
        self.Brand = A
        self.Ram = B
        self.Rom = C

    def config(self):
        print("the phone is", self.Brand, self.Ram, self.Rom)

SP = phone('MI', 8, 65)
SP1 = phone('MI', 8, 128)

SP.config()
SP1.config()

class books:
    def __init__(self, a, b, c):
        self.bookname = a
        self.firstedition = b
        self.lastedition = c
    def config(self):
        print('this books is', self.bookname, self.firstedition, self.lastedition)

customer = books('the jungle', 2001, 2002)
customer1 = books('the zoo', 2004, 2006)
customer2 = books('30 steps to success', 2005, 2008)




customer.config()
customer1.config()
customer2.config()

class coder:
   loc=1000
   def __init__(self):
      self.error=20
jv=coder()
print(jv.error)

activ=(500,300,309,290)
print(activ[4])
game=[1,5,3]
print(games[1])
