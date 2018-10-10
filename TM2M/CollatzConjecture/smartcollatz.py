#Smart Collatz
#Adapted from Project Euler Problem #14
#Programmed by Mary Sonnabend

#import time module to help judge runtime
import time

#start the clock!!!
start = time.time()

#lookup-creates a lookup table 
lookup = {}

#collatz function--implements the collatz conjecture and saves lengths 
def collatz(n):
    if not n in lookup:
        if n == 1:
            lookup[n] = 1
        if n % 2 == 0:
            lookup[n] = collatz(n//2)+ 1
        else:
            lookup[n] = collatz(3*n + 1) +1
    return lookup[n]

#program main
def main():
    #upper bound of what we're looking for
    upperbound = 1000000
    #find collatz lengths for numbers
    for i in range(1, upperbound):
        collatz(i)
    #find the max in the lookup table
    maxVal = max(lookup, key=lookup.get)
            
    #calculate total execution time
    end = time.time()
    total = end - start

    print("Found max at n = " + str(maxVal) + " with a time of " + str(total) + "s.")
 #   end main

#execute main
main()
