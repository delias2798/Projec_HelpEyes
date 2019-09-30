from tkinter import *
from tkinter import filedialog
import socket
import json
from os import listdir
from os.path import isfile, join

HOST = "172.20.10.4"
PORT = 9595
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect((HOST, PORT))

class text_editor:
    current_open_file = "no files"
    def open_file(self):
        open_return = filedialog.askopenfile(initialdir = "/", title = "Select File to Open", filetypes=(("text files","*.txt"),("all files","*.*")))
        if(open_return != None):
            self.text_area.delete(1.0, END)
            for line in open_return:
                self.text_area.insert(END,line)
            self.current_open_file = open_return.name
            open_return.close()

    def save_as_file(self):
        f = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt")
        if f is None:
            return
        text2save = self.text_area.get(1.0, END)
        self.current_open_file = f.name
        f.write(text2save)
        f.close()


    def save_file(self):
        if self.current_open_file == "no file":
            self.save_as_file()
        else:
            f = open(self.current_open_file, "w+")
            f.write(self.text_area.get(1.0,END))
            f.close()

    def new_file(self):
        self.text_area.delete(1.0,END)
        self.current_open_file = "no_file"





    def __init__(self, master):
        self.master = master
        master.title("GUI")
        self.text_area = Text(self.master, undo = True)
        self.text_area.pack(fill = BOTH, expand = 1)
        self.main_menu = Menu()
        self.master.config(menu = self.main_menu)

        self.file_menu = Menu(self.main_menu, tearoff= False)
        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label = "Open", command = self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Save As", command = self.save_as_file)
        self.file_menu.add_command(label = "Save", command = self.save_file)
        self.text_area.bind('<Control-z>',)

root = Tk()
te = text_editor(root)

new_root = Tk()
new_root.title("Server")
new_root.minsize(height=380, width=300)
entry1 = Entry(new_root)
entry1.place(x=130, y=10)
entry2 = Entry(new_root)
entry2.place(x=130, y=50)
entry3 = Entry(new_root)
entry3.place(x=130, y=90)
entry4 = Entry(new_root)
entry4.place(x=130, y=130)
entry5 = Entry(new_root)
entry5.place(x=130, y=170)
entry6 = Entry(new_root)
entry6.place(x=130, y=210)
entry7 = Entry(new_root)
entry7.place(x=130, y=250)
entry8 = Entry(new_root)
entry8.place(x=130, y=290)
label1 = Label(new_root, text="Distance")
label1.place(x=40, y=10)
label2 = Label(new_root, text="Temperature")
label2.place(x=40, y=50)
label3 = Label(new_root, text="Humidity")
label3.place(x=40, y=90)
label4 = Label(new_root, text="Sound")
label4.place(x=40, y=130)
label5 = Label(new_root, text="Brightness")
label5.place(x=40, y=170)
label6 = Label(new_root, text="Inclination")
label6.place(x=40, y=210)
label7 = Label(new_root, text="Vibration")
label7.place(x=40, y=250)
label8 = Label(new_root, text="Speed")
label8.place(x=40, y=290)

#onlyfiles = [f for f in listdir("/home/kevinfgn/PycharmProjects/GUI/venv/Archives")]

def sendJson():
    datajson = {
        "clientType" : "Compilador",
        "distance": entry1.get(),
        "temperature": entry2.get(),
        "humidity": entry3.get(),
        "sound": entry4.get(),
        "brightness": entry5.get(),
        "inclination": entry6.get(),
        "vibration": entry7.get(),
        "speed": entry8.get(),
    }

    data = json.dumps(datajson)
    print(datajson)
    #sock.sendall(data.encode())
    #sock.close()

def compilar():
    return

requestEntry = Entry(new_root)
requestEntry.place(x = 5, y =320)

#def requestAux(a,b):
#    if a == 0:
 #       print("No existe")
  #  elif onlyfiles[b] == requestEntry.get():
   #     True
    #else:
     #   return requestAux(a-1 , b+1)

#def request():
 #       if len(onlyfiles) == 0:
  #          print("No hay archivos")
   #     else:
    #        return requestAux(len(onlyfiles),0)


compileButton = Button(root,text="Run",command = compilar)
compileButton.place(x=1320,y=0)

serverSend = Button(new_root, text="Send", command = sendJson)
serverSend.place(x=230, y=320)

requestButton = Button(new_root, text= "Request", command = request)
requestButton.place(x=6, y=345)

root.mainloop()



