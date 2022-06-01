import threading
import time

cmd = ''
state = 'stopped'

def timer():
    seconds_elapsed = 0
    global state
    while True:
        if cmd == 's':
            time.sleep(0.01)
            seconds_elapsed += 0.01
            print('seconds elapsed:{}'.format(round(seconds_elapsed, 4)))
            state = 'running'
        elif cmd == 'p' and state != 'stopped':
            seconds_elapsed = 0
            print('Stopped')
            state = 'stopped'
        elif cmd == 'r':
            seconds_elapsed = 0
            print(seconds_elapsed)

t1 = threading.Thread(target=timer)
t1.start()
while True:
    cmd = input('enter s for start, p for stop and r for reset: ')
