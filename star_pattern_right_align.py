n=int(input("enter number of rows to be printed:"))

for i in range(1,n+1):

    #To print spaces
    for k in range(0,n-i):
        print("",end=" ")

    #To print stars
    for j in range(1,i+1):
        print("*",end="")
    print("\n",end="")
