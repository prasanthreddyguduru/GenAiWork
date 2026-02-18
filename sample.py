def addition(a,b) :
    sum=a+b;
    return sum;
def subtraction(a,b) :
    sub=a-b;
    return sub
def multiplication(a,b):
    mul=a*b
    return mul
def division(a,b) :
    try :
        value=a/b;
        return value
    except ValueError:
        print ("please enter a number instead of string ..") 

print(addition(10,5))
print(subtraction(10,5))
print(multiplication(10,5))
print(division(10,5))