#Factorial Digit Length
#Returns the number of digits in a factorial of the user's choice
#Programmed by Mary Sonnabend

#import modules
import math

#digitNum-returns number of digits
def digitNum(n):
    digitNum = 0
    for d in n:
        digitNum += 1
    return digitNum

#program main
def main():
    testNum = input("Enter a number: ")
    if testNum.isdigit():
        print(digitNum(str(math.factorial(int(testNum)))))
    else:
        print("ERROR: Please enter a number")

#execute main
main()
