import zipfile
import pathlib

def make_archive(filepaths, dir_path):
    dest_path = pathlib.Path(dir_path, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(["D:/Soliton Technologies/Self paced learning/pythonProject/files/a.txt",
                  "D:/Soliton Technologies/Self paced learning/pythonProject/files/b.txt",
                  "D:/Soliton Technologies/Self paced learning/pythonProject/files/c.txt"],
                 "D:/Soliton Technologies/Self paced learning/pythonProject/files/repetitions")
