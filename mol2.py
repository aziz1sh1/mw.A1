from collections import Counter
print ("********************************************************************")
print ("The program is designed to calculate molecular mass")
print ("and apply Lipinski's rule to identify suitable candidates")
print ("\t toward drug discovery.")
print ("********************************************************************")
print ("Avoid entering symbols")
print ("\t Enter first capital lettar of each chemical symbol second letter normal\n")

# Atomic weights (g/mol)
atomic_weights = {

    'H': 1.01,    # Hydrogen
    'He': 4.00,   # Helium
    'Li': 6.94,   # Lithium
    'Be': 9.01,   # Beryllium
    'B': 10.81,   # Boron
    'C': 12.01,   # Carbon
    'N': 14.01,   # Nitrogen
    'O': 16.00,   # Oxygen
    'F': 19.00,   # Fluorine
    'Ne': 20.18,  # Neon
    'Na': 22.99,  # Sodium
    'Mg': 24.31,  # Magnesium
    'Al': 26.98,  # Aluminum
    'Si': 28.09,  # Silicon
    'P': 30.97,   # Phosphorus
    'S': 32.07,   # Sulfur
    'Cl': 35.45,  # Chlorine
    'Ar': 39.95,  # Argon
    'K': 39.10,   # Potassium
    'Ca': 40.08,  # Calcium
    'Sc': 44.96,  # Scandium
    'Ti': 47.87,  # Titanium
    'V': 50.94,   # Vanadium
    'Cr': 51.99,  # Chromium
    'Mn': 54.94,  # Manganese
    'Fe': 55.85,  # Iron
    'Co': 58.93,  # Cobalt
    'Ni': 58.69,  # Nickel
    'Cu': 63.55,  # Copper
    'Zn': 65.38,  # Zinc
    'Ga': 69.72,  # Gallium
    'Ge': 72.64,  # Germanium
    'As': 74.92,  # Arsenic
    'Se': 78.96,  # Selenium
    'Br': 79.90,  # Bromine
    'Kr': 83.80,  # Krypton
    'Rb': 85.47,  # Rubidium
    'Sr': 87.62,  # Strontium
    'Y': 88.91,   # Yttrium
    'Zr': 91.22,  # Zirconium
    'Nb': 92.91,  # Niobium
    'Mo': 95.94,  # Molybdenum
    'Tc': 98.00,  # Technetium
    'Ru': 101.07, # Ruthenium
    'Rh': 102.91, # Rhodium
    'Pd': 106.42, # Palladium
    'Ag': 107.87, # Silver
    'Cd': 112.41, # Cadmium
    'In': 114.82, # Indium
    'Sn': 118.71, # Tin
    'Sb': 121.76, # Antimony
    'Te': 127.60, # Tellurium
    'I': 126.90,  # Iodine
    'Xe': 131.29, # Xenon
    'Cs': 132.91, # Cesium
    'Ba': 137.33, # Barium
    'La': 138.91, # Lanthanum
    'Ce': 140.12, # Cerium
    'Pr': 140.91, # Praseodymium
    'Nd': 144.24, # Neodymium
    'Pm': 145.00, # Promethium
    'Sm': 150.36, # Samarium
    'Eu': 151.96, # Europium
    'Gd': 157.25, # Gadolinium
    'Tb': 158.93, # Terbium
    'Dy': 162.50, # Dysprosium
    'Ho': 164.93, # Holmium
    'Er': 167.26, # Erbium
    'Tm': 168.93, # Thulium
    'Yb': 173.04, # Ytterbium
    'Lu': 174.97, # Lutetium
    'Hf': 178.49, # Hafnium
    'Ta': 180.95, # Tantalum
    'W': 183.84,  # Tungsten
    'Re': 186.21, # Rhenium
    'Os': 190.23, # Osmium
    'Ir': 192.22, # Iridium
    'Pt': 195.08, # Platinum
    'Au': 196.97, # Gold
    'Hg': 200.59, # Mercury
    'Tl': 204.38, # Thallium
    'Pb': 207.2,  # Lead
    'Bi': 208.98, # Bismuth
    'Po': 209.00, # Polonium
    'At': 210.00, # Astatine
    'Rn': 222.00, # Radon
    'Fr': 223.00, # Francium
    'Ra': 226.03, # Radium
    'Ac': 227.00, # Actinium
    'Th': 232.04, # Thorium
    'Pa': 231.04, # Protactinium
    'U': 238.03,  # Uranium
    'Np': 237.00, # Neptunium
    'Pu': 244.00, # Plutonium
    'Am': 243.00, # Americium
    'Cm': 247.00, # Curium
    'Bk': 247.00, # Berkelium
    'Cf': 251.00, # Californium
    'Es': 252.00, # Einsteinium
    'Fm': 257.00, # Fermium
    'Md': 258.00, # Mendelevium
    'No': 259.00, # Nobelium
    'Lr': 262.00, # Lawrencium
    'Rf': 267.00, # Rutherfordium
    'Db': 268.00, # Dubnium
    'Sg': 271.00, # Seaborgium
    'Bh': 270.00, # Bohrium
    'Hs': 277.00, # Hassium
    'Mt': 278.00, # Meitnerium
    'Ds': 281.00, # Darmstadtium
    'Rg': 282.00, # Roentgenium
    'Cn': 285.00, # Copernicium
    'Nh': 286.00, # Nihonium
    'Fl': 289.00, # Flerovium
    'Mc': 289.00, # Moscovium
    'Lv': 292.00, # Livermorium
    'Ts': 294.00, # Tennessine
    'Og': 294.00  # Oganesson   
    
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
formula = input ("Enter Molcular formula ")
molecular_weight = calculate_molecular_weight(formula)
print(f" Molecular weight of {formula} is {molecular_weight:.2f} g/mol or Dalton")
if molecular_weight < 501:
    print ('Small molecular weight is best for drug')
else :
    print ("Higher molcular weight are not suitable for drug")
print ("Note there is no strict cutoff for the acceptable molecular weight of proteins in drug discovery")

input("Enter to exit")
