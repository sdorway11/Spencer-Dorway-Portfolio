import wx, os.path, time, shutil, sqlite3
from datetime import datetime, timedelta

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, \
            title=title, size=(800,450))
        self.Center()

        self.panel = wx.Panel(self)

        self.conn = sqlite3.connect('lastFileCheck.db')
        #self.deleteTable()
        self.createTable()
        self.showLastTimestamp()

        
        # Create the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        self.CreateStatusBar()

        # Create static boxes for Path input
        wx.StaticBox(self.panel, label='Choose Directories', \
                     pos=(20,40), size=(380,190))
        wx.StaticBox(self.panel, label='Commit Transfer', pos =(20,240), \
                     size=(380,100))
        
        font = wx.Font(15, wx.DECORATIVE,
                       wx.NORMAL, wx.FONTWEIGHT_BOLD, False)
        
        wx.StaticText(self.panel, label = "Move From", pos=(30,70))
        wx.StaticText(self.panel, label = "Move To",pos =(30,150))
        text = wx.StaticText(self.panel, label = "Files to move in directory",
                      pos =(470,50))
        text.SetFont(font)
        

        self.moveFrom = wx.TextCtrl(self.panel, size=(250, -1), pos =(130,102))
        self.moveTo = wx.TextCtrl(self.panel, size=(250, -1), pos = (130, 182))

        # Create Buttons
        ChooseBtn = wx.Button(self.panel, label="Browse...", pos=(30,100))
        ChooseBtn2 = wx.Button(self.panel, label="Browse...", pos=(30,180))
        TransferBtn = wx.Button(self.panel, label="Move Files", pos=(260,262),
                             size=(120,60))
        TransferBtn2 = wx.Button(self.panel, label="See Files", pos=(130,262),
                             size=(120,60))


        # Create Display box
        self.listCtrl = wx.ListCtrl(self.panel, size =(275,260), pos =(450, 80), \
                               style = wx.LC_REPORT |wx.BORDER_SUNKEN)
        self.listCtrl.InsertColumn(0, "Files from the last 24 hours:")
        self.listCtrl.SetColumnWidth(col=0,width=275)

        # Bind Buttons
        ChooseBtn.Bind(wx.EVT_BUTTON,lambda event: self.openFile(self.moveFrom))
        ChooseBtn2.Bind(wx.EVT_BUTTON, lambda event: self.openFile(self.moveTo))
        TransferBtn2.Bind(wx.EVT_BUTTON, self.insertTimestamp)
        TransferBtn2.Bind(wx.EVT_BUTTON, self.pathToFiles)
        TransferBtn.Bind(wx.EVT_BUTTON, self.moveFiles)

        # Show Last Date
        


        
        
        
        
        
    def openFile(self,out):
        openD = wx.DirDialog(self, "Choose a directory:",style=wx.DD_DEFAULT_STYLE |
                               wx.DD_NEW_DIR_BUTTON)
        if openD.ShowModal() == wx.ID_OK:
            out.SetValue(openD.GetPath())

        openD.Destroy()

    def pathToFiles(self, event):
        try:
            self.src = self.moveFrom.GetValue()
            
            listOfFiles = os.listdir(self.src)

            hoy = datetime.now()
            ayer = hoy + timedelta(hours = -24)
            day = hoy - ayer

            self.listCtrl.DeleteAllItems()
            lastSaved = self.readLastTimestamp()
            deltaTimeLastSaved = lastSaved - hoy

            if deltaTimeLastSaved < day:
            
                for f in listOfFiles:
                    Fpath = self.src + "\\" + f
                    modDate = datetime.fromtimestamp((os.path.getmtime(Fpath)))
                    modDif = hoy - modDate
                    if modDif < day:
                        self.listCtrl.Append([f])
                    
                count = self.listCtrl.GetItemCount()
                filesFound = wx.StaticText(self.panel, label = "...File(s) found..."
                                       ,pos =(450,348))
                filesFound.Destroy()
                time.sleep(.5)
                self.filesFound = wx.StaticText(self.panel, label = "{} File(s) found...".format(count)
                                       ,pos =(450,348))
            else:
                for f in listOfFiles:
                    Fpath = self.src + "\\" + f
                    modDate = datetime.fromtimestamp((os.path.getmtime(Fpath)))
                    modDif = hoy - modDate
                    if modDif < deltaTimeLastSaved:
                        self.listCtrl.Append([f])
                    
                count = self.listCtrl.GetItemCount()
                self.filesFound.Destroy()
                time.sleep(.5)
                self.filesFound = wx.StaticText(self.panel, label = "{} File(s) found...".format(count)
                                       ,pos =(450,348))

            
        except:
            pathError = wx.MessageDialog(frame, caption = "Error",
                                      message = "Folder selection invalid"
                                       ,style = wx.OK)
            pathError.ShowModal()


    def moveFiles(self,event):
        
        try:    
            self.dst = self.moveTo.GetValue()
            if not os.path.exists(self.dst):
                pathError = wx.MessageDialog(frame, caption = "Error",
                                      message = "Folder selection invalid"
                                       ,style = wx.OK)
                pathError.ShowModal()
                return
            
            count = self.listCtrl.GetItemCount()
            if count == 0:
                pathError = wx.MessageDialog(frame, caption = "Error",
                                      message = "There are no files to move"
                                       ,style = wx.OK)
                pathError.ShowModal()
                return
            
            for row in range(count):
                item = self.listCtrl.GetItem(row,0)
                f = item.GetText()
                Fpath = self.src + "\\" + f
                shutil.move(Fpath, self.dst)
        
            filesMoved = wx.MessageDialog(frame, caption = "Success!",
                              message = "{} Files moved...".format(count)
                            ,style = wx.OK)

            filesMoved.ShowModal()
            self.insertTimestamp()
        except:   
            pathError = wx.MessageDialog(frame, caption = "Error",
                                      message = "The Files have already been moved"
                                       ,style = wx.OK)
            pathError.ShowModal()

    def createTable(self):
        self.conn.execute("CREATE TABLE if not exists \
                last_file_check(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                timeStamp DATE);")
        cursor = self.conn.execute("SELECT * from last_file_check;")
        rows = cursor.fetchall()
        hoy = datetime.now()
        ayer = (hoy + timedelta(hours = -24)).strftime("%Y-%m-%d %H:%M:%S")
        
        if len(rows) < 1:
            self.conn.execute("INSERT INTO last_file_check(timeStamp) VALUES(?);",(ayer,))
            
        self.conn.commit()

    def insertTimestamp(self):
        Ct = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.conn.execute("INSERT INTO last_file_check(timeStamp) VALUES(?);",(Ct,))

        self.showLastTimestamp()
        self.conn.commit()
        
    def readLastTimestamp(self):
        cursor = self.conn.execute("SELECT * from last_file_check;")
        rows = cursor.fetchall()
        date_unicode = str(rows[-1][1])
        date = datetime.strptime(date_unicode, '%Y-%m-%d %H:%M:%S')
        return  date

    def showLastTimestamp(self):
        cursor = self.conn.execute("SELECT * from last_file_check;")
        rows = cursor.fetchall()
        
        if len(rows) == 1:
            self.filesChecked = wx.StaticText(self.panel, label =
                                            "Files have not been checked"
                                            ,pos =(175,20))
        else:
            self.filesChecked = wx.StaticText(self.panel, label =
                                            "Files last moved: {}"
                                            .format(rows[-1][1]),pos =(175,20))


    def deleteTable(self):
        self.conn.execute("DROP TABLE if exists last_file_check;")
        self.conn.commit()
        

    def exitProgram(self, event):
        self.Destroy()
        


app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
