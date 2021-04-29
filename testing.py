from Files.Extensions import Extensions

list1 = ['.mp3', '.mp4', '.WOW']

list2 = ['.jpg', '.png', '.mp4', '.mov', '.mp3', '.doc']

# print(".jpg" in images)
#



# print( Extensions.images[1])


array = []
for i in Extensions.images:
    if i not in list1:
        array.append(i)
    print(array)