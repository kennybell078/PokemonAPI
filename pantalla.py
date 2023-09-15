import tkinter
import requests
from PIL import Image,ImageTk
from io import BytesIO

class Pantalla:   

    image_url = ""    
    anchoBanco = 90
    altoBanco = 120
    def __init__(self):
        self.juego = tkinter.Tk()
        self.juego.title("Jogo?")
        self.juego.geometry("400x600")
        #self.juego.resizable(False,False)

        self.FramePadre = tkinter.Frame(self.juego,bg="White")
        self.FramePadre.grid(column=0,row=1)

        self.Pelea = tkinter.Frame(self.FramePadre, bg="Black",width=400,height=600)
        self.Pelea.grid()

        self.fp1 = tkinter.Frame(self.Pelea,bg="red",width=133,height=120)
        self.fp1.grid(row=0,column=0)
        self.fp2 = tkinter.Frame(self.Pelea,bg="white",width=133,height=120)
        self.fp2.grid(row=0,column=1)
        self.fp3 = tkinter.Frame(self.Pelea,bg="white",width=133,height=120)
        self.fp3.grid(row=0,column=2)
        self.fp4 = tkinter.Frame(self.Pelea,bg="white",width=133,height=120)
        self.fp4.grid(row=1,column=0)
        self.fp5 = tkinter.Frame(self.Pelea,bg="red",width=133,height=120)
        self.fp5.grid(row=1,column=1)
        self.fp6 = tkinter.Frame(self.Pelea,bg="white",width=133,height=120)
        self.fp6.grid(row=1,column=2)
        self.fp7 = tkinter.Frame(self.Pelea,bg="white",width=133,height=120)
        self.fp7.grid(row=2,column=0)
        self.fp8 = tkinter.Frame(self.Pelea,bg="white",width=133,height=120)
        self.fp8.grid(row=2,column=1)
        self.fp9 = tkinter.Frame(self.Pelea,bg="red",width=133,height=120)
        self.fp9.grid(row=2,column=2)

        self.Lineauwu = tkinter.Frame(self.FramePadre, bg="Blue",width=400,height=10)
        self.Lineauwu.grid()

        self.Ataques = tkinter.Frame(self.FramePadre, bg="White",width=400,height=600)
        self.Ataques.grid()

        self.ft1 = tkinter.Frame(self.Ataques,bg="black",width=100,height=100)
        self.ft1.grid(row=0,column=0)
        self.ft2 = tkinter.Frame(self.Ataques,bg="white",width=100,height=100)
        self.ft2.grid(row=0,column=1)
        self.ft3 = tkinter.Frame(self.Ataques,bg="black",width=100,height=100)
        self.ft3.grid(row=0,column=2)
        self.ft4 = tkinter.Frame(self.Ataques,bg="white",width=100,height=100)
        self.ft4.grid(row=0,column=3)

        self.Lineauwu2 = tkinter.Frame(self.FramePadre, bg="Blue",width=400,height=10)
        self.Lineauwu2.grid()

        self.Cambiopoke = tkinter.Frame(self.FramePadre, bg="Blue",width=400,height=120)
        self.Cambiopoke.grid()


        self.cp1 = tkinter.Label(self.Cambiopoke,bg="Orange",width=self.anchoBanco,height=self.altoBanco)
        self.cp1.grid(row=0,column=0)
        self.cp2 = tkinter.Label(self.Cambiopoke,bg="White",width=self.anchoBanco,height=self.altoBanco)
        self.cp2.grid(row=0,column=1)
        self.cp3 = tkinter.Label(self.Cambiopoke,bg="Orange",width=self.anchoBanco,height=self.altoBanco)
        self.cp3.grid(row=0,column=2)
        self.cp4 = tkinter.Label(self.Cambiopoke,bg="White",width=self.anchoBanco,height=self.altoBanco)
        self.cp4.grid(row=0,column=3)
        self.cp5 = tkinter.Label(self.Cambiopoke,bg="Orange",width=self.anchoBanco,height=self.altoBanco)
        self.cp5.grid(row=0,column=4)
        self.cp6 = tkinter.Label(self.Cambiopoke,bg="White",width=self.anchoBanco,height=self.altoBanco)
        self.cp6.grid(row=0,column=5)

        self.bancoDeSuplentes = [self.cp1, self.cp2, self.cp3, self.cp4, self.cp5, self.cp6]
        
        self.Lineauwu3 = tkinter.Frame(self.FramePadre, bg="Violet",width=400,height=10)
        self.Lineauwu3.grid()


    def insertarFoto(self, frame, url):
        response = requests.get(url)
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        photo = ImageTk.PhotoImage(image)
        frame.config(image=photo)
        frame.image = photo


    def actualizarPantalla(self):

        image_url = ""
        self.image_url = self.img
        response = requests.get(self.image_url)
        #print(self.image_url)
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        photo = ImageTk.PhotoImage(image)
        self.fp7.config(image=photo)
        self.fp7.image = photo
        

if __name__ == '__main__':
    p = Pantalla()
    p.juego.mainloop()