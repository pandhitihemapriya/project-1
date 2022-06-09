def fact(n):
 	if (n==1 or n==0):
	   return 1
	else:
	   y=n*fact(n-1)
	   return y
key=int(input("enter the number"))
print("the factorial of",key,"is",fact(key))
