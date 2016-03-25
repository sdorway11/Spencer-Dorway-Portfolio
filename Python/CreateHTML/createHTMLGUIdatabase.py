import os,sqlite3
from tkinter import *
from tkinter import ttk, Text, messagebox

class Window_:
    
    def __init__(self, master):

        self.conn = sqlite3.connect('pre-madeContent.db')
        #self.deleteTable()
        self.createTable()
        

        # Create the menu bar
        menuBar = Menu(master)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        editMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit",menu=editMenu)
        master.config(menu=menuBar)
        

        master.title("File check and transfer")
        master.resizable(False,False)
        master.configure(background = '#2d3953')

        #self.Center()
        self.style = ttk.Style()
        self.style.configure("TFrame", background = '#2d3953')
        self.style.configure("TButton",background = '#2d3953')
        self.style.configure('TLabel', background = '#2d3953', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold')) 
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        ttk.Label(self.frame_header, text = 'Update Content', style = 'Header.TLabel'
                  ).grid(row = 0, column = 3,columnspan=2,ipadx=5,ipady=5)
        
        

        ttk.Label(self.frame_header, text="").grid(row=0,column=0,ipadx=3)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.listBox = Listbox(self.frame_content,width = 40,height=18,selectmode=SINGLE,
                               yscrollcommand=Scrollbar(master))
        self.enterText= ttk.Label(self.frame_content, text="Text for webpage:",font=('arial',11,'bold'))
        self.savedText= ttk.Label(self.frame_content, text="Saved pre-made text:",font=('arial',11,'bold'))
        self.titleInput= ttk.Label(self.frame_content, text="Title for Entry:",font=('arial',11,'bold'))
        self.enterBtn= Button(self.frame_content, text="Post to webpage",height=2)
        self.enterContent= Text(self.frame_content,width=50,height=20)
        self.titleText= Entry(self.frame_content,width=50,font=('arial',11,'bold'))
        self.saveBtn= Button(self.frame_content, text="Save Entry",font=('arial',11,'bold'))
        self.viewBtn= Button(self.frame_content, text="View pre-made text",height=2)

        ttk.Label(self.frame_content, text="").grid(row=0,column=0,ipadx=3)
        ttk.Label(self.frame_content, text="").grid(row=0,column=3,ipadx=3)
        ttk.Label(self.frame_content, text="").grid(row=8,column=1,ipadx=3)
        ttk.Label(self.frame_content, text="").grid(row=5,column=1,ipadx=3)
        ttk.Label(self.frame_content, text="").grid(row=0,column=5,ipadx=3)


        self.enterText.grid(row=3,column=1,sticky=W)
        self.enterContent.grid(row=4,column=1)
        self.enterBtn.grid(row=6,column=1,rowspan=2,sticky=NSEW)
        self.listBox.grid(row=4,column=4,sticky=S)
        self.savedText.grid(row=4,column=4,sticky=N)
        self.titleText.grid(row=2,column=1,sticky=NSEW)
        self.titleInput.grid(row=1,column=1,sticky=W)
        self.saveBtn.grid(row=2,column=4,sticky=NSEW)
        self.viewBtn.grid(row=6,column=4,sticky=NSEW)

        self.enterBtn.config(font=("Arial",13,"bold"))
        self.enterBtn.config(command=self.addContent)
        self.viewBtn.config(font=("arial",13,"bold"),command=self.viewEntry)
        self.saveBtn.config(command=self.saveEntry)
        
        


        
        # Create the menu bar
        menuBar = Menu(master)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        editMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit",menu=editMenu)
        master.config(menu=menuBar)

        self.setTemplates()


    def createPage(self,into):
        file = open("WebPageUpdate.html", "w+")
        file.write( "<html>\n\
<body>\n\
{}\n\
</body>\n\
</html>".format(into))



    def createTable(self):
        self.conn.execute("CREATE TABLE if not exists \
                webContent(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                preview STRING, bodyContent STRING);")

    def saveEntry(self):
        titleInput = self.titleText.get()
        textInput = self.enterContent.get('1.0',END)
        self.conn.execute("INSERT INTO webContent(preview,bodyContent) \
                           VALUES (?,?);",(titleInput,textInput))
        cursor = self.conn.execute("SELECT * from webContent;")
        rows = cursor.fetchall()
        nextEntry = len(rows)
        self.listBox.delete(0,END)

        for row in rows:
            self.listBox.insert(nextEntry,row[1])
            
        self.titleText.delete(0,END)
        self.enterContent.delete('1.0',END)

        self.conn.commit()

    def setTemplates(self):
        try:
            preSets = [
                (1, "Updating Website", "The website is currently being updated. Thank you for your patience."),
                (2, "Tech Problems", "We are currently experiencing some technical difficulties. Thank you for your patience."),
                (3, "Sumer Sale", "Come in and check out our new summer sale!"),
                (4, "Winter Sale", "Come in and check out our new winter sale!"),
                (5, "Spring Sale", "Come in and check out our new Spring sale!"),
                (6, "Fall Sale", "Come in and check out our new Fall sale!")
                ]

        
            for set in preSets:
                self.conn.execute("INSERT INTO webContent(ID, preview, bodyContent) VALUES (?,?,?);",(set[0],set[1],set[2]))

            self.conn.commit()

        except:
            pass

        cursor = self.conn.execute("SELECT * from webContent;")
        rows = cursor.fetchall()
        nextEntry = len(rows)
        self.listBox.delete(0,END)

        for row in rows:
            self.listBox.insert(nextEntry,row[1])
            
            

    def viewEntry(self):
        items = self.listBox.curselection()
        for item in items:
            cursor = self.conn.execute("SELECT * from webContent;")
            rows = cursor.fetchall()
            print(rows[item])
            self.titleText.delete(0,END)
            self.enterContent.delete('1.0',END)
            self.titleText.insert(0,(rows[item][1]))
            self.enterContent.insert('1.0',(rows[item][2]))
        
    def addContent(self):
        into = self.enterContent.get("1.0",END)
        self.createPage(into)
        pathError = messagebox.showinfo("", "Your Content has been added")
        self.enterContent.delete("1.0",END)

        self.conn.commit()
        
    def deleteTable(self):
        self.conn.execute("DROP TABLE if exists webContent;")
        self.conn.commit()



    def exitProgram(self):
        quit()
       
    


    def exitProgram(self):
        quit()
       

def main():
    
    root = Tk()
    fileTransfer = Window_(root)
    root.mainloop()

if __name__ == "__main__": main()
