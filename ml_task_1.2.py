lst = ['0001','0011','0101','1011','1101','1111']

convert = lambda x : int(x,2)

converted = list(map(convert,lst))

# Required minimum difference is (Sum of all elems of list) - 2(Last element)

total = sum(converted)
greatest = max(converted)

new_lst = []
new_lst.append(total-greatest)
new_lst.append(greatest)

print(new_lst)



