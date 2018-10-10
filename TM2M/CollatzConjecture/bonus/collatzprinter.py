#Collatz Chain Printer
#A simple program to print Collatz Chains
#Programmed by Mary Sonnabend

def collatz(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            print(str(int(n)))
        else:
            n = (3 * n)+ 1
            print(str(int(n)))

def main():
    startNumber = int(input("Pick a starting number: "))
    collatz(startNumber)

main()
