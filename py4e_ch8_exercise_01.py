fh = open('romeo.txt')
lst = list()
for line in fh:
    line = line.rstrip()
    lin_split = line.split()
    #print(lin_split)
    for word in lin_split:
        if word in lst: continue
        lst.append(word)
        lst.sort()
print(lst)
    

#for word in new_ap:
#    if word != lst:
#        lst.append(word)
#        lst.sort()
#print(lst)
#lst.extend(new_ap)

#for word in lst:
 #   print(word)
    

        

