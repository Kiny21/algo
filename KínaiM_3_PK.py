from sympy import mod_inverse



def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x


def tombRendezes(t):
    for i in range(0,len(t)-1):
        for j in range(i+1,len(t)):
            if t[i] > t[j]:
                tmp=t[i]
                t[i]=t[j]
                t[j]=tmp
    return t



def chineseRemaider(numb, mod):

    j=2
    k=len(mod)
    tombRendezes(numb)
    tombRendezes(mod)
    eredmeny=0
    
    
    for i in range(0,len(mod)):
         for j in range(0,len(mod)):
             if i !=j: 
                 if gcd(mod[i], mod[j])!=1:
                     i=i+1
                     print('Páronként nem relatív prímek!')
                     break;

    
    prod=1

    for i in range(0,len(mod)):
        prod=prod*mod[i]
        i=i+1
        
    M=prod
    
    print(M)
        
    for i in range(0,k):
        s= M// mod[i]

        eredmeny = eredmeny + numb[i]*mod_inverse(s,mod[i])*s
    

    return eredmeny % M

    



def main():
    numb=[1,4,6]
    mod=[3,5,7]
    print(chineseRemaider(numb,mod))
    
    
    return 0

main()
