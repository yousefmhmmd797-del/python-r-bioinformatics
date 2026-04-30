dna = "ATGCGCAGTA"
g = dna.count("G")
c = dna.count("C")

gc = ((g + c) / len(dna)) * 100

print("GC Content:", gc, "%" )

#print(f"GC Content: {gc_content:.2f}%")