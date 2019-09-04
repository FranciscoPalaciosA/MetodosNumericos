from tkinter import *
import numbers_chi_streak as nums

tk = Tk()

inputs = ['X:','a:','c:','m:','N:', 'alpha:','min:','max:']

def generar():
    flag = True
    for i in inputlst:
        aux = i.get()
        if aux is "" or aux == "Campo requerido...":
            i.delete(0, "end")
            i.insert(0, "")
            i.insert(0, "Campo requerido...")
            flag = False
    if flag:
        Xi = float(inputlst[0].get()) #3734
        a = float(inputlst[1].get()) #1687
        c = float(inputlst[2].get()) #0
        m = float(inputlst[3].get()) #21474836434
        N = int(inputlst[4].get()) #40
        alpha = float(inputlst[5].get()) #0.05
        min_n = float(inputlst[6].get()) # 0
        max_n = float(inputlst[7].get()) #0
        random_numbers = nums.get_numbers(Xi,a,c,m,N,min_n,max_n)
        nums.export_to_txt(random_numbers, min_n, max_n)
        print(nums.chi_square(N, random_numbers, alpha))
        print(nums.increasing_streak(random_numbers, alpha))

def hipotesis():
    print("hipotesis")

def on_entry_click(event):
    if event.widget.get() == "Campo requerido...":
        event.widget.delete(0, "end")
        event.widget.insert(0, "")
        event.widget.config(fg = "black")
def on_focusout(event):
    if event.widget.get() == "":
        event.widget.insert(0, "Campo requerido...")
        event.widget.config(fg = "grey")

r = 0
inputlst = []
for c in inputs:
    Label(text=c, relief=RIDGE, width=10).grid(row=r,column=0)
    inputlst.append(Entry(relief=SUNKEN, width=10))
    inputlst[r].grid(row=r,column=1)
    inputlst[r].bind('<FocusIn>', on_entry_click)
    inputlst[r].bind('<FocusOut>', on_focusout)
    inputlst[r].config(fg = "grey")
    r = r + 1

Label(text="G.N.A", width=10, height=1).grid(row=0,column=4)
Button(text="Generar excel", width=15, height=1, command=generar).grid(row=2, column=4)
Button(text="Prueba de hipótesis", width=15, height=1, command=hipotesis).grid(row=5, column=4)

mainloop()
