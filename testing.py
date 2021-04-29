from Config.Config import getConfigValue
from Files.Extensions import Extensions

list1 = ['.mp3', '.mp4', '.WOW']

list2 = ['.jpg', '.png', '.mp4', '.mov', '.mp3', '.doc']

# print(".jpg" in images)
#
extensions = getConfigValue("extensions", "extensionsfolder2")
haha = extensions.split(", ")

print(haha[0])