print ("List of amino acids and their")
print ("single-letter codes")
print ("_______________________\n")
amino_acids = {
    "Alanine": "A",
    "Arginine": "R",
    "Asparagine": "N",
    "Aspartic acid": "D",
    "Cysteine": "C",
    "Glutamic acid": "E",
    "Glutamine": "Q",
    "Glycine": "G",
    "Histidine": "H",
    "Isoleucine": "I",
    "Leucine": "L",
    "Lysine": "K",
    "Methionine": "M",
    "Phenylalanine": "F",
    "Proline": "P",
    "Serine": "S",
    "Threonine": "T",
    "Tryptophan": "W",
    "Tyrosine": "Y",
    "Valine": "V"
}

# Print each amino acid and its code
for amino_acid, code in amino_acids.items():
    print(f"{amino_acid} - {code}")
print ("_______________________\n")

input ("\tEnter to exit")
