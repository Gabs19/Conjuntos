from tkinter import *
import tkinter as tk

root = Tk()
root.title("Math Math")

class app:
    def __init__(self,master = None):
        
        a = []
        b = []
        
        uniao = []
        intersecao = []
        complet_b = []
        complet_a = []
        
        def inserindo_a():
            a.append(valores_a.get())
            show_me_a['text'] = a
            print(a)
            
        def inserindo_b():
            b.append(valores_b.get())
            show_me_b['text'] = b
            print(b)
            
        def union():
            for i in a:
                if i not in uniao:
                    uniao.append(i)
            
            for i in b:
                if i not in uniao:
                    uniao.append(i)   
            
            show_me_union['text'] = 'União : {}'.format(uniao) 
            
        def intersection():
            for i in a:
                if i in b:
                    intersecao.append(i)    
            show_me_inters['text'] = 'Interseção: {}'.format(intersecao)       
                     
        def completemento_b():
            for i in a:
                if i not in b:
                    complet_b.append(i)
            show_me_complete_b['text'] = 'Complemento de b: {}'.format(complet_b)
            
        def complemento_a():
            for i in b:
                if i not in a:
                    complet_a.append(i)
            show_me_complete_a['text'] = 'Complemtento de a: {}'.format(complet_a)
            
            
        conjunto_a = Label(text = "Digite os Valores do Conjunto A: ")
        conjunto_a.pack()
        conjunto_a.place(x = 10, y = 30)
        
        valores_a = Entry()
        valores_a.pack()
        valores_a['width'] = 4
        valores_a.place(x = 250, y = 30)

        inserir_a = Button(text = "Inserir",command = inserindo_a)
        inserir_a.pack
        inserir_a.place(x = 300, y = 30)
        
        conjunto_b = Label(text = "Digite os Valores do Conjunto B: ")
        conjunto_b.pack()
        conjunto_b.place(x = 10, y = 60)
        
        valores_b = Entry()
        valores_b.pack()
        valores_b['width'] = 4
        valores_b.place(x = 250, y = 60)
        
        inserir_b = Button(text = 'Inserir', command = inserindo_b)
        inserir_b.pack()
        inserir_b.place(x = 300, y = 60)
        
        show_me_a = Label()
        show_me_a.pack()
        show_me_a.configure(relief = 'groove', border = 2)
        show_me_a.place(x = 10, y = 90)
        
        show_me_b = Label()
        show_me_b.pack()
        show_me_b.configure(relief = 'groove', border = 2)
        show_me_b.place(x = 10, y = 120)
        
        
        uni_btn = Button(text = 'União', command = union)
        uni_btn.pack()
        uni_btn.place(x = 10, y = 160)
        
        inters_btn = Button(text = 'Interseção', command = intersection)
        inters_btn.pack()
        inters_btn.place(x = 80, y = 160)
        
        complet_a_btn = Button(text = 'Complet de a',command = complemento_a)
        complet_a_btn.pack()
        complet_a_btn.place(x = 180, y = 160 ) 
        
        complet_b_btn = Button(text = 'Complet de b', command = completemento_b)
        complet_b_btn.pack()
        complet_b_btn.place(x = 300, y = 160)
        
        show_me_union = Label()
        show_me_union.pack()
        show_me_union.place(x = 10, y = 200)
        
        show_me_inters = Label()
        show_me_inters.pack()
        show_me_inters.place(x = 10, y = 220)
        
        show_me_complete_a = Label()
        show_me_complete_a.pack()
        show_me_complete_a.place(x = 10, y = 240)
           
        show_me_complete_b = Label()
        show_me_complete_b.pack()
        show_me_complete_b.place(x = 10, y = 260)
           
        
        
app(root)
root.geometry("450x300+10+10")
root.mainloop()
