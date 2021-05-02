import configparser
from pathlib import Path


def makeConfigFile():
    configRoot = Path('settings.ini')

    # If configFile doesn't exist, create it.
    if not configRoot.is_file():
        config = configparser.ConfigParser()

        config['Subfolders'] = {'folder1': 'Imagenes', 'folder2': 'Videos', 'folder3': 'Documentos', 'folder4': 'Otros'}

        config['extensions'] = {'extensionsFolder1': ".png , .jpg , .jpeg",
                                'extensionsFolder2': ".doc , .pdf , .docx",
                                'extensionsFolder3': ".mp4 , .mov",
                                'extensionsFolder4': ".css , .html"
                                }

        config['Folder1'] = {'orderByYear': 'True', 'orderByMonth': 'True'}
        config['Folder2'] = {'orderByYear': 'True', 'orderByMonth': 'True'}
        config['Folder3'] = {'orderByYear': 'True', 'orderByMonth': 'True'}
        config['Folder4'] = {'orderByYear': 'True', 'orderByMonth': 'True'}

        with open('settings.ini', 'w') as configfile:
            config.write(configfile)


def changeValues(section, row, value):
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config.set(section, row, value)
    with open("settings.ini", "w") as f:
        config.write(f)


def getConfigValue(section, row):
    config = configparser.ConfigParser()
    config.read('settings.ini')
    value = config.get(section, row)

    return str(value)


def getSubfolders():
    subFolders = []
    for i in range(1, 5):
        subFolders.append(getConfigValue("Subfolders", "folder" + str(i)))
    return subFolders


def getExtensions(section, row):
    extensions = getConfigValue(section, row)
    extensions = extensions.split(" , ")
    return extensions
