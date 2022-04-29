number =  int(input("Enter number:"))
sum = 0
answer = True
for i in range(1,number):
    if number % i == 0:
        sum = sum+i
if sum == number:
    answer = True
else:
    answer = False
print(answer)

