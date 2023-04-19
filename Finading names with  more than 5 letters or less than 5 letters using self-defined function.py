#Finading names with  more than 5 letters or less than 5 letters using self-defined function

def count(name):
    more_than5=0
    less_than5=0
    for i in name:
        if len(i)>=5:
            more_than5+=1
        else:
            less_than5+=1
    return more_than5,less_than5
names=[]
number=int(input("Please enter the number of names you want to check: "))
for a in range(number):
    input_names=input("Please enter a name and press enter: ")
    names.append(input_names)
more_than5,less_than5=count(names)
print("Names with letter more than 5 : {}\nNames with letter less than 5 : {}".format(more_than5,less_than5))