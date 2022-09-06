
#author:v.vivek
#program name:hallow square pattern
n=int(input("enter the numbers"))
for i in range (0,n+1):
    for j in range (0,n+1):  
       if (i==0 or j==0):
            print("*",end="")
       elif(i==n or j==n):
            print("*",end="")
       else:
            print(" ",end="")
    print() 
