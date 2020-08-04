n=int(input("Enter the number"))
fc=0
for i in range(2,n):
    if n%i==0:
        fc+=1
if fc==2:
    print('prime')
else:
    print('not prime')
