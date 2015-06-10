class Complex:
   def __init__(self, realpart=0, imagpart=0):          
        self.r = realpart
        self.i = imagpart
   def str (self):
         return "({0},{1})".format(self.x,self.y)
f=Complex(2.5,-3.7)
print(f.r,f.i)
print f