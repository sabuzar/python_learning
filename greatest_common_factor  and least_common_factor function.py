first_divser = 3
second_divser = 9
factor = 0
def gcd_operation(first_deviser, second_deviser, factor,operation):
    if operation == "gcf":
         for gcf in range(1,first_divser+1):
             if (first_divser % gcf==0) and (second_divser % gcf ==0):
                 factor = gcf
         print(factor)

    if operation == 'lcm':
        gcd = 0
        lcm = 0
        for gcf in range(1, first_divser + 1):
            if (first_divser % gcf == 0) and (second_divser % gcf == 0):
                factor = gcf
        gcd = factor
        lcm = int(first_divser / gcd * second_divser / gcd * gcd)
        print(lcm)


gcd_operation_function_required="gcf"
gcd_operation(first_divser,second_divser,factor,gcd_operation_function_required)









