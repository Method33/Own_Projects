import os
import glob
import cv2
import pytesseract

# Ścieżka do tesseract OCR
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\przem\\PycharmProjects\\ocrAPI\\tesseract.exe'


def odczytaj_tekst_z_obrazu(sciezka_obrazu):
    obraz = cv2.imread(sciezka_obrazu)
    przetworzony_obraz = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    tekst = pytesseract.image_to_string(przetworzony_obraz)
    return tekst


def zapisz_tekst_do_pliku(tekst, sciezka_pliku):
    with open(sciezka_pliku, 'w', encoding='utf-8') as plik:
        plik.write(tekst)


folder = "C:\\Users\\przem\\PycharmProjects\\ocrAPI\\image"
sciezka_pliku_tekstowego = 'C:\\Users\\przem\\PycharmProjects\\ocrAPI\\ImageConverted\\ImageConverted'

# Znajdź wszystkie pliki obrazów w folderze
sciezki_obrazow = glob.glob(os.path.join(folder, '*.[PpJj][Nn][GgJj]*'))

# Sortuj pliki według daty modyfikacji w kolejności malejącej
sciezki_obrazow.sort(key=os.path.getmtime, reverse=True)

# Wybierz pierwszy obraz (najnowszy)
if len(sciezki_obrazow) > 0:
    sciezka_obrazu = sciezki_obrazow[0]
    tekst_z_obrazu = odczytaj_tekst_z_obrazu(sciezka_obrazu)
    zapisz_tekst_do_pliku(tekst_z_obrazu, sciezka_pliku_tekstowego)
    print('Tekst został zapisany do pliku:', sciezka_pliku_tekstowego)
else:
    print('Brak obrazów w folderze.')
