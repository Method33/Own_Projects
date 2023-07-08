import sys
from tkinter import *
from tkinter import filedialog
from docx2pdf import convert

root = Tk()
root.title('Docx to PDF Converter')

def choose_input_file():
    input_file_path = filedialog.askopenfilename(
        title='Select input file',
        filetypes=[('Word Document', '*.docx')]
    )
    input_file_path_entry.delete(0, END)
    input_file_path_entry.insert(0, input_file_path)


def choose_output_file():
    output_file_path = filedialog.askdirectory(
        title='Select output folder'
    )
    output_file_path_entry.delete(0, END)
    output_file_path_entry.insert(0, output_file_path)



def convert_file():
    input_file_path = input_file_path_entry.get()
    output_file_path = output_file_path_entry.get() + "/output.pdf"  # add file name to output path

    sys.stdout = output_text_widget
    output_text_widget.insert(END, 'Converting file...\n')
    output_text_widget.insert(END, 'Input file path: ' + input_file_path + '\n')
    output_text_widget.insert(END, 'Output file path: ' + output_file_path_entry.get() + '\n')
    convert(input_file_path, output_file_path)
    output_text_widget.insert(END, 'File conversion completed!\n')



input_file_path_label = Label(root, text='Input file path:')
input_file_path_entry = Entry(root, width=50)
input_file_path_button = Button(root, text='Select file', command=choose_input_file)

output_file_path_label = Label(root, text='Output file path:')
output_file_path_entry = Entry(root, width=50)
output_file_path_button = Button(root, text='Select file', command=choose_output_file)

convert_button = Button(root, text='Convert', command=convert_file)
output_text_widget = Text(root, width=60, height=20)

input_file_path_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
input_file_path_entry.grid(row=0, column=1, padx=5, pady=5)
input_file_path_button.grid(row=0, column=2, padx=5, pady=5)

output_file_path_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
output_file_path_entry.grid(row=1, column=1, padx=5, pady=5)
output_file_path_button.grid(row=1, column=2, padx=5, pady=5)

convert_button.grid(row=2, column=1, padx=5, pady=5)
output_text_widget.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
