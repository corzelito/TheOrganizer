import calendar
import datetime
import locale
import os
import time
from pathlib import Path


def makefolders(path, subfolders):
    # path C:\Users\Adri\Desktop\pruebasFicherosExtraidos
    os.makedirs(path, exist_ok=True)
    for i in subfolders:
        os.makedirs(path + "/" + i, exist_ok=True)


def deleteAllFolders(path):
    directory = Path(path)
    for item in directory.iterdir():
        if item.is_dir():
            deleteAllFolders(item)
        else:
            item.unlink()
    directory.rmdir()


def recorrerFichero(path, organizedFolderPath, subfolders):
    directory = Path(path)
    for item in directory.iterdir():
        if item.is_dir():
            # print(str(item) + " dir")
            recorrerFichero(item, organizedFolderPath, subfolders)
        else:
            # print(str(item) + " fichero")

            organizeFileByExtension(item, organizedFolderPath, subfolders)


def organizeFileByExtension(item, organizedFolderPath, subfolders):
    images = [".png", ".jpg"]
    documents = [".doc", ".pdf", ".docx"]
    videos = [".mp4", ".mov"]

    extension = str(os.path.splitext(item)[1]).lower()

    if extension in images:
        print("Last modified: %s" % time.ctime(os.path.getmtime(item)))
        organizarPorMesYAnio(organizedFolderPath, item, subfolders[0])
    elif extension in videos:
        Path(item).rename(organizedFolderPath + "/" + subfolders[1] + "/" + item.name)
    elif extension in documents:
        Path(item).rename(organizedFolderPath + "/" + subfolders[2] + "/" + item.name)
    else:
        Path(item).rename(organizedFolderPath + "/" + subfolders[3] + "/" + item.name)



def organizarPorMesYAnio(organizedFolderPath, item, imgSubFolder):
    print(item)
    year = datetime.date.fromtimestamp(os.path.getmtime(item)).year
    yearFolder = organizedFolderPath + "/" + imgSubFolder + "/" + str(year)

    creationMonthName = calendar.month_name[datetime.date.fromtimestamp(os.path.getmtime(item)).month].capitalize()
    monthFolder = yearFolder + "/" + creationMonthName

    copyFilePath = monthFolder + "/" + item.name

    os.makedirs(yearFolder, exist_ok=True)
    os.makedirs(monthFolder, exist_ok=True)
    Path(item).rename(copyFilePath)



if __name__ == '__main__':
    # path = input("Dime la ruta")
    locale.setlocale(locale.LC_ALL, 'ES')
    path = "C:\\Users\\Adri\\Desktop\\pruebas"
    subfolders = ['Imagenes', 'Videos', 'Documentos', 'Otros']
    organizedFolderName = "FicherosExtraidos"
    organizedFolderPath = os.path.abspath(path + organizedFolderName)
    print(organizedFolderPath)
    print("RUTA DE ENTRADA ---> " + str(path))

    # if os.path.exists(organizedFolderPath):
    #     deleteAllFolders(organizedFolderPath)

    makefolders(organizedFolderPath, subfolders)
    recorrerFichero(path, organizedFolderPath, subfolders)
