# -*- coding: utf-8 -*-
"""
Εργασία 7: Δίνεται από το χρήστη μια σειρά από λέξεις χωρισμένες στο διάστημα, επιστρέψτε τη λέξη με το
μεγαλύτερο μήκος.
Αν υπάρχουν πολλές λέξεις με το μεγαλύτερο μήκος, επιστρέψτε την τελευταία εμφάνιση της λέξης με το μεγαλύτερο μήκος.
Παράδειγμα:
Είσοδος: 'red white blue'
Έξοδος “white”
Είσοδος: 'red blue gold' 
Έξοδος “gold”
"""

string = raw_input("Input some words to evaluate (use only alpha characters and spaces): ")

def main():
    y = sorted(string.split(), key=len) [-1]
    print "The longest word is", str(y) + "."

if not all(x.isalpha() or x.isspace() for x in string):
    print "Please use only alpha characters and spaces."
else:
    main()
