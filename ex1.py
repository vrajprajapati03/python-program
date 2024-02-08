'Write a Python function to find the maximum of three numbers'

def maximum(a, b, c): 

	if (a >= b) and (a >= c): 
		largest = a 

	elif (b >= a) and (b >= c): 
		largest = b 
	else: 
		largest = c 
		
	return largest 


 
a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))
print(maximum(a, b, c)) 
