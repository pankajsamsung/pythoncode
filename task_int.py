#! /usr/bin/env python3
## a = [1,2,3,4,5,6,7]

## a = [1,2,3,4,5,6,7] 

def myfun(a,sum=6):
    for i in range(len(a) - 1):
            #print (a)    
            #print("i: ", i)
            
            j=i+1
            while j < (len(a)):
                 if ((a[i] + a[j]) == sum):
                        print (a[i], a[j])
                 j=j+1
                        

myarr = [1,4,5,2,3,3,1]
x = myfun(myarr)
