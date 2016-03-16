import shutil, os

src = "C:\Users\sdorw_000\Desktop\Folder A"
dst = "C:\Users\sdorw_000\Desktop\Folder B"

listOfFiles = os.listdir(src)

for f in listOfFiles:
    path = src + "\\" + f
    shutil.move(path, dst)
    print(path)
