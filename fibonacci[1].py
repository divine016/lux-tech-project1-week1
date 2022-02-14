import math
def perfect_square(numb):
    number=int(math.sqrt(numb))
    return number*number == numb
n = int(input("enter a number \n"))
cond1= 5*(n*n)+4
cond2= 5*(n*n)-4
if perfect_square(cond1) or perfect_square(cond2):
    print("this number is a fibonamcci number") 
else:
    print("this number is not a fibonacci number.")