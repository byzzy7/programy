'''
author: Lukáš Bystroň
email: lbystron@gmail.com
'''

from PyPDF2 import PdfReader, PdfWriter
import datetime
import re

with open("nazev.pdf", "rb") as file:
    reader = PdfReader(file)
    # Získání aktuálního data ve formátu MM.YYYY
    datum = datetime.datetime.today().strftime('%m.%Y')

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        nadpis = text[80:96] if text and len(text) >= 96 else f'strana_{i + 1}'
        nadpis = re.sub(r'[<>:"/\\|?*]', '', nadpis)  # nahrazení zakázaných znaků
        filename = f'{nadpis}- {datum}.pdf'
        writer = PdfWriter()
        writer.add_page(page)
        with open(filename, 'wb') as output_file:
            writer.write(output_file)
            print(f'Vytvořen soubor: {filename}')
