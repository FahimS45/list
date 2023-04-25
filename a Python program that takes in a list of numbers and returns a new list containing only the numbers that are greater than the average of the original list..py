# a Python program that takes in a list of numbers and returns a new list containing only the numbers that are greater than the average of the original list.

def greater_than_avg (lst):
    new_list = []
    total = sum(lst)
    avg = total/len(lst)
    for each in lst:
        if each > avg:
            new_list.append(each)
    return new_list

input_list = [int(i) for i in input("Please enter the values of your list, separating each value with a space: ").split( )]
result = greater_than_avg(input_list)
print(result)

