from selectfiledir.filepicker import GetFile

class FilePicker():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2007ファイル", "*.xlsx"),("Excel2007ファイル", "*.xls")]
        self.picker = GetFile(self.__def_dir,self.__ftype)
        self.file_list = self.picker.get_files()

    def get_file_list(self):
        if self.file_list is False:
            quit()
        else:
            return self.file_list