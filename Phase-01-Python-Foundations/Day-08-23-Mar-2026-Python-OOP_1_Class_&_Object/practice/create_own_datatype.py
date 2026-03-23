class Fraction:
    #parameterized constructor : It is defined with parameters that allow us to initialize the attributes of the class when creating an object.
    def __init__(self,x,y):
        self.num=x
        self.den=y
        
        
# __str__ method is used to define the string representation of the object. 
# It is called when we print the object or convert it to a string.
    def __str__(self):
        return  '{} / {}'.format(self.num,self.den)
    
    
    #__add__ method is used to define the behavior of the addition operator (+) when applied to objects of the class.
    def __add__(self,other):
        new_num=self.num*other.den + self.den*other.num
        new_den=self.den*other.den
        return  '{}/{}'.format(new_num,new_den)
    
    def __sub__(self,other):
        new_num=self.num*other.den - self.den*other.num
        new_den=self.den*other.den
        return  '{}/{}'.format(new_num,new_den)
    def __mul__(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den
        return  '{}/{}'.format(new_num,new_den)
    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num
        return  '{}/{}'.format(new_num,new_den)
    
    def covert_to_decimal(self):
        return self.num/self.den    
    
fr1=Fraction(1,2)
print(fr1)
fr2=Fraction(3,4)
print(fr2)
 
print("Sum:",fr1+fr2)
print("Difference:",fr1-fr2)
print("Product:",fr1*fr2)
print("Quotient:",fr1/fr2)
print("Decimal value of fr1:",fr1.covert_to_decimal())
print("Decimal value of fr2:",fr2.covert_to_decimal())