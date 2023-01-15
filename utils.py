import time
import sys

def script(var,num,num2):            #fonction pour écrire le texte lettre par lettre + mettre un délai après le msg
    for character in var:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(num)
    time.sleep(num2)