num = 5
isprime = True
for i in range(2, num):
    if num%i==0:
        isprime = False
        break
print(isprime)