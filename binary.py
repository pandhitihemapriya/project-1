def binary(array,low,high,element):
	if high>=low:
	   mid=(high+low)//2
	   if(array[mid]==element):
		return mid
	   elif(array[mid]>element):
		return binary(array,low,mid-1,element)
	   else:
		return binary(array,mid+1,high,element)
	else:
	   return 0
array=[2,45,6,12,40]
print("the list is ",array)
element=int(input("enter an element to search"))
output=binary(array,0,len(array)-1,element)
if output !=0:
	print("the element is found at",output)
else:
	print("element is not present in the list")
