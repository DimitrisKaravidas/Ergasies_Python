# -*- coding: utf-8 -*-
"""
Εργασία 10: Μία πυθαγόρεια τριάδα είναι τρεις αριθμοί a,b,c για τους  οποίους ισχύει ότι a^2+b^2=c^2.
Γράψτε ένα πρόγραμμα το οποίο θα βρίσκει τις πυθαγόρειες τριάδες (αν υπάρχουν) οι οποίες θα έχουν
άθροισμα (a+b+c) ίσο με έναν αριθμό που παίρνει από το χρήστη.
"""

def error(r):
    print "Wrong input: %s is not an integer." %r

def pythagorean_triples(n):
        try:
            n=int(n)
            found = 0
            if n>0:
                for a in range(1,n-1):
                    for b in range(a+1,n):
                        for c in range(b+1,n+1):
                            if a*a + b*b == c*c and a + b + c == n:
                                found = 1
                                print(a,b,c)


            else:
                print "ERROR! You have to enter a positive integer!"
                n = raw_input("Try again: ")
                found = 1
                pythagorean_triples(n)

            if found == 0:
                print "Nothing found. There is no pythagorean triple so as to be a+b+c=%d." %n
        except ValueError:
            error(n)
               

n = raw_input("Enter a positive integer: ")

pythagorean_triples(n)
