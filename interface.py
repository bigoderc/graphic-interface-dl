from tkinter import filedialog 
from tkinter import*
import gatocachorro
 


treinoimg = " "
testeimg = " "
def load_directory():
    dirLocal = filedialog.askdirectory()
    return dirLocal
def load_file():
    fileLocal = filedialog.askopenfilename()
    return fileLocal    
class Interface:
    def __init__(self, master=None):
    
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 100
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
  
        self.segundocontainer = Frame(master)
        self.segundocontainer["padx"] = 100
        self.segundocontainer["pady"] = 15
        self.segundocontainer.pack()
        
        self.terceirocontainer = Frame(master)
        self.terceirocontainer["padx"] = 100
        self.terceirocontainer["pady"] = 15
        self.terceirocontainer.pack()
        
        
        
        
        self.quartocontainer = Frame(master)
        self.quartocontainer["padx"] = 100
        self.quartocontainer["pady"] = 20
        self.quartocontainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Classificador de imagens")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()
  
        self.autenticar = Button(self.segundocontainer)
        self.autenticar["text"] = "Imagens teste"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["background"] = "yellow2"
        self.autenticar["width"] = 15
        self.autenticar["command"] = self.importtest
        self.autenticar.pack(side=LEFT)
        
        self.autenticar = Button(self.segundocontainer)
        self.autenticar["text"] = "Imagens treino"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["background"] = "yellow2"
        self.autenticar["width"] = 15
        self.autenticar["command"] = self.importtreino
        self.autenticar.pack()
       
  
        self.autenticar = Button(self.terceirocontainer)
        self.autenticar["text"] = "Classificar"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["background"] = "red2"
        self.autenticar["width"] = 25
        self.autenticar["command"] = self.classificar
        self.autenticar.pack()
  
        self.accuracy = Label(self.quartocontainer, text="aqui aparecerá sua accuracy", font=self.fontePadrao, background='red3')
        self.accuracy.pack()
        
    def importtreino(self):
       global treinoimg
       treinoimg= load_directory()
 
    def importtest(self):
        global testeimg
        testeimg = load_directory()
    def classificar(self):
        global treinoimg
        global testeimg
        gatocachorro.training(treinoimg,testeimg )
        
  
root = Tk()
Interface(root)
root.mainloop()
