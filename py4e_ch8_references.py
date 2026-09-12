from ast import Delete


cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123, 1]
empty = []

print(cheeses, numbers, empty)

for i in range(len(numbers)):
    #print(i)
    print(range(len(numbers)))
    #numbers[i]= numbers[i] * 2
    #print(numbers)

for x in empty:
    print('This never happens.')

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0]*4)
print([a]*3)
print([1, 2, 3]*3)
print(a*3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
print(t)
print([t])
t[1:4]=['x','z']
print(t)
t.append('n')
print(t)
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
t.extend(a)
print(t)
#t.sort()
#not supported between instances of 'int' and 'str'
print(t)

x = t.pop(2)
print(t)
print(x)

del t[4]
print(t)

#t.remove('1')
print(t)
#t.remove(2, 3) list.remove() takes exactly one argument (2 given)
print(t)
#t.remove[1] []is supposed to be a list
del t[:3]
print(t)

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

letters = ['l', 'Z', 'n']
print(max(letters))
#letters = [l, m, n]
#print(max(letters))
#print(min(letters))

#total = 0
#count = 0
#while (True):
#    inp = input('enter a number:')
 #   if inp == 'done': break
  #  value = float(inp)
   # total = total + value
    #count = count + 1
#average = total/count
#print('average', average)

#numlist = list()
#while (True):
    #inp = input('enter the name:')
   # if inp == 'done': break
  #  value = float(inp)
 #   numlist.append(value)

#average = sum(numlist)/len(numlist)
#print('average', average)

s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])

#s = 'spam-spam-spam'
#delimiter = '-'
#print(s.split(delimiter))
#t = ['pining', 'for', 'the', 'fjords']
#delimiter = 'yeo'
#print(delimiter.join(t))


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    #print(len(line))
    words = line.split()
    if len(words) < 3: continue
    print(len(words))
    print(words[2])
    #print(words[2])

a = [1, 2, 3]
b = a
b is a

b[0] = 17
print(a)

def delete_head(x):
    del x[0]

letters = [1, 2, 3]
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [3]
print(t3)
print(t1 is t3)
print(t1 is t2)
def bad_delete_head(t):
    t = t[1:]
print(bad_delete_head(t))
t = ['for' 'a' 'breath' 'I' 'tarry']
def tail(t):
    return t[1:]
print(tail(t))

t = [1, 2, 3, 4]
print(tail(t))
print(t)

poet = ['for', 'a', 'breath', 'I', 'tarry']
def chop(t):
    del t[0]
    del t[-1]
print(chop(poet))
print(poet)

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 1 or words[0] != 'From': continue
    print(words[2])