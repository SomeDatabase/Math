#Dumb Collatz
#Adapted from Project Euler Problem #14
#Programmed by Mary Sonnabend

#import time module to help judge runtime
import time

#start the clock!!!
start = time.time()

#collatz function--implements the collatz sequence
def collatz(n, chainLen = 1):
    while n > 1:
        chainLen += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n)+ 1
    return chainLen

def main():
    #upper bound of the values we're trying to find
    upperbound = 1000000

    #the current maximum collatz chain length
    maxLen = 0
    
    #number that creates current maximum value
    maxVal = 0
    for i in range(upperbound):
        res = collatz(i)
        if res > maxLen:
            maxLen = res
            maxVal = i

    #calculate total execution time
    end = time.time()
    total = end - start

    print("Found " + str(maxLen) + " at n = " + str(maxVal) + " with a time of " + str(total) + "s.")
    #end main

#execute main
main()
