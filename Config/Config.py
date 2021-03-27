import configparser


def makeConfigFile():
    config = configparser.ConfigParser()

    config['Subfolders'] = {'folder1': 'Imagenes', 'folder2': 'Videos', 'folder3': 'Documentos', 'folder4': 'Otros'}

    config['extensions'] = {'extensionsFolder1': ".png , .jpg , .jpeg",
                            'extensionsFolder2': ".doc , .pdf , .docx",
                            'extensionsFolder3': ".mp4 , .mov"}

    config['OrderBy'] = {'orderByYear': 'True', 'orderByMonth': 'True'}

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