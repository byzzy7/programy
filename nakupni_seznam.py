'''
jednoduchy nakupní seznam
'''

import csv

def volba():
    '''
    vyběr možnosti
    '''
    print("   NÁKUPNÍ SEZNAM\n"
          "1 - přidat položku\n"
          "2 - odebrat položku\n"
          "3 - zobrazit seznam\n"
          "4 - smazat seznam\n"
          "5 - uložit do csv souboru\n"
          "6 - ukončit program")
    return

def uzivatel():
    '''
    Vstup uživatele
    '''
    try:
        vyber = int(input("Volba: "))
        return vyber
    except ValueError:
        print("Pouze čísla!")

def main():
    pokracovani = "ano"
    while pokracovani == "ano":
        xx = uzivatel()
        if xx == 1:
            polozka = input("Položka: ")
            seznam.append(polozka)
        elif xx == 2:
            polozka = input("Položka: ")
            seznam.remove(polozka)
        elif xx == 3:
            print(seznam)
        elif xx == 4:
            seznam.clear()
            print(seznam)
        elif xx == 5:
            ulozeni_csv(seznam)
        else:
            pokracovani = "ne"
    return

def ulozeni_csv(seznam):
    '''
    uložení seznam do csv souboru
    '''
    with open("seznam.csv", "w", encoding="utf-8", newline="") as file:
        w = csv.writer(file)
        for polozka in seznam:
            w.writerow([polozka])
    print("Seznam byl uložen.")

seznam = [] # Paměť nákupního seznamu

if __name__ == '__main__':
    volba()
    main()

