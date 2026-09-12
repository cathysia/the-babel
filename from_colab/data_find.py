data = 'From stephen.marquard@uct.az.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ')
print(sppos)
host = data[atpos+1 : sppos]
#host = data[sppos : atpos+1]
print(host)