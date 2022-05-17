num = [1,2,9,7,6,8,5]
even_num = 0
odd_num = 0
for i in num:
   if i % 2 ==0:
      even_num = 1 + even_num
   else:
      odd_num = 1+ odd_num
print(even_num)
print(odd_num)
