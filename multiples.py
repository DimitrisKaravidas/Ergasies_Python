# -*- coding: utf-8 -*-
"""
Εργασία 8: Γράψτε ένα πρόγραμμα το οποίο παίρνει από το χρήστη δύο ακέραιους m και n
και στη συνέχεια εμφανίζει στο χρήστη το άθροισμα όλων των πολλαπλασίων του n μέχρι το m.
"""

def divisibles(below, *divisors):
    return (n for n in xrange(below) if 0 in (n%d for d in divisors))

num1 = int(raw_input("Give a positive integer: "))
while num1<=0:
    print "ERROR: %d is not correct! The number has to be natural(except for 0)!" %num1
    num1 = int(raw_input("Try again. Give the first number: "))

num2 = int(raw_input("Now, give a second positive integer: "))
while num2<=0:
    print "ERROR: %d is not correct! The numbers have to be natural(except for 0)!" %num2
    num2 = int(raw_input("Try again. Give the second number: "))

print "The sum of multiples of %d up to %d is" %(num1, num2), sum(divisibles(num2+1, num1))
