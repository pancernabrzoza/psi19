class FileManager:
    def __init__(self,file_name):
        self.file_name=file_name
    def read_file(self):
        uchwyt=open('plik.txt','r')
        dane=uchwyt.read()
        print(dane)
        uchwyt.close()
    def update_file(text_data):
        uchwyt=open('plik.txt','a+')
        uchwyt.writelines("\n")
        uchwyt.writelines(text_data)
        uchwyt.close()
FileManager.update_file("przyklad")