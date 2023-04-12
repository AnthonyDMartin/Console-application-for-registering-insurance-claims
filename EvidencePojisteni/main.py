from pojistenec import Pojistenec

pojistenec = Pojistenec


class Evidence:
    def __init__(self):
        self.evidence = []
        pass


evidence = [Pojistenec("David", "Jančík", 27, 123456788)]

while True:
    print()
    print("------------------------------")
    print("Evidence pojištěných")
    print("------------------------------")
    print()
    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    while True:
        try:
            volba = int(input(""))
            print()
            break
        except:
            print()
            print("Nevybrali jste si akci!")

    if volba == 1:
        while True:
            jmeno = input("Zadejte jméno pojištěného:\n")
            if jmeno.isalpha():
                break
            else:
                print("\nNeplatné zadání")
        while True:
            prijmeni = input("Zadejte příjmení:\n")
            if prijmeni.isalpha():
                break
            else:
                print("\nNeplatné zadání")
        while True:
            telefon = input("Zadejte telefonní číslo:\n")
            if telefon.isdigit():
                break
            else:
                print("\nNeplatné zadání")
        while True:
            vek = input("Zadejte věk:\n")
            if vek.isdigit():
                break
            else:
                print("\nNeplatné zadání")
        evidence.insert(0, Pojistenec(jmeno, prijmeni, vek, telefon))
        print()
        print("Data byla uložena. Pokračujte libovolnou klávesou...")
        input("")

    elif volba == 2:
        for pojistenec in evidence:
            print(pojistenec)
        print()
        print("Pokračujte libovolnou klávesou...")
        input("")

    elif volba == 3:
        while True:
            vyhledat_jmeno = input("Zadejte jméno pojištěného:\n")
            if vyhledat_jmeno.isalpha():
                break
            else:
                print("\nNeplatné zadání")
        while True:
            vyhledat_prijmeni = input("Zadejte příjmení:\n")
            if vyhledat_prijmeni.isalpha():
                break
            else:
                print("\nNeplatné zadání")
        for i in range(len(evidence)):
            if evidence[i].jmeno == vyhledat_jmeno.capitalize() and evidence[i].prijmeni == vyhledat_prijmeni.capitalize():
                print()
                print(f"{evidence[i].jmeno}\t{evidence[i].prijmeni}\t{evidence[i].vek}\t{evidence[i].telefon}")
                print()
                print("Pokračujte libovolnou klávesou...")
                input("")
            else:
                pass

    elif volba == 4:
        print("Konec")
        break

    else:
        print("Vybrali jste si špatnou akci")
