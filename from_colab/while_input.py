#while True:
 #   line = input('>')
  #  if line == 'done':
   #     break
    #print(line)
    #print('done!')

while True:
    line = input('>')
    if line[1] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('done')
