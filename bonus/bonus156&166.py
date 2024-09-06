import FreeSimpleGUI as fsg
import zipcreator

label_compress_text = fsg.Text("Select files to compress ")
compress_filepaths_input = fsg.InputText()
compress_choose_button = fsg.FilesBrowse("Choose", key="files")

label_dest_text = fsg.Text("Select destination folder ")
dest_folderpath_input = fsg.InputText()
dest_choose_button = fsg.FolderBrowse("Choose", key="folder")

compress_button = fsg.Button("Compress")
output_text = fsg.Text(key="result_status", text_color="blue")

window = fsg.Window("File Zipper", layout=[[label_compress_text, compress_filepaths_input, compress_choose_button],
                                           [label_dest_text, dest_folderpath_input, dest_choose_button],
                                           [compress_button, output_text]])
while True:
    event, values = window.read()
    print(event, values, sep="\n")
    files = values["files"].split(";")
    folder = values["folder"]
    zipcreator.make_archive(files, folder)
    window["result_status"].update(value="Compressed files successfully.")

window.close()
