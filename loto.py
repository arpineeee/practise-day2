from random import randint
lst = [None] * 6
ind = 0
while ind < 6:
      lst[ind] = randint(1, 49)
      ind += 1
count = 0
for i in range(6):
      for j in range(i + 1, 5):
           if lst[i] == lst[j]:
                print("There are repeted numbers.")
                count += 1
           else:
                 continue
if count == 0:
      print("The numbers are not repeted.")
for i in range(6):
      for j in range(i + 1, 6):
            if lst[i] > lst[j]:
                  lst[i], lst[j] = lst[j], lst[i]
            else:
                  continue

print(f'The numbers of loto are: {lst}')
