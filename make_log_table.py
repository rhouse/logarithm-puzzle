# make_log_table.py  --  Compute and print special log table
#
# Written by Roger House
# Started:  2019 May 19

import math

NUM_ROWS = 60
NUM_COLS = 16

log_table = [[None for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
str_table = [[None for j in range(NUM_COLS)] for i in range(NUM_ROWS)]

def mylog(m):       # m is in minutes (time or arc)
    return 0.1111       # replace this line to solve the puzzle

def make_log_table():
    minutes = 0
    for j in range(NUM_COLS):
        for i in range(NUM_ROWS):
            if minutes == 0:
                log_table[0][0] = -1    # no log value in upperleft corner
            else:
                log_table[i][j] = mylog(minutes)
            minutes += 1

def prepare_table():
    global str_table
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            elem = log_table[i][j]
            if elem < 0:
                str_elem = " "*6
            else:
                str_elem = "{:06.4f}".format(elem)
                if j > 2:
                    str_elem = str_elem[-4:]
            str_table[i][j] = str_elem
            
        
def print_table():
    header = ("       0      1      2     3    4    5    6    7    8" +
              "    9   10   11   12   13   14   15     ")
    print(header)
    for i in range(NUM_ROWS):
        print(" {:2d} ".format(i), end='')
        for j in range(NUM_COLS):
            if j != 0:
                print(" ", end='')
            print(str_table[i][j], end='')
        print(" {:2d} ".format(i))
    print(header)

def main():
    print("Begin make_log_table")

    make_log_table()
    prepare_table()
    print_table()

    print("End make_log_table")
    
main()

# end make_log_table.py
