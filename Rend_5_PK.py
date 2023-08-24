import math

def isPrime(n):
    if n==1:
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
        
    return True


def factorPrime(a):
    
    i=1
    primes=[]
    
   
    
    while a!=1:
        
        if isPrime(i)==True:           
            
            while a%i==0:                
                a=a/i
            primes.append(i)
              
        i=i+1

    return primes


def factorExp(n):
    
    primes=factorPrime(n)
    exp=[]
    e=0

    for p in primes:
        e=0
        while (n%p==0):
            n=n//p      
            e+=1         
        exp.append(e)
    return exp


def gcd(a, b):
    
    while b != 0:
        a, b = b, a % b
        
    return a

def coprime(a, b):
    
    return gcd(a, b) == 1



def orderElement(g,n):
    card=0
    for i in range(1,n):
        
        if coprime(i,n)==True:
            card=card+1

    h=card
    e=h
    i=0
    primH=factorPrime(h)
    expH=factorExp(h)
    k=len(primH)

    for i in range(0,k+2):
        
        if len(primH)==1:
            i=i+1
            
            if(i>k):
                print("Az adott elem: " + str(g) + " rendje " + str(e) + "." )
                return e
            
            else:
                x=pow(primH[i-1],expH[i-1])
                print(x)
                e=e//x
                print(e)
                g1=pow(g,e)
                print(g1)
         
                o=g1%n
                print(o)
                
                if o!=1:
                    p1=primH[i-1]            
                    g1=pow(g1,p1)
                    e=e*x
                    print(e)
                    
                else:
                    print("Az adott elem: " + str(g) + " rendje " + str(e) + "." )
                    return e




            
        else:
            i=i+1
            
            if(i>k):
                print("Az adott elem: " + str(g) + " rendje " + str(e) + "." )
                return e
            
            else:
                x=pow(primH[i-1],expH[i-1])
                print(x)
                e=e//x
                print(e)
                g1=pow(g,e)
                print(g1)
         
                o=g1%n
                print(o)
                
                if o!=1:
                    p1=primH[i-1]            
                    g1=pow(g1,p1)
                    e=e*p1
                    print(e)
                    
                else:
                    print("Az adott elem: " + str(g) + " rendje " + str(e) + "." )
                    return e





def main():

    print(orderElement(7,10))

    
    return 0

main()
