from tkinter import *
from tkinter import filedialog
import socket
import json
from os import listdir
from os.path import isfile, join
import tokrules

HOST = "172.20.10.4"
PORT = 8787
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

class text_editor:
    current_open_file = "no files"
    def open_file(self):
        open_return = filedialog.askopenfile(initialdir = "/home/elias/PycharmProjects/Compiler/venv", title = "Select File to Open", filetypes=(("text files","*.txt"),("all files","*.*")))
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

#onlyfiles = [f for f in listdir("/home/kevinfgn/PycharmProjects/GUI/venv/Archives")]

def sendJson():
    f = open("json_Test.json")
    data = f.read()
    f.close()
    sock.sendall(data.encode())
    sock.close()

def compilar():
    compiler = tokrules.Compiler()
    compiler.execute_file(te.current_open_file)
    compiler.start_lexer()
    compiler.start_parser()
    return

#requestEntry = Entry(new_root)
#requestEntry.place(x = 5, y =320)

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
compileButton.place(x=1250,y=0)

serverSend = Button(root, text="Send", command = sendJson)
serverSend.place(x=1250, y=30)

#requestButton = Button(root, text= "Request", command = request)
#requestButton.place(x=6, y=345)

root.mainloop()



