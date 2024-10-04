
print ("********************************************************************")
print ("The program is designed to calculate molecular weight  ")
print ("of standard amino acids and highlight suitable candidates")
print ("\t toward drug discovery.")
print ("********************************************************************")
print ("\t Enter first single code letter of each essential amino acid")
print ("Avoid entering blank spaces, punctuation, numbers, and symbols\n")



def amino_acid_composition():
    return {
        'A': {'C': 3, 'H': 7, 'N': 1, 'O': 2},  # Alanine
        'C': {'C': 3, 'H': 7, 'N': 1, 'O': 2, 'S':1},  # Cysteine
        'D': {'C': 4, 'H': 7, 'N': 1, 'O': 4},  # Aspartic Acid
        'E': {'C': 5, 'H': 9, 'N': 1, 'O': 4},  # Glutamic Acid
        'F': {'C': 9, 'H': 11, 'N': 1, 'O': 2}, # Phenylalanine
        'G': {'C': 2, 'H': 5, 'N': 1, 'O': 2},  # Glycine
        'H': {'C': 6, 'H': 7, 'N': 3, 'O': 1},  # Histidine
        'I': {'C': 6, 'H': 13, 'N': 1, 'O': 2}, # Isoleucine
        'K': {'C': 6, 'H': 14, 'N': 2, 'O': 2}, # Lysine
        'L': {'C': 6, 'H': 13, 'N': 1, 'O': 2}, # Leucine
        'M': {'C': 5, 'H': 11, 'N': 1, 'O': 2,'S':1}, # Methionine
        'N': {'C': 4, 'H': 8, 'N': 2, 'O': 3},  # Asparagine
        'P': {'C': 5, 'H': 9, 'N': 1, 'O': 2},  # Proline
        'Q': {'C': 5, 'H': 10, 'N': 2, 'O': 3}, # Glutamine
        'R': {'C': 6, 'H': 12, 'N': 4, 'O': 2}, # Arginine
        'S': {'C': 3, 'H': 7, 'N': 1, 'O': 3},  # Serine
        'T': {'C': 4, 'H': 9, 'N': 1, 'O': 3},  # Threonine
        'V': {'C': 5, 'H': 11, 'N': 1, 'O': 2}, # Valine
        'W': {'C': 11, 'H': 12, 'N': 2, 'O': 2},# Tryptophan
        'Y': {'C': 9, 'H': 11, 'N': 1, 'O': 3}  # Tyrosine
    }

def calculate_molecular_formula(sequence):
    composition = amino_acid_composition()
    total_counts = {'C': 0, 'H': 0, 'N': 0, 'O': 0,'S' :0}

    for aa in sequence:
        if aa in composition:
            for atom, count in composition[aa].items():
                total_counts[atom] += count
        else:
            raise ValueError(f"Invalid amino acid: {aa}")

    # Construct molecular formula string
    formula1 = ""
    for atom, count in total_counts.items():
        if count > 0:
            formula1 += f"{atom}{count}"

    return formula1

# Example usage
sequence = input("Enter an amino acid sequence (single letter codes): \n").strip().upper()
try:
    formula1 = calculate_molecular_formula(sequence)
    print(f"Molecular formula: {formula1}\n")
except ValueError as e:
    print(e)

from collections import Counter
# Atomic weights (g/mol)
atomic_weights = {

    'H': 1.01,    # Hydrogen
    'C': 12.01,   # Carbon
    'N': 14.01,   # Nitrogen
    'O': 16.00,   # Oxygen
    'F': 19.00,   # Fluorine
    'P': 30.97,   # Phosphorus
    'S': 32.07,   # Sulfur
   

    
}

def parse_formula(formula):
    elements = Counter()
    element = ''
    count = ''
    
    for char in formula:
        if char.isupper():
            if element:
                elements[element] += int(count) if count else 1
            element = char
            count = ''
        elif char.islower():
            element += char
        elif char.isdigit():
            count += char
            
    if element:
        elements[element] += int(count) if count else 1
    
    return elements

def calculate_molecular_weight(formula):
    elements = parse_formula(formula)
    weight = sum(atomic_weights[elem] * count for elem, count in elements.items())
    return weight


# Example usage
#formula = "C10H8BaO6"  # Water Glucose
molecular_weight = calculate_molecular_weight(formula1)
print(f" Molecular weight of {formula1} is {molecular_weight:.2f} g/mol or Dalton")

if molecular_weight < 5501:
    print (' which is more effective due to better absorption and bioavailability\n')
else :
    print ("Molecular weight higher than 150,000 dalton are not suitable for Protein-based Therapeutics drug\n")

print ("Note: there is no strict cutoff for the acceptable molecular weight of proteins in drug discovery\n")
   

input ('Enter to exit')
