import subprocess

def main():
    print(" ")
    print("\t\tChoose an desire option\n")
    print ("********************************************************************")
    print("1: Calculate the molecular weight and molecular formula from")
    print("\ta sequence of standard amino acids.\n")
    print("2: Calculate the molecular mass from the molecular formula")
    print("\tof non-protien components.\n")
    print("3: Estimate the number of amino acids in proteins.\n")
    print("4: Sum the molecular weight of proteins and the non-protein components.\n")
    print ("5: Single code Amino acid image.\n " )
    print("6: Exit")
    print ("********************************************************************")

    choice = input("\t\tEnter your choice: ")

    if choice == '1':
        run_script('mol1.py')
    elif choice == '2':
        run_script('mol2.py')
    elif choice == '3':
        run_script('mol2.py')
    elif choice == '4':
        run_script('mol4.py')
    elif choice == '5':
        run_script('openimage.py')
    elif choice == '6':
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")

if __name__ == '__main__':
    main()
