first_divser = 24
second_divser = 12
factor = 0
gcd = 0
lcm = 0
for gcf in range(1,first_divser+1):
    if (first_divser % gcf==0) and (second_divser % gcf ==0):
        factor = gcf
gcd = factor
lcm = (first_divser/gcd * second_divser/gcd * gcd)
print(lcm)