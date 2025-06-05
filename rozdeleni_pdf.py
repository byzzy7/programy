from PyPDF2 import PdfReader, PdfWriter
import datetime
import re

nazev_souboru = "pásky 04 (2).pdf"

try:
    with open(nazev_souboru, "rb") as file:
        reader = PdfReader(file)
        # Získání aktuálního data ve formátu MM.YYYY
        datum = datetime.datetime.today().strftime('%m.%Y')

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            # Nadpis stránky je extrahován z textu, pozice 74 až 96
            nadpis = text[74:96]
            nadpis = re.sub(r'[<>:"/\\|?*]', '', nadpis) # nahrazení zakázaných znaků
            nadpis = re.sub(r'[á]', 'a', nadpis)
            filename = f'{nadpis}.pdf'
            writer = PdfWriter()
            writer.add_page(page)
            with open(filename, 'wb') as output_file:
                writer.write(output_file)
                print(f'Vytvořen soubor: {filename}')
except FileNotFoundError:
    print(f"Soubor {nazev_souboru} nebyl nalezen.")
except Exception as e:
    print(f"Došlo k chybě: {e}")
