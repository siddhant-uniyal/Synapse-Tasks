''' final output is [x , 48-x] where x is the sum of any number of elements 
for req min diff maximise x --> since it is (48-2*x)
ideal situation is [24,24]
any x which is at the least distance from 24 is the req result
start a loop on the reverse sorted list , reverse sorting for least steps.
store running sum
compare current distance of the running sum from 24 and the distance of the first(greatest) elem from 24 on each itern
once min distance obtained , break and append into req_list 
'''

given_list = ['0001','0011','0101','1011','1101','1111']

convert = lambda x : int(x,2)

sorted_list =  sorted(list(map(convert,given_list)),reverse = True)

req_list = []

total = sum(sorted_list)

x = int(total/2)

running_sum = 0

starting_distance = abs(sorted_list[0] - x) 

last_elem = 0

for index,value in enumerate(sorted_list):
    running_sum+=value
    current_distance = abs(running_sum - x)
    if(current_distance==min(starting_distance,current_distance) and not current_distance==starting_distance):
        last_elem = running_sum


req_list.append(last_elem)
req_list.append(total-last_elem)
print(req_list)







