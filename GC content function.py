#GC content function 

def calculate_gc(dna):
    g = dna.count("G")
    c = dna.count("C")
    gc_content = ((g + c) / len(dna)) * 100
    return gc_content

#testing the function

sequence = "ATGCGCAGTA"
result = calculate_gc(sequence)

print(f"GC Content: {result:.2f}%")