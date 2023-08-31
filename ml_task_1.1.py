jumbled_superheroes = ['DocToR_sTRAnge' , 'sPidERmaN' , 'Mo0N_KnigHT' , 'caPTAIN_aMERIca' , 'hULK' ]

decoded_names = []

indices = []

for count,value in enumerate(jumbled_superheroes):
    value = value.lower()
    value = value.replace('_',' ')
    value = value.replace('0','o')
    decoded_names.append(value) #so decoded_names now has cleaned names
    indices.append((count,value)) #indices is a list of tuples of format (index , name at that index)

length_finder = lambda string : len(string) 

name_lengths= list(map(length_finder,decoded_names)) #name_lengths now contains lengths of each corresponding name in decoded_names

indices.sort(key = lambda x : name_lengths[x[0]])
#we are sorting the list indices based on every 'x' present in it. the logic for sorting is , take x , which is a tuple , and take the first element of that tuple , which is the index of that value
# name_lengths[x[0]] is the  length of the current name , since x[0] is the index and the value at that index in name_lengths is the length ,  and it is what we are returning
# hence .sort() will use name lengths as a key to sort the list indices

print("Phase 5 kickoff list :")
for count,value in enumerate(indices,1):
    value = value[1] #actual name to print is the second element of every tuple in indices
    value = value.title()
    print(f'{count}: {value}')
