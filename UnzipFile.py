import os
import zipfile
from PIL import Image

# Funkcja konwertująca zdjęcia do mniejszego rozmiaru
def process_images(folder_path, dest_folder, width, height):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')) and os.path.isfile(file_path):
            image = Image.open(file_path)
            image_copy = image.copy()
            image = image.convert('RGB')
            image_copy_resize = image_copy.resize((width, height))
            new_file_path = os.path.join(dest_folder, file_name)
            image_copy_resize.save(new_file_path, 'JPEG', quality=95, optimize=True)
            while os.path.getsize(new_file_path) > 200000:
                image_copy_resize.save(new_file_path, 'JPEG', quality=80, optimize=True)
        elif os.path.isdir(file_path):
            process_images(file_path, dest_folder, width, height)


# Ścieżki do folderów i plików
path = "images"
zip_file_path = "allzips"
destination_folder = "images"
converted_images_folder = "converted_images"

# Wymiary docelowe
width = 560
height = 900

if not os.path.exists(converted_images_folder):
    os.makedirs(converted_images_folder)

# Wypakowywanie plików zip
for zip_file_name in os.listdir(zip_file_path):
    if zip_file_name.endswith('.zip') or zip_file_name.endswith('.ZIP'):
        zip_file = os.path.join(zip_file_path, zip_file_name)
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)

# Przetwarzanie wypakowanych zdjęć
process_images(destination_folder, converted_images_folder, width, height)
