#Function Composition
#Programmed by Mary Sonnabend


#Function: myFunc
#Accepts x and n as parameters
#x is the value we're passing in to be executed by the function
#n is a counter variable to keep track of the recursion
def myFunc(x, n):
    x = 2.8 * x * (1 - x)
    if n == 0:
        return x
    else:
        return myFunc(x, n-1)

#program main
def main():
    n = 5 #this value is intentionally low for debugging purposes, feel free to adjust as needed
    x = 0.5
    res = myFunc(x, n)
    print(str(res))
    
main()
