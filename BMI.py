'''
 ______   ____    ____  _____
|_   _ \ |_   \  /   _||_   _|
  | |_) |  |   \/   |    | |
  |  __'.  | |\  /| |    | |
 _| |__) |_| |_\/_| |_  _| |_
|_______/|_____||_____||_____|

author: Lukáš Bystroň
email: lbystron@gmail.com
'''

jmeno = input("Napiš své jméno: ")
vaha = int(input("Napiš svojí váhu v kg: "))
vyska = float(input("Napiš svojí výšku v metrech: "))
bmi = int(vaha / vyska **2)
kategorie=[
    "> 18.5", "Podvýživa",
    "18.5 - 25", "Zdravá váha",
    "25 - 30", "Mirná nadváha",
    "30 - 40", "Obezita",
    "40 <", "Těžká obezita"
]

if bmi < 18.5:
    print(jmeno, "tvé BMI je", bmi,", což spadá do kategorie ", kategorie[1])
elif bmi > 18.5 and bmi < 25:
    print(jmeno, "tvé BMI je", bmi,", což spadá do kategorie ", kategorie[3])
elif bmi > 25 and bmi < 30:
    print(jmeno, "tvé BMI je", bmi,", což spadá do kategorie ", kategorie[5])
elif bmi > 30 and bmi < 40:
    print(jmeno, "tvé BMI je", bmi,", což spadá do kategorie ", kategorie[7])
else:
    print(jmeno, "tvé BMI je", bmi,", což spadá do kategorie ", kategorie[9])