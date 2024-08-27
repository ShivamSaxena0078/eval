input="The Ganges is the longest river in India while The Nile in World "
rev=""
c=""
for i in range(len(input)):
    
    if (input[i]!=" "):
        c+=input[i]
    else:
        rev=c+rev
        
        c=""
        continue
    
print(rev)
    


    
