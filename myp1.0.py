print("'Divisibility test'")
a = int( input("Enter a number: ") )
b = []
m=[]
if a < 0:
    print("Please enter a positive number")
else:
    for i in range(2 , a):

        if a%i == 0:
            b.append(i)
        else:
            m.append(i)

if len(b)==0:
    print("The given number %d is a prime number"%(a))
else:
    print("The given number %d is divisible by %s "%(a,str(b)))
print(m)