from tkinter import*

root = Tk()
root.geometry("350x500")
root.title("CALCULADORA")

framePrincipal = Frame(root, bg="#00aae4")
framePrincipal.pack(fill="both", expand=1)

A=IntVar()
B=IntVar()
valorA= IntVar()
bx= IntVar()
suma=IntVar()
multiplicacion=IntVar()
resta=IntVar()
division=IntVar()
c=IntVar()
igual=IntVar()
r=IntVar

def sumando():
    r=valorA.get()+bx.get()
    respuesta.config(text=r)

def multi():
    r=valorA.get()*bx.get()
    respuesta.config(text=r)
    
def div():
    r=valorA.get()/bx.get()
    respuesta.config(text=r)
    
def res():
    r=valorA.get()-bx.get()
    respuesta.config(text=r)
    
def igua():
    pass
 
    
def clc():
    pass

#salidas o mensajes
titulo = Label(framePrincipal, text="calculadora", bg="white", font=("Roboto", 20, "bold")).pack()
numeroA = Label (framePrincipal, text="NÚMERO A =   ").place(x=25, y=60)
numeroB = Label (framePrincipal, text="NÚMERO B =   ").place(x=25, y=90)
resx = Label (framePrincipal,text="RESULTADO =" ).place(x=25, y=120)
respuesta = Label (framePrincipal,text="" )
respuesta.place(x=125, y=120)


#entradas
A = Entry(framePrincipal, textvariable=valorA)
A.place(x=125, y=60)
B = Entry(framePrincipal, textvariable=bx)
B.place(x=125, y=90)

#Botones
botonsuma=Button(framePrincipal, text="SUMA", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=sumando).place(x=25, y=180)
botonmultiplicacion=Button(framePrincipal, text="MULT", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=multi).place(x=120, y=180)
botonresta=Button(framePrincipal, text="RESTA", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=res).place(x=215, y=180)
botondivision=Button(framePrincipal, text="DIVISIÓN", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=div).place(x=25, y=230)
botonc=Button(framePrincipal, text="C", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=clc).place(x=120, y=230)

botonigual=Button(framePrincipal, text="=", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=igua).place(x=215, y=230)

root.mainloop()