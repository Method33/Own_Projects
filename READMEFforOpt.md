# OCR Image to Text

This Python project uses OpenCV and PyTesseract to implement Optical Character Recognition (OCR) for reading text from images.

## Requirements

This project requires Python 3.6 or later, and the following Python libraries installed:

- OpenCV
- PyTesseract

You also need to have Tesseract OCR installed on your machine. You can install it from here: https://github.com/UB-Mannheim/tesseract/wiki

## Installation

1. Clone this repository to your machine.
2. Install required packages if you haven't done so already: OpenCV and PyTesseract. You can do this by running `pip install opencv-python pytesseract` in your console.
3. Install Tesseract OCR on your computer.

## Usage

1. Open the `main.py` script in your preferred IDE or text editor.
2. Set the `folder` variable to the path of the directory containing your images. The path should be formatted as follows: `'C:\\path_to_your_folder'`
3. Set the `sciezka_pliku_tekstowego` variable to the path where you want the text file to be saved: `'C:\\path_to_text_file'`
4. Set the path to the Tesseract executable in the line: `pytesseract.pytesseract.tesseract_cmd = 'C:\\path_to_tesseract\\tesseract.exe'`
5. Save the script and run it. It will find all the image files in the specified folder, select the most recently modified one, read the text from the image, and save it to the specified text file.

The image files should be in .jpg or .png format. The script might not work correctly with other file formats.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
