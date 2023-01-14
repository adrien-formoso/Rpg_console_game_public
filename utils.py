import time
import sys

def script(var,num,num2):
    for character in var:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(num)
    time.sleep(num2)