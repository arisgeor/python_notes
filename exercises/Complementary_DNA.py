#! python3

"""
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to 
get the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell)

"""

def DNA_strand(dna):
    dna_list = []
    for elem in list(dna):
        if elem == 'A':
            dna_list.append('T')
        elif elem == 'T':
            dna_list.append('A')
        elif elem == 'G':
            dna_list.append('C')
        elif elem == 'C':
            dna_list.append('G')
    return ''.join(dna_list)


dna = 'ATTGC'
DNA_strand(dna)

#pretty easy.
#how i could have done it better:

def DNA_strand_better(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

#what I' ve learned:
#

