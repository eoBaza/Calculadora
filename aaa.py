from asyncio import events
from subprocess import REALTIME_PRIORITY_CLASS
from tkinter import *
from tkinter import ttk 

#cores
cor1 = "#151e1f" #cinza
cor2= "#56824f" #verde
cor3= "#359da1" #azul
cor4= "#afb53e" #laranja
cor5= "#81b53e" #amaraleo

janela =Tk()
janela.title("Calculadora")
janela.geometry("450x400")
janela.config(bg=cor1)



#frame
frame_tela = Frame(janela, width=450, height=100, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=450, height=300, bg= cor3)
frame_body.grid(row=1, column=0)

#todos valores
todos_valores= ""



#função
def entrar_valores(event):

    global todos_valores

    todos_valores= todos_valores + str(event)
    
    #passando valor para tela
    valor_texto.set(todos_valores)

#funcao calcular
def calcular():
    global todos_valores
    resultado=eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)
    

#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")




#label
valor_texto= StringVar()

app_label= Label(frame_tela, textvariable=valor_texto,width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Yvy 33 bold"), bg=cor1, fg="#feffff")
app_label.place(x=0,y=0)

#bootons
b_1 = Button(frame_body, command= limpar_tela, text="C", width=15, height=3, bg=cor4, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=1, y=0)
b_2 = Button(frame_body, command= lambda: entrar_valores('%'),text="%", width=15, height=3, bg=cor4, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=113, y=0)
b_19=Button(frame_body, command= lambda: entrar_valores('±'), text="±", width=15, height=3, bg=cor4, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_19.place(x=227, y=0)
b_3 = Button(frame_body, command= lambda: entrar_valores('/'), text="÷", width=15, height=3, bg=cor5, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=340, y=0)
b_4 = Button(frame_body, command= lambda: entrar_valores('7'), text="7", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=56)
b_5 = Button(frame_body, command= lambda: entrar_valores('8'), text="8", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=112, y=56)
b_6 = Button(frame_body, command= lambda: entrar_valores('9'), text="9", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=226, y=56)
b_7 = Button(frame_body, command= lambda: entrar_valores('*'), text="x", width=15, height=3, bg=cor5, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=340, y=56)
b_8 = Button(frame_body, command= lambda: entrar_valores('4'), text="4", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=112)
b_9= Button(frame_body, command= lambda: entrar_valores('5'), text="5", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=112, y=112)
b_10=Button(frame_body, command= lambda: entrar_valores('6'), text="6", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=226, y=112)
b_11=Button(frame_body, command= lambda: entrar_valores('-'), text="-", width=15, height=3, bg=cor5, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=340, y=112)
b_12=Button(frame_body, command= lambda: entrar_valores('1'), text="1", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=165)
b_13=Button(frame_body, command= lambda: entrar_valores('2'), text="2", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=113, y=165)
b_14=Button(frame_body, command= lambda: entrar_valores('3'), text="3", width=15, height=3, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=226,y=165)
b_15=Button(frame_body, command= lambda: entrar_valores('+'), text="+", width=15, height=3, bg= cor5, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=340, y=165)
b_16=Button(frame_body, command= lambda: entrar_valores('0'), text="0", width= 20, height=5, font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=221)
b_17=Button(frame_body, command= lambda: entrar_valores(','), text=",", width=15, height=5, font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=166, y=221)
b_18=Button(frame_body,command=calcular, text="=", width=20, height=5, bg=cor5, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=301, y=221)



janela.mainloop()
