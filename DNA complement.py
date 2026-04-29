# Task 4: DNA Complement

dna = "ATGC"
complement = ""

for base in dna:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement += "G"

print("Original: ", dna)
print("Complement: ", complement)