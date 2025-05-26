'''
 _         _ _          _            _
| |       | | |        | |          | |
| | ____ _| | | ___   _| | __ _  ___| | ____ _
| |/ / _` | | |/ / | | | |/ _` |/ __| |/ / _` |
|   < (_| | |   <| |_| | | (_| | (__|   < (_| |
|_|\_\__,_|_|_|\_\\__,_|_|\__,_|\___|_|\_\__,_|

author: Lukáš Bystroň
email: lbystron@gmail.com
'''

def scitani(prvni_cislo, druhe_cislo):
    """"sčítaní"""
    return prvni_cislo + druhe_cislo
            
def odcitani(prvni_cislo, druhe_cislo):
    """"Odčítaní"""
    return prvni_cislo - druhe_cislo
        
def nasobeni(prvni_cislo, druhe_cislo):
    """"násobení"""
    return prvni_cislo * druhe_cislo
        
def deleni(prvni_cislo, druhe_cislo):
    """"dělení"""
    return prvni_cislo / druhe_cislo

def matematicke_operace():
    operace={
        "+": scitani,
        "-": odcitani,
        "*": nasobeni,
        "/": deleni
    }
    return operace

def main():
    pokracovani = "ano"
    while pokracovani == "ano":
        num1 = float(input("Zadejte první číslo: "))
        for volba in matematicke_operace():
            print(volba)

        uzivate_symbol = input("Vyberte jednu z oprace výše: ")
        num2 = float(input("Zadejte druhe číslo: "))

        vypocet = matematicke_operace().get(uzivate_symbol)
        result = vypocet(num1, num2)

        print(f"{num1} {uzivate_symbol} {num2} = {result}")
        pokracovani = input(print("Chcete pokračovat ANO nebo znovu NE: "))
        if pokracovani == "ne":
            exit()

if __name__ == '__main__':
    main()