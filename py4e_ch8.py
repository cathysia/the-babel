print(range(4))
friends = ['joseph', 'glenn', 'sally']
print(len(friends))
print(range(len(friends)))
print(list(range(len(friends))))

friends = ['joseph', 'gelenn', 'sally']
for friend in friends:
  print('Happy New Year,', friend)

for  i in range(len(friends)):
  friend = friends[i]
  print('Happy New Year,', friend)

x = list()
type(x)
dir(x)

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

some = [1, 9, 21, 10, 16]
9 in some
15 in some

friends = ['joseph', 'glenn', 'sally']
friends.sort()
print(friends)
print(friends[1])

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# total = 0
#count = 0
#while True:
  #inp = input('enter a name:')
  #if inp == 'done': break
  #value = float(inp)
  #total = total + value
 # count = count + 1
#avarage = total/count
#print('avarage is', avarage)

numlist = list()
while True:
  inp = input('enter a number')
  if inp == 'done': break
  value = float(inp)
  numlist.append(value)
average = sum(numlist)/len(numlist)
print('average', average)