#Math Problem of the Week
#Programmed by Mary Sonnabend

#function: findDivisors(n)
#finds numbers that evenly divide 6 or 15, but not both
def findDivisors(n):
    for i in range(1,n):
        if (i % 6 == 0) ^ (i % 15 == 0):
            divs.append(i)
#function: sumList
#takes our list of numbers and counts the elements
def sumList(divs):
    count = 0
    for i in range(len(divs)):
        count += 1
    return count


#program main

#list to hold divisors
divs = []

#our upper limit
num = 1000000 

#call to find numbers that evenly divide 6 or 15
findDivisors(num)

#call to find the total
theSum = sumList(divs)

#display the result
print( "The number is " + str(theSum))
