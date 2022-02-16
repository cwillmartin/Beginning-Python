x = 42
print("The value of x is",x)

print ("Hello World")

a=4
b=3
c=a+b
print(a,"+",b,"=",c)

"""decisions
The if statement
if some-condition-is-true:
do this
else:
do that  
Colon : after the IF clause
Everything after the IF and before the ELSE is indented
Don't always need the ELSE"""

if c>12:
    print("c is",c);
else:
    print ("c is not greater than 12","c is",c)
    
"""Loops
Repeat statements a fixed number of times or while some condition is true
WARNING! 
The range is 1 to 9 even tho the end is 10. 
Range is "up to but not including the end value" """

sum=0
for i in range (1,10):
    sum=sum+i
print("sum is",sum)