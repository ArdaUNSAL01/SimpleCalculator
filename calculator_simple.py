import tkinter as tk
import random
from tkinter import colorchooser

pencere = tk.Tk()
pencere.title("Hesap Makinesi") 
pencere.geometry("196x270") 

# Entry 
entry = tk.Entry(pencere)
entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=5)

#Fonksiyonlar
def yaz(deger):
    entry.insert(tk.END, deger)

def temizle():
    entry.delete(0, tk.END)

def hesapla():
    try:
        sonuc = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(sonuc))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Hata")

def renk_degistir():
    renk_kodu = colorchooser.askcolor(title="Bir Renk Seç")[1]
    if renk_kodu:
        pencere.config(bg=renk_kodu)

# Butonlar
btn1 = tk.Button(pencere, text="1", width=5, height=2, command=lambda: yaz("1"))
btn2 = tk.Button(pencere, text="2", width=5, height=2, command=lambda: yaz("2"))
btn3 = tk.Button(pencere, text="3", width=5, height=2, command=lambda: yaz("3"))
btn4 = tk.Button(pencere, text="4", width=5, height=2, command=lambda: yaz("4"))
btn5 = tk.Button(pencere, text="5", width=5, height=2, command=lambda: yaz("5"))
btn6 = tk.Button(pencere, text="6", width=5, height=2, command=lambda: yaz("6"))
btn7 = tk.Button(pencere, text="7", width=5, height=2, command=lambda: yaz("7"))
btn8 = tk.Button(pencere, text="8", width=5, height=2, command=lambda: yaz("8"))
btn9 = tk.Button(pencere, text="9", width=5, height=2, command=lambda: yaz("9"))
btn0 = tk.Button(pencere, text="0", width=5, height=2, command=lambda: yaz("0"))

btn_clear = tk.Button(pencere, text="C", width=5, height=2, command=temizle)
btn_hesapla = tk.Button(pencere, text="=", width=5, height=2, command=hesapla)

btn_eksi = tk.Button(pencere, text="-", width=5, height=2, command=lambda: yaz("-"))
btn_arti = tk.Button(pencere, text="+", width=5, height=2, command=lambda: yaz("+"))
btn_carp = tk.Button(pencere, text="*", width=5, height=2, command=lambda: yaz("*"))
btn_bol = tk.Button(pencere, text="/", width=5, height=2, command=lambda: yaz("/"))

btn_renk = tk.Button(pencere, text="Renk Değiştir", width=20, command=renk_degistir)

# Butonların gridi 
btn1.grid(row=1, column=0, padx=2, pady=2)
btn2.grid(row=1, column=1, padx=2, pady=2)
btn3.grid(row=1, column=2, padx=2, pady=2)
btn_bol.grid(row=1, column=3, padx=2, pady=2)

btn4.grid(row=2, column=0, padx=2, pady=2)
btn5.grid(row=2, column=1, padx=2, pady=2)
btn6.grid(row=2, column=2, padx=2, pady=2)
btn_carp.grid(row=2, column=3, padx=2, pady=2)

btn7.grid(row=3, column=0, padx=2, pady=2)
btn8.grid(row=3, column=1, padx=2, pady=2)
btn9.grid(row=3, column=2, padx=2, pady=2)
btn_eksi.grid(row=3, column=3, padx=2, pady=2)

btn_clear.grid(row=4, column=0, padx=2, pady=2)
btn0.grid(row=4, column=1, padx=2, pady=2)
btn_hesapla.grid(row=4, column=2, padx=2, pady=2)
btn_arti.grid(row=4, column=3, padx=2, pady=2)

btn_renk.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

pencere.mainloop()
