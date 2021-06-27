# This is a module

class MyMath:
    def isEven(num):
        if(num%2==0):
            return True
        return False
    
    def isOdd(num):
        if(num%2==0):
            return False
        return True
    
    def isPrime(num):
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    
class Calsi:
    def add(num1, num2):
        return num1+num2
    
    def sub(num1, num2):
        return num1-num2
    
    def mul(num1,num2):
        return num1*num2
    