# make a list of mersenne numbers in a range of values

# check if the number is prime
def isPrime(x):
    check = True
    for i in range(2,x):
        if(x%i == 0):
            check = False
    return check    

lower_limit = int(input("input the lower limit:"))
upper_limit = int(input("input the upper limit:"))
results = []

n = 2
last_num = 0
while(True):
    if(last_num > upper_limit):
        break
    val = 2**n - 1
    if(isPrime(val)):
        last_num = val
        if(val > lower_limit and val < upper_limit):
            results.append(val)
    n += 1

print(results)