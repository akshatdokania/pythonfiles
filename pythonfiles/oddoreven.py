s=list()
n=int(input("Enter no. of elements"))
for i in range(n):
    num = int(input("Enter no."))
    s.append(num)
print("Array:",s)
for i in s:
    if int(i)%2==0:
        print(i, " is even")
    else:
        print(i, " is odd")
