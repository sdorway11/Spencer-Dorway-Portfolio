import os.path, time, shutil
from datetime import datetime, timedelta

src = "C:\Users\sdorw_000\Desktop\Folder A"
dst = "C:\Users\sdorw_000\Desktop\Folder B"

listOfFiles = os.listdir(src)

hoy = datetime.now()
ayer = hoy + timedelta(hours = -24)
day = hoy - ayer


for f in listOfFiles:
    Fpath = src + "\\" + f
    modDate = datetime.fromtimestamp((os.path.getmtime(Fpath)))
    modDif = hoy - modDate
    if modDif < day:
        shutil.move(Fpath, dst)
        print Fpath
        print "This is new"
        
