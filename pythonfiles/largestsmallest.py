largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    num = num-1
        try:
            if largest is None:
        	          largest = num
    	    elif num>largest:
        	          largest=num
    	    if smallest is None:
                      smallest=num
            elif num<smallest:
        	          smallest=num

	     except:
               if num == "done" :
                    break
               else:
                    print("Invalid input")

print("Maximum is ", largest+1)
print("Minimum is ",smallest+1)
