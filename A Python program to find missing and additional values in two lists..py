# A Python program to find missing and additional values in two lists.
def compare(lst1,lst2):
    common_list = []
    additional_list = []
    for each in lst2:
        if each in lst1:
            common_list.append(each)
        else:
            additional_list.append(each)

    return common_list, additional_list
result = compare([10,20,30],[10,50,30])
print(result)
a = result[0]
b = result[1]
print(f"Common: {a} and additional: {b}")
