a = 2
second_last = 0
last = 1

def fibonacci_operation(a,second_last,last,operation):
    if operation == 'range':
        a = 10
        second_last = 0
        last = 1
        for i in range(0, a + 1):
            if i == 0:
                second_last = i
                print(i)
            if i == 1:
                last = i
                print(i)
            if i > 1:
                f = second_last + last
                print(f)
                second_last = last
                last = f
    if operation == 'th':
        a = 10
        second_last = 0
        last = 1
        for i in range(0, a + 1):
            if i > 1:
                f = second_last + last
                second_last = last
                last = f
        print(f)
op = 'range'
fibonacci_operation(a,second_last,last,op)