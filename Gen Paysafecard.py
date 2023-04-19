import random
import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
def main():
    os.system('cls')
    code=''
    for _ in range(15):
        rand = random.randint(0,9)
        code = (code+str(rand))
    fcode=('0'+code)
    print(fcode)
    addToClipBoard(fcode)
    input("Press Enter to continue...")
    main()
main()

#by MaskeZen https://github.com/MaskeZen945961