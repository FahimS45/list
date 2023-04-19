# A Python program to create a list by concatenating a given list with a range from 1 to n.

import ast
def concat (list1,n):
    new_list2 = []
    i=0
    for i in range(1,n+1):
        for a in list1:
            new_mem = str(a) + str(i)
            new_list2.append(new_mem)
        i+=1
    return new_list2
input_lst = ast.literal_eval(input("Please enter you list: "))
input_number = int(input("Please enter the value: "))
result = concat(input_lst,input_number)
print(result)
