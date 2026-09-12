#largest = None
#smallest = None
#while True:
 #   num_str = input('Enter a number (or "done" to finish):\n')
  #  if num_str == 'done':
   #     break
    #num = float(num_str)
    #if largest is None or num > largest:
     #   largest = num
    #if smallest is None or num < smallest:
     #   smallest = num

#print('max', largest)
#print('min', smallest)


largest = None
print('before', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
        print('loop', itervar, largest)
print('largest', largest)