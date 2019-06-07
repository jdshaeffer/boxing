import threading
import time
import sys

def background():
    while True:
        time.sleep(3)
        print 'disarm me by typing disarm'

# runs regardless of user input
threading1 = threading.Thread(target=background)
threading1.daemon = True
threading1.start()

while True:
    if raw_input() == 'disarm':
        print 'DONE'
        sys.exit()
    else:
        print 'not disarmed'