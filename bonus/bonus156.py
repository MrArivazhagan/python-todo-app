import FreeSimpleGUI as fsg

label_compress_text = fsg.Text("Select files to compress ")
compress_filepaths_input = fsg.InputText()
compress_choose_button = fsg.FilesBrowse("Choose")

label_dest_text = fsg.Text("Select destination folder ")
dest_folderpath_input = fsg.InputText()
dest_choose_button = fsg.FolderBrowse("Choose")

compress_button = fsg.Button("Compress")

window = fsg.Window("File Zipper", layout=[[label_compress_text, compress_filepaths_input, compress_choose_button],
                                           [label_dest_text, dest_folderpath_input, dest_choose_button],
                                           [compress_button]])
window.read()
window.close()