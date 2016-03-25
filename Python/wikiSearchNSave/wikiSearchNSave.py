from bs4 import BeautifulSoup
import urllib, sqlite3
from urllib import request
from tkinter import *
from tkinter import ttk, messagebox






class Window_:
    
    def __init__(self,master):
        master.title("Find and save a Wikipedia entry")
        master.resizable(False,False)
        master.configure(background = '#afc7cf')

        self.style = ttk.Style()
        self.style.configure("TFrame",background = '#afc7cf')
        self.style.configure("TLabel",background = '#afc7cf')
        self.style.configure('Header.TLabel', font = ('arial', 22, 'bold')
                             ,background = '#afc7cf')
        
        

        # Create the menu bar
        menuBar = Menu(master)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        editMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit",menu=editMenu)
        master.config(menu=menuBar)
        

        #Header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        
        ttk.Label(self.frame_header, text = 'Wikipedia Search-N-Save',
                  style="Header.TLabel").grid(row = 0, column = 1,ipadx=5,ipady=5)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        
        #Content Left
        self.frame_content = ttk.Frame(self.frame_content)
        self.frame_content.pack()
        

        self.searchText = ttk.Label(self.frame_content, text="Topic:"
                                    ,font = ('arial', 11, 'bold'),
                                    background = '#afc7cf'
                                    ).grid(row=1,column=1,sticky=W)

        self.entryTitle = ttk.Entry(self.frame_content, width=26,background = '#afc7cf')
        
        self.searchBtn = Button(self.frame_content, text="Search")
        
        self.savedTopics = ttk.Label(self.frame_content, text="Saved Topics"
                                     ,font=('arial', 13, 'bold'),background = '#afc7cf'
                                     ).grid(row=2,column=2)
        self.listBox = Listbox(self.frame_content, width = 67,height=20,
                               selectmode=SINGLE)
        self.loadBtn = Button(self.frame_content, text="Load Topic")
        self.titleEntry = ttk.Entry(self.frame_content, width=42)
        self.textBody = Text(self.frame_content, width = 40,height=24)
        self.saveBtn = Button(self.frame_content, text="Save Topic")
        self.deleteBtn = Button(self.frame_content, text="Delete Topic")

        #set up scrollbars
        scrollbar = Scrollbar(self.frame_content)
        scrollbar.grid(row=3,column=9,rowspan=5,sticky=NSEW)

        scrollbar2 = Scrollbar(self.frame_content)
        scrollbar2.grid(row=3,column=3,rowspan=3,sticky=NSEW)



        self.listBox.grid(row=3,column=1,columnspan=3,rowspan=3,sticky=N)
        self.listBox.config(yscrollcommand=scrollbar2.set)
        scrollbar2.config(command=self.listBox.yview)
        
        self.searchBtn.grid(row=1, column=3,sticky=NSEW)
        self.searchBtn.config(font=("arial",9,"bold"))
        self.searchBtn.config(command=self.wikiSearch)
        
        self.saveBtn.grid(row=7,column=1,sticky=NSEW)
        self.saveBtn.config(font=("arial",13,"bold"))
        self.saveBtn.config(command=self.saveWiki)

        self.deleteBtn.grid(row=7,column=3,sticky=NSEW)
        self.deleteBtn.config(font=("arial",13,"bold"))
        self.deleteBtn.config(command=self.deleteSavedEntry)
        
        self.loadBtn.grid(row=7,column=2,sticky=NSEW)
        self.loadBtn.config(font=("Arial",13,"bold"))
        self.loadBtn.config(command=self.loadSavedEntry)

        self.titleEntry.grid(row=1,column=6,columnspan=4)
        
        
        self.textBody.grid(row=3,column=6,columnspan=3,rowspan=5,sticky=N)
        self.textBody.config(wrap=WORD,yscrollcommand= scrollbar.set)
        scrollbar.config(command=self.textBody.yview)

        self.entryTitle.grid(row=1,column=1,columnspan=2,sticky=E)
        self.entryTitle.config(font=("arial",11,"bold"))

        self.titleEntry.config(font=("arial",11,"bold"))


        #spacers
        ttk.Label(self.frame_content, text="").grid(row=0,column=0,ipadx=5)
        ttk.Label(self.frame_content, text="").grid(row=0,column=1,ipadx=5)
        ttk.Label(self.frame_content, text="").grid(row=0,column=4,ipadx=5)
        ttk.Label(self.frame_content, text="").grid(row=8,column=0,columnspan=8)
        ttk.Label(self.frame_content, text="").grid(row=0,column=10,ipadx=5)
        ttk.Label(self.frame_content, text="").grid(row=2,column=6)
        ttk.Label(self.frame_content, text="").grid(row=6,column=1,columnspan=3)
        
        self.conn = sqlite3.connect("savedWikis.db")
        self.createTable()

    def searchWiki(self):
        pass

    def fillListbox(self):
        duplicate=self.conn.execute("SELECT* FROM saved_wikis WHERE rowid NOT IN\
                          (SELECT MAX(rowid) FROM saved_wikis GROUP BY title);")
        numDuplicates = len(duplicate.fetchall())
        

        if numDuplicates >0:
            noSite = messagebox.showwarning("Error!","Topic already saved")
            
            self.conn.execute("DELETE FROM saved_wikis WHERE rowid NOT IN\
                          (SELECT MAX(rowid) FROM saved_wikis GROUP BY title);")
        
        cursor = self.conn.execute("SELECT * from saved_wikis;")
        rows = cursor.fetchall()
        count=0
        for row in rows:
            self.listBox.insert(count,row[1])
            count +=1

    def saveWiki(self):
        
        Title = self.titleEntry.get()
        Body = self.textBody.get("1.0",END)
        self.conn.execute("INSERT INTO saved_wikis(title, bodyText) VALUES(?,?);",(Title,Body))
        self.listBox.delete(0,END)
        self.fillListbox()
        self.conn.commit()
        
            
        

    def createTable(self):
        self.conn.execute("CREATE TABLE if not exists \
                saved_wikis(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                title STRING,bodyText STRING);")
        cursor = self.conn.execute("SELECT * from saved_wikis;")
        rows = cursor.fetchall()
        firstTitle = "Select Title"
        firstBody = "The information will display here"
        
        if len(rows) < 1:
            self.conn.execute("INSERT INTO saved_wikis(title, bodyText) VALUES(?,?);",(firstTitle,firstBody))

        self.fillListbox()
        self.conn.commit()

    def deleteTable(self):
        self.conn.execute("DROP TABLE if exists saved_wikis;")
        self.conn.commit()


    def wikiSearch(self):
        count=0
        searched = self.entryTitle.get()
        
        searchItem = searched.replace(" ", "_")
        progress = "...Searching... " +str(int((count/len(searchItem))*100))+ "% complete..."
        print(progress)
        
        
        
        
        while len(searchItem) > count:    
            try:
                url = "https://en.wikipedia.org/wiki/"+searchItem[count:]
                file = urllib.request.urlopen(url)
                break
            except urllib.error.HTTPError :
                count+=1
                progress = "...Searching... " +str(int((count/len(searchItem))*100))+ "% complete..."
                print(progress)
            except urllib.error.URLError:
                noSite = messagebox.showwarning("Error!","Your are not connected to the internet")
                return
            
                
        if len(searchItem[count:]) > 2:
            count = len(searchItem) - 1
            progress = "...Searching... " +str(int((count/len(searchItem))*100))+ "% complete..."
            print(progress)
            soup = BeautifulSoup(file.read(), "html.parser")

            title = soup.find("h1",{"id":"firstHeading"})
            titleText = title.getText()
            self.titleEntry.delete(0,END)
            self.textBody.delete("1.0",END)
            

            bodyContent = soup.find("div",{"id":"mw-content-text"})
            paragraph = bodyContent.find_all("p")
            text = bodyContent.getText()
            bodyInfo = "   "
            try:
                for i in range(3):
                    bodyInfo += paragraph[i].getText()
                bodyInfo += "\n\nFind out more on the site: " + url
                self.textBody.insert("1.0",bodyInfo)
                self.titleEntry.insert(0,titleText)
                print("Complete!")
            except:
                noSite = messagebox.showwarning("Error!","Missing information on " +searched)

            
            
        else:
            noSite = messagebox.showwarning("Error!","No wiki found on " +searched)
       

    def loadSavedEntry(self):
        items = self.listBox.curselection()
        for item in items:
            cursor = self.conn.execute("SELECT * from saved_wikis;")
            rows = cursor.fetchall()
            self.titleEntry.delete(0,END)
            self.textBody.delete('1.0',END)
            self.titleEntry.insert(0,(rows[item][1]))
            self.textBody.insert('1.0',(rows[item][2]))

    def deleteSavedEntry(self):

        item = (self.listBox.curselection())[0]
        Name=self.listBox.get(item)
        

        if messagebox.askyesno("Delete","Are you sure you want to delete the entry " +Name+"?"):
            
            Title = self.titleEntry.get()
            Body = self.textBody.get("1.0",END)
            self.conn.execute("DELETE FROM saved_wikis WHERE title = ?;",(Name,))
            self.listBox.delete(0,END)
            self.fillListbox()
            self.conn.commit()
            
        else:
            return
        


    def exitProgram(self):
        quit()


def main():
    
    root = Tk()
    fileTransfer = Window_(root)
    root.mainloop()

    

if __name__ == "__main__": main()
