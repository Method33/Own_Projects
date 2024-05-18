import Augmentor
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Lista nazw folderów (klas)
nazwy_folderow = ["Buk", "Dab", "Jesion", "Jodla", "Modrzew", "Olcha", "Sosna", "Swierk"]

# Utwórz obiekt Pipeline dla każdego folderu i dodaj operacje.
pipelines = [Augmentor.Pipeline(nazwa_folderu) for nazwa_folderu in nazwy_folderow]

for p in pipelines:
    p.resize(probability=1, width=224, height=224)
    p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
    p.flip_left_right(probability=0.5)
    p.flip_top_bottom(probability=0.5)

# Wygeneruj próbki dla każdego pipeline.
for p in pipelines:
    p.sample(300)

# Ścieżka do folderu z wygenerowanymi obrazami.
output_folder = "C:/Users/przem/PycharmProjects/WoodRecog"


# Utworzenie instancji ImageDataGenerator.
datagen = ImageDataGenerator(
    rescale=1./255,  # Przeskalowanie obrazów do wartości od 0 do 1
)

# Ładowanie obrazów z dysku.
image_data = datagen.flow_from_directory(
    output_folder,
    target_size=(224, 224),  # Wymiary obrazów po przeskalowaniu
    color_mode='rgb',  # Kolor obrazów
    class_mode='categorical',  # Rodzaj klasyfikacji - tutaj wieloklasowa
    batch_size=32,  # Rozmiar batcha
)
