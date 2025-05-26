'''
______  ______  ______
| ___ \ |  _  \ |  ___|
| |_/ / | | | | | |_
|  __/  | | | | |  _|
| |     | |/ /  | |
\_|     |___/   \_|

author: Lukáš Bystroň
email: lbystron@gmail.com
'''

import PyPDF2

with open("nazev.pdf", "rb") as pdf_file:
    pdf = PyPDF2.PdfReader(pdf_file)

    for i in range(len(pdf.pages)):
           # Vytvoření nového PDF souboru pro každou stránku
           with open(f"page_{i+1}.pdf", "wb") as output_file:
               writer = PyPDF2.PdfWriter()
               writer.add_page(pdf.pages[i])  # Přidání stránky do nového souboru
               writer.write(output_file)