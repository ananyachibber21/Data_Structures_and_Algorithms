''' Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function'''

l = []
num = int(input("Enter a maximum number for the list: "))
for i in range(1,num+1):
    if(i%2==1):
        l.append(i)
print(l)