import selectfiledir.filepicker as picker
import os
import sys


def main():
    defdir = "DeskTop"
    ftype = [("Excelファイル", "*.xlsx")]
    dialog = picker.GetFile(defdir, ftype)
    files = dialog.get_files()


if __name__ == "__main__":
    main()
