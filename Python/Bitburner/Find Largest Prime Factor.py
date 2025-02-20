x = 28843876
primes = []
primeFlag = False
while not primeFlag:
    print(f"Current Primes: {primes}")
    littlePrime = False
    for i in range(2,x+1):
        if x % i == 0 and littlePrime == False:
            primes.append(int(i))
            x = int(x/i)
            littlePrime = True
            break
        elif littlePrime == True:
            break
    if not littlePrime:
        primeFlag = True
print(f"Prime Factorization: {str(primes)}")
print(f"Largest Factor: {max(primes)}")
input("hit enter to exit")