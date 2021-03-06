

def f(x):
    return 1/(1+x)**2 #you can change this function for your equation

loLimit = float(input("Input the lower limit:"))
upLimit = float(input("Input the upper limit:"))
subInterval = float(input("Input the number of sub-intervals:"))
sum2 = 0.0

h = (upLimit-loLimit)/subInterval

sum1 = f(loLimit)+f(upLimit)

for i in range(1, int(subInterval)):
    sum2 += f(loLimit + i*h)
    
fx = (h/2)*(sum1 + 2*sum2)

print("Your result is: {}".format(fx))





