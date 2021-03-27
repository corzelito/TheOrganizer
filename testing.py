# print(getConfigValue("Subfolders", "folder2"))


# getSubfolders()
from Config.Config import getExtensions, makeConfigFile

makeConfigFile()

print(getExtensions("extensions", "extensionsfolder3"))
