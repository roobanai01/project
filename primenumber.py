'''a=input("Enter the Value:")
b=input("Choose square or cube:")
if "square" in b:
    c=int(a)*int(a);
    print("The square Value of "+ a +" is:",c)
elif "cube" in b:
    c=int(a)*int(a)*int(a);
    print("The cube Value of " " is:",c)
else:
    print("Please choose the correct option.")'''


n=int(input("Enter the number:"))
flag=False
if n==1:
    print(n," is not a prime number.")
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            flag=True            
            print(n," is not a prime number.")
            break
        else:
            print(n," is a prime number.")
            break