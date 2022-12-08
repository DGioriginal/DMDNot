from tkinter import *
import tkinter as tk
from time import sleep
from translate import Translator
from itertools import cycle
from tkinter import *
from tkinter import ttk
def polska_langueg():
  root.withdraw()
  win = Tk()
  win.title("DMDNot")
  win.geometry('1000x600')
  win.resizable(width=False, height=False)
  colors = cycle(['red', 'green', 'blue',])

  def change_color():
      win['bg'] = next(colors)
      win.after(2000, change_color)

  change_color()
  def close_win_pol():
    win.destroy()
  n= Menu(win)
  win.config(menu=m)
  fn = Menu(n)
  n.add_cascade(label="Tłumaczenie", menu=fn)
  fn.add_command(label="Angielski na polski", command=translator_ep)
  fn.add_command(label="Szukaj", command=info)
  fn.add_command(label="Angielski", command=info)
  fn.add_command(label="Wyjść",command=close_win_pol)

def translator_ep():
    roots = Tk()
    rBtn = IntVar()
    roots.title('Przetłumacz')
    roots.geometry('1000x600')
    roots.resizable(width=False, height=False)
    def translater():
        if (rBtn.get() == 0):
            translator = Translator(from_lang='English', to_lang='Polish')
        elif (rBtn.get() == 1):
            translator = Translator(from_lang='Polish', to_lang='English')
        txt = pole.get('0.0', END)
        w = translator.translate(txt)
        poleTranslate.delete('1.0', END)
        poleTranslate.insert('1.0', w)
    pole = Text(roots, width=80, height=10, font='Arial, 13')
    pole.pack(pady=10)

    algo01 = Radiobutton(roots, text="Tłumaczenie na język polski", variable=rBtn, value=0, font='Arial, 12')

    algo01.place(x=50, y=215)

    Btn = ttk.Button(roots, text="Przetłumacz", command=translater)
    
    Btn.pack()

    algo02 = Radiobutton(roots, text="Tłumaczenie na język angielski", variable=rBtn, value=1, font='Arial, 12')
    algo02.place(x=430, y=215)

    poleTranslate = Text(roots, width=80, height=10, font='Arial, 13')

    poleTranslate.pack(pady=10)

    roots.mainloop()

def translator_eu():
    root = Tk()
    rBtn = IntVar()
    root.title('Перекладачь')
    root.geometry('1000x600')
    root.resizable(width=False, height=False)
    def translater():
        if (rBtn.get() == 0):
            translator = Translator(from_lang='English', to_lang='Ukrainian')
        elif (rBtn.get() == 1):
            translator = Translator(from_lang='Ukrainian', to_lang='English')
        txt = pole.get('0.0', END)
        w = translator.translate(txt)
        poleTranslate.delete('1.0', END)
        poleTranslate.insert('1.0', w)
    pole = Text(root, width=80, height=10, font='Arial, 13')
    pole.pack(pady=10)

    algo01 = Radiobutton(root, text="Переклад на українську", variable=rBtn, value=0, font='red, 12')

    algo01.place(x=50, y=215)

    Btn = ttk.Button(root, text="Перекласти", command=translater)

    Btn.pack()

    algo02 = Radiobutton(root, text="Переклад на англійскуй", variable=rBtn, value=1, font='Arial, 12')
    algo02.place(x=430, y=215)

    poleTranslate = Text(root, width=80, height=10, font='Arial, 13')

    poleTranslate.pack(pady=10)

    root.mainloop()


def translator_er(): 
    root = Tk()
    rBtn = IntVar()
    root.title('Translator')
    root.geometry('1000x600')
    root.resizable(width=False, height=False)
    def translater():
        if (rBtn.get() == 0):
            translator = Translator(from_lang='English', to_lang='Polish')
        elif (rBtn.get() == 1):
            translator = Translator(from_lang='Polish', to_lang='English')
        txt = pole.get('0.0', END)
        w = translator.translate(txt)
        poleTranslate.delete('1.0', END)
        poleTranslate.insert('1.0', w)
    pole = Text(root, width=80, height=10, font='Arial, 13')
    pole.pack(pady=10)

    algo01 = Radiobutton(root, text="Translate to Polish", variable=rBtn, value=0, font='Arial, 12')

    algo01.place(x=50, y=215)

    Btn = ttk.Button(root, text="Translate", command=translater)

    Btn.pack()

    
    algo02 = Radiobutton(root, text="Translate to English", variable=rBtn, value=1, font='Arial, 12')
    algo02.place(x=430, y=215)

    poleTranslate = Text(root, width=80, height=10, font='Arial, 13')

    poleTranslate.pack(pady=10)

    root.mainloop()

def english_langueg():
  root.withdraw()
  win = Tk()
  win.title("DMDNot")
  win.geometry('1000x600')
  win.resizable(width=False, height=False)
  colors = cycle(['red', 'green', 'blue',])

  def change_color():
      win['bg'] = next(colors)
      win.after(2000, change_color)

  change_color()
  def close_win_en():
    winu.destroy()
  n= Menu(win)
  win.config(menu=m)
  fn = Menu(n)
  n.add_cascade(label="Tanslator", menu=fn)
  fn.add_command(label=" English to Polish", command=translator_er)
  fn.add_command(label="Search", command=info)
  fn.add_command(label="Englisch", command=info)
  fn.add_command(label="Exit",command=close_win_en)

def ukraine_langueg():
  root.withdraw()
  winu = Tk()
  winu.title("DMDNot")
  winu.geometry('1000x600')
  winu.resizable(width=False, height=False)
  colors = cycle(['red', 'green', 'blue',])

  def change_color():
      winu['bg'] = next(colors)
      winu.after(2000, change_color)

  change_color()
  def close_win_uk():
    winu.destroy()
  n= Menu(winu)
  winu.config(menu=m)
  fn = Menu(n)
  n.add_cascade(label="Перекладачь", menu=fn)
  fn.add_command(label="Англійська в Український", command=translator_eu)
  fn.add_command(label="Шукать", command=info)
  fn.add_command(label="Англійский", command=info)
  fn.add_command(label="Вихід", command=close_win_uk)

def info():
  win = Toplevel(root)
  colors = cycle(['red', 'green', 'blue',])

  def change_color():
      win['bg'] = next(colors)
      win.after(2000, change_color)

  change_color()
  win.geometry('1000x600')
  win.resizable(width=False, height=False)
  lab = Label(win, text="Version 1.0")
  lab.pack()


root = Tk()
root.title("DMDNot")
root.geometry('1000x600')
root.resizable(width=False, height=False)

def close_win():
    root.destroy()



colors = cycle(['red', 'green', 'blue',])

def change_color():
    root['bg'] = next(colors)
    root.after(2000, change_color)

change_color()

m = Menu(root)

root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Langueg", menu=fm)
fm.add_command(label="Ukraine", command=ukraine_langueg)
fm.add_command(label="Polska", command=polska_langueg)
fm.add_command(label="Englisch", command=english_langueg)


fm.add_command(label="  Exit", command=close_win)

hm = Menu(m)
m.add_cascade(label="Our", menu=hm)
hm.add_command(label="info", command=info)
hm.add_command(label="of programm", command=info)

root.mainloop()
