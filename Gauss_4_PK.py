# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:20:11 2020

@author: Kinga
"""



import numpy as np  



def Gauss(a,b):
    A=np.matmul(a,a)
    B=np.matmul(b,b)
    go=True

        


    if A<B:
        l=a
        a=b
        b=l

        L=A
        A=B
        B=L

    while(go):
            
        n=np.matmul(a,b)
        print(n)
        r=n//B
        T=A-2*r*n+r*r*B
        
        print(B)
        print(T)
        print(a)
        print(r)

        if T>=B:
            return b
        
        else:
            u=r*np.array(b)
            t=np.subtract(a,u)
            a=b
            b=t
            A=B
            B=T
            go=True
            



def main():
    a=(1,0,5)
    b=(8,10,13)
    print(Gauss(a,b))

    
    return 0


main()
