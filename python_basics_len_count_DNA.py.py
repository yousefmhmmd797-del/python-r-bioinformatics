# Task 1: Calculate DNA sequence length and count nucleotides in it

dna = "ATGCTAGCTAGCTAACG"
length = len(dna)

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

# Outputs

print("DNA sequence: ", dna)
print("The length: ", length)

print("A: ", a)
print("T: ", t)
print("G: ", g)
print("C: ", c)