#Collatz Chain Length Finder
#Prints the length of a Collatz Chain for any number n
#Programmed by Mary Sonnabend

def collatz(n, chainLen = 1):
    while n > 1:
        chainLen += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n)+ 1
    return chainLen

def main():
    startNumber = int(input("Pick a starting number: "))
    res = collatz(startNumber)
    print("The answer is " + str(res))

main()
