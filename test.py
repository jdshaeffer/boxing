import threading
import time
import sys

str = 'disarm me by typing disarm'

def background(str):
    while True:
        time.sleep(2)
        print str

# runs regardless of user input
threading1 = threading.Thread(target=background, args=[str])
threading1.daemon = True
threading1.start()

while True:
    if raw_input() == 'disarm':
        print 'DONE'
        sys.exit()
    else:
        print 'not disarmed'