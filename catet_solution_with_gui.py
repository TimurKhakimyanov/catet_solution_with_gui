#A program to calculate the lengths of the legs and the hypotenuse of a triangle
#August 2020

#Программа для вычисления длины катетов и гипотенузы прямоугольного треугольника
#Август 2020 

from tkinter import *
from tkinter.ttk import Radiobutton
a = 0
b = 0
c = 0
#Функции для радио кнопок 
def clicka():
    entrya.delete(0 , END)
    entryb.delete(0 , END)
    entryc.delete(0 , END)
    global i 
    entrya.configure(state = 'disable')
    entryb.configure(state = 'normal')
    entryc.configure(state = 'normal')
    i = 1
    return i
def clickb():
    entrya.delete(0 , END)
    entryb.delete(0 , END)
    entryc.delete(0 , END)
    global i 
    entrya.configure(state = 'normal')
    entryb.configure(state = 'disable')
    entryc.configure(state = 'normal')
    i = 2
    return i
    
def clickc():
    entrya.delete(0 , END)
    entryb.delete(0 , END)
    entryc.delete(0 , END)
    global i 
    entrya.configure(state = 'normal')
    entryb.configure(state = 'normal')
    entryc.configure(state = 'disable')
    i = 3
    return i
#Функция для кнопки решения далее вычисления 
def clicksoul():
    if i == 1:
        b = int(entryb.get())
        c = int(entryc.get())
        c = c*c
        b = b*b
        a = c - b
        a = pow(a,0.5)
        entrya.configure(state = 'normal')
        entrya.insert(0 , a)
    if i == 2:
        a = int(entrya.get())
        c = int(entryc.get())
        c = c*c
        a = a*a
        b = c - a
        b = pow(b,0.5)
        entryb.configure(state = 'normal')
        entryb.insert(0 , b)
    if i == 3:
        a = int(entrya.get())
        b = int(entryb.get())
        a = a*a
        b = b*b
        c = a + b
        c = pow(c,0.5)
        entryc.configure(state = 'normal')
        entryc.insert(0 , c)
#Функция для очистки полей 
def clickclean():
    entrya.delete(0 , END)
    entryb.delete(0 , END)
    entryc.delete(0 , END)
    

#Создание окна , далее в основном функции для создания и размещения кнопок в окне и всякие штуки для интерфейса
windowdone = Tk()
windowdone.title("Catet programm")
windowdone.geometry('400x250')

#Создание кнопок 
btnsol = Button(windowdone , text = "Solute" , command = clicksoul)
btncln = Button(windowdone , text = "Clean" , command = clickclean)

#Создание "радио" кнопок 
rada = Radiobutton(windowdone, text='Найти один из катетов (а)', value=1 , command = clicka)  
radb = Radiobutton(windowdone, text='Найти один из катетов (b)', value=2 , command = clickb)  
radc = Radiobutton(windowdone, text='Найти гипотенузу (с)', value=3 , command = clickc)

#Создание пунктов для ввода 
entrya = Entry(windowdone , width = 20)
entryb = Entry(windowdone , width = 20)
entryc = Entry(windowdone , width = 20)

#Размещение "радио"кнопок
rada.place(x = 0 , y = 30)
radb.place(x = 0 , y = 60)
radc.place(x = 0 , y = 90)

#Размещение пунктов 
entrya.place(x = 250 , y = 30)
entryb.place(x = 250 , y = 60)
entryc.place(x = 250 , y = 90)

#Размещение кнопок
btnsol.place(x = 120 , y = 120)
btncln.place(x = 200 , y = 120)

windowdone.mainloop()
