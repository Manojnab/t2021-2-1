class calculator:
    def __init__(self,a):
        self.__a=a
        
    def __sub__(self,c):
        return self.__a-c.__a
    def __add__(self,c):
        return self.__a+c.__a
    def __mul__(self,c):
        return self.__a*c.__a
    def __truediv__(self,c):
        return self.__a/c.__a
a=float(input())
b=float(input())
c1=calculator(a)
c2=calculator(b)
while True:
    print("enter sum or sub or div or mul as input and get the desired result and press q to quit")
    type_of_operation=input()
    if type_of_operation=='sum':
        print(c1+c2)
    elif type_of_operation=='sub':
        print(c1-c2)
    elif type_of_operation=='div':
        print(c1*c2)
    elif type_of_operation=='mul':
        print(c1/c2)
    elif type_of_operation=='q':
        break
    else:
        print("entera valid operation")
    

    
        
