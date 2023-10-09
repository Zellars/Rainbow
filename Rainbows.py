import time, sys
try:
    import bext
except ImportError:
    print('This program require the bext module, which you')
    print('can install by following instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

time.sleep(3)
indent = 0
indentIncreasing = True

import time, sys #the time module provides various time-related functions
#sys can provide information about the system that code is being run on

try: #lets you test a block of code for errors
    import bext
except ImportError: #we are handling the error in case of imports not being installed
     print('This program requires the bext module, which you')
     print('can install by following the instructions at')
     print('https://pypi.org/project/Bext/')
     sys.exit()

print('Press Ctrl-C to stop.')
time.sleep(3) #code pauses for a moment before the program runs

indent = 0  # How many spaces to indent.
indentIncreasing = True  # Whether the indentation is increasing or not.

#this program continuously prints the same rainbow pattern. What changes is the number of
#space characters printed to the left of it. Inceasing this number moves the raibow to the right
#decreasing it moves the rainbow to the left....
try:
    while True:  # Main program loop.
         print(' ' * indent, end='')
         bext.fg('red')
         print('##', end='')
         bext.fg('yellow')
         print('##', end='')
         bext.fg('green')
         print('##', end='')
         bext.fg('blue')
         print('##', end='')
         bext.fg('cyan')
         print('##', end='')
         bext.fg('purple')
         print('##')
#The indentIncreasing variable is set to True to note that indent should increase until it
#reaches 60.... at which point it changes to false....

#The rest of the code decreases the number of space... Once it reaches 0, it changes back
#to true again to repeat the zigzag pattern

         if indentIncreasing:
             # Increase the number of spaces:
             indent = indent + 1
             if indent == 60:  # (!) Change this to 10 or 30.
                 # Change direction:
                 indentIncreasing = False
         else:
             # Decrease the number of spaces:
             indent = indent - 1
             if indent == 0:
                 # Change direction:
                 indentIncreasing = True

         time.sleep(0.02)  # Add a slight pause.
except KeyboardInterrupt:
     sys.exit()  # When Ctrl-C is pressed, end the program.