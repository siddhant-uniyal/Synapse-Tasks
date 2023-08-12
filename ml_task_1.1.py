jumbled_superheroes = ['DocToR_sTRAnge' , 'sPidERmaN' , 'Mo0N_KnigHT' , 'caPTAIN_aMERIca' , 'hULK' ]

decoded_names = []

for value in jumbled_superheroes:
    value = value.lower()
    value = value.replace('_',' ')
    value = value.replace('0','o')
    decoded_names.append(value)

indices = decoded_names

str_length = lambda string : len(string)

name_lengths= list(map(str_length,decoded_names))

indices.sort(key=len)

print("Phase 5 kickoff list :")
for count,value in enumerate(indices,1):
    value = value.title()
    print(f'{count}: {value}')



    


