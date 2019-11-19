from tkinter import *
import sqlite3
import random
from tkinter import ttk
import tkinter as tk

f=''
flag=''
flags=''

login=sqlite3.connect("admin.db")
l=login.cursor()

c=sqlite3.connect("medicine.db")
cur=c.cursor()

columns=('Sl No', 'Nama', 'Type', 'Stock', 'Harga', 'Tujuan')

def open_win(): #OPENS MAIN MENU----------------------------------------------------------------------------MAIN MENU
    global apt, flag
    flag='apt'
    apt=Tk()
    apt.geometry("897x600")
    apt.resizable(False, False)
    apt.iconbitmap(r'medicine.ico')
    apt.title("Menu Utama")
    

    frame_menu = Frame(apt, bd=5, bg="white" )
    frame_menu.place(width=897, height=600)

    gambar = PhotoImage(file="latar.png")  #kalo nda muncul backgroundnya, sesuikan lokasi "Login.png"
    background = Label(frame_menu, image=gambar)
    background.pack(expand=True)

    gambar1 = PhotoImage(file="judul.png")  #kalo nda muncul backgroundnya, sesuikan lokasi "Login.png"
    judul = Label(apt, image=gambar1, bg="#068f1f").place(x="50",y=50)

    # Label(apt, text="Apotek", font=('Calibri',20), bg="#41183A", fg="white").place(x=400, y=50)

    # Button(apt,text='Hapus Produk', width=25,command=delete_stock).place(x=250, y = 200)
    # Button(apt,text='Modify',width=15, command=modify).place(x=450, y= 200)
    gambar_stok = PhotoImage(file="stok.png")  #kalo nda muncul backgroundnya, sesuikan lokasi "Login.png"
    button_stok = Button(apt, text='OBAT', bg="#068f1f", fg="white", bd="3", font=('Helvetica 18 bold'), command=stock).place(x=620, y=190, width=250, height=75)
    stok = Label(button_stok, image=gambar_stok, bg="#068f1f").place(x=630,y=200)

    gambar_update = PhotoImage(file="medical.png")
    button_update = Button(apt, text="UPDATE", bg="#068f1f", fg="white", bd="3", font=('Helvetica 15 bold'), command = modify).place(x=620, y=270, width=250, height=75)
    update = Label(button_update, image=gambar_update, bg="#068f1f").place(x=630,y=280)

    gambar_hapus = PhotoImage(file="sampah.png")
    button_hapus = Button(apt, text="HAPUS", bg="#068f1f", fg="white", bd="3", font=('Helvetica 15 bold'), command = delete_stock).place(x=620, y=350, width=250, height=70)
    hapus = Label(button_hapus, image=gambar_hapus, bg="#068f1f").place(x=630,y=360)

    gambar_kasir = PhotoImage(file="kasir.png")  #kalo nda muncul backgroundnya, sesuikan lokasi "Login.png"
    button_kasir = Button(apt, text="KASIR", bg="#068f1f", fg="white", bd="3", command=billing, font=('Helvetica 18 bold')).place(x=620, y=430, width=250, height=70)
    kasir = Label(button_kasir, image=gambar_kasir, bg="#068f1f").place(x=630,y=440)
    
    gambar_logout = PhotoImage(file="logout-fix.png")  #kalo nda muncul backgroundnya, sesuikan lokasi "Login.png"
    button_logout = Button(apt, text='LOGOUT', bg="#068f1f", fg="white", bd="3", font=('Helvetica 15 bold'), command=again).place(x=620, y=510, width=250, height=75)
    logout = Label(button_logout, image=gambar_logout, bg="#068f1f").place(x=630,y=520)

    
    
    # label_logout = Label(apt, text='LOGOUT', bg="#068f1f", fg="white", font=('Helvetica 15'), command=again).place(x=760, y=540)

    apt.mainloop()

def delete_stock(): #Jendela hapus
    global cur, c, flag, lb1, d, s1
    apt.destroy()
    flag='d'
    d=Tk()
    d.title("Hapus Produk")
    d.geometry("897x600")
    d.resizable(False, False)
    d.iconbitmap(r'medicine.ico')
   

    frame_menu = Frame(d, bd=5, bg="white" )
    frame_menu.place(width=897, height=600)
    judul = Label(d, text="Hapus Barang", bg="white", font=('Helvetica 15')).place(x=20, y=20)
    garis = Label(d, text="-"*30, fg="#068f1f", bg="white", font=('Helvetica 8 bold'))
    garis.place(x=20, y=50, height=5)

    frame_table = Frame(d, bg="#068f1f").place(x=20, y=175, width=760, height=217)

    label_nama_tbl = Label(d, text="Nama Obat", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=40,y=175)
    

    label_jenis_tbl = Label(d, text="Jenis Obat", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=250,y=175)
    

    label_stok_tbl = Label(d, text="Stok", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=370,y=175)
    

    label_harga_tbl = Label(d, text="Harga", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=460,y=175)
    

    label_tujuan_tbl = Label(d, text="Tujuan Obat", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=550,y=175)

    ren()

    button_delete = Button(d, text="HAPUS", bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command = delt)
    button_delete.place(x=300, y=450, width=125, height=50)
    button_menu = Button(d, text="MAIN MENU", bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command = main_menu)
    button_menu.place(x=500, y=450, width=125, height=50)

    d.mainloop()

def ren():
    global lb1,d,cur,c
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)
        lb4.yview(*args)
        lb5.yview(*args)
        # lb6.yview(*args)

    def onmousewheel():
        lb1.ywiew=('scroll',event.delta,'units')
        lb2.ywiew=('scroll',event.delta,'units')
        lb3.ywiew=('scroll',event.delta,'units')
        lb4.ywiew=('scroll',event.delta,'units')
        lb5.ywiew=('scroll',event.delta,'units')
        # lb6.ywiew=('scroll',event.delta,'units')
        
        return 'break'
    cx=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(d,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set)
    lb2=Listbox(d,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set)
    lb3=Listbox(d,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set,width=10)
    lb4=Listbox(d,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set,width=7)
    lb5=Listbox(d,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set,width=25)
    # lb6=Listbox(sto,yscrollcommand=vsb.set,width=37)
    vsb.place(relx=1, rely=0, relheight=1, anchor='ne')
    lb1.place(x=40,y=200, width=190, height=160)
    lb2.place(x=250,y=200, width=100, height=160)
    lb3.place(x=370,y=200, width=70, height=160)
    lb4.place(x=460,y=200, width=70, height=160)
    lb5.place(x=550,y=200, width=210, height=160)
    # lb6.grid(row=15,column=5)
    lb1.bind('<MouseWheel>',onmousewheel)
    lb2.bind('<MouseWheel>',onmousewheel)
    lb3.bind('<MouseWheel>',onmousewheel)
    lb4.bind('<MouseWheel>',onmousewheel)
    lb5.bind('<MouseWheel>',onmousewheel)
    # lb6.bind('<MouseWheel>',onmousewheel)
    cur.execute("select *from med")
    for i in cur:
        cx+=1
        seq=(str(i[0]),str(i[1]))
        lb1.insert(cx,'. '.join(seq))
        lb2.insert(cx,i[2])
        lb3.insert(cx,i[3])
        lb4.insert(cx,i[4])
        lb5.insert(cx,i[5])
    c.commit()
    lb1.bind('<<ListboxSelect>>', sel_del)


def sel_del(e):
    global lb1, d, cur, c,p, sl2
    p=lb1.curselection()
    print (p)
    x=0
    sl2=''
    cur.execute("select * from med")
    for i in cur:
        print (x, p[0])
        if x==int(p[0]):
            sl2=i[0]
            break
        x+=1
    c.commit()
    print (sl2)
    # Label(d,text=' ',bg='white', width=20).grid(row=0,column=1)
    cur.execute('Select * from med')
    # for i in cur:
    #     if i[0]==sl2:
    #         Label(d,text=i[0]+'. '+i[0],bg='white').grid(row=0,column=1)
    c.commit()
    
def delt():
    global p,c,cur,d
    cur.execute("delete from med where sl_no=?",(sl2,))
    c.commit()
    ren()

def modify():    # Jendela edit
    global cur, c, accept, flag, att, up, n, name_, apt, st, col,col_n
    col=('', '', 'type', 'qty_left', 'cost', 'purpose')
    col_n=('', '', 'Type', 'Stock', 'Harga', 'Tujuan')
    flag='st'
    name_=''
    apt.destroy()
    n=[]
    cur.execute("select * from med")
    for i in cur:
        n.append(i[1])
    c.commit()
    
    st=Tk()
    st.title('EDIT STOK')    
    st.geometry("897x600")
    st.resizable(False, False)
    st.iconbitmap(r'medicine.ico')

    frame_menu = Frame(st, bd=5, bg="white" )
    frame_menu.place(width=897, height=600)
    judul = Label(st, text="Update Stok", bg="white", font=('Helvetica 15')).place(x=20, y=20)
    
    garis = Label(st, text="-"*30, fg="#068f1f", bg="white", font=('Helvetica 8 bold'))
    garis.place(x=20, y=50, height=5)
    frame_table = Frame(st, bg="#068f1f").place(x=10, y=100, width=500, height=350)
    def onvsb(*args):
        name_.yview(*args)
    def onmousewheel():
        name_.ywiew=('scroll',event.delta,'units')
        return 'break'
    cx=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    vsb.place(relx=1, rely=0, relheight=1, anchor='ne')
    name_=Listbox(st,width=25, bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set)
    cur.execute("select *from med")
    for i in cur:
        cx+=1
        name_.insert(cx,(str(i[0])+'.  '+str(i[1])))
        name_.place(x=120,y=110, width=300, height=160)
    c.commit()
    name_.bind('<MouseWheel>',onmousewheel)
    name_.bind('<<ListboxSelect>>', sel_mn)

    Label(st, text='Nama Obat: ', bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=15, y=180)
    Label(st, text='Ubah: ',bg="#068f1f", fg="white", font=('Helvetica 12')).place(x = 15, y = 300)
    att=Spinbox(st, values=col_n)
    att.place(x = 120, y = 300)
    up=Entry(st, width= 25)
    up.place(x = 270, y = 300)
    Button(st,width=13,text='UPDATE',bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command=save_mod).place(x =  550, y = 200)
    Button(st, width = 13, text="MAIN MENU", bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command = main_menu).place(x =  550, y = 100)
    Button(st,width=13,text='RESET', bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command=res).place(x =  550, y = 300)
    Button(st,width=13,text='DATA',bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command=show_val).place(x =  550, y = 400)
   
    st.mainloop()

def res():
    global st, up
    up=Entry(st, width= 25)
    up.place(x = 270, y = 300)

def sel_mn(e):
    global n,name_, name_mn, sl, c, cur
    name_mn=''
    p=name_.curselection()
    print (p)
    x=0
    sl=''
    cur.execute("select * from med")
    for i in cur:
        print (x, p[0])
        if x==int(p[0]):
            sl=i[0]
            break
        x+=1
    c.commit()
    print (sl)
    name_nm=n[int(sl)]
    print (name_nm)
    
def show_val():
    global st, name_mn, att, cur, c, col, col_n, sl, a
    # for i in range(3):
    #     Label(st,width=20, text='                         ').grid(row=5,column=i)
    cur.execute("select * from med")
    for i in cur:
        for j in range(6):
            if att.get()==col_n[j] and sl==i[0]:
                Label(st, text=str(i[0]), bg="#068f1f", fg="white", font=('Helvetica 12')).place(x = 130, y = 400)
                Label(st, text=str(i[1]), bg="#068f1f", fg="white", font=('Helvetica 12')).place(x = 200, y = 400)
                Label(st, text=str(i[j]), bg="#068f1f", fg="white", font=('Helvetica 12')).place(x = 300, y = 400)
    c.commit()

def save_mod(): #simpan sata baru
    global cur, c, att, name_mn, st, up, col_n, sl 
    for i in range(6):
        if att.get()==col_n[i]:
            a=col[i]
    sql="update med set '%s' = '%s' where sl_no = '%s'" % (a,up.get(),sl)
    cur.execute(sql)
    c.commit()
    Label(st, text='Updated!', bg="#068f1f", fg="white", font=('Helvetica 12')).place(x = 420, y = 150)
    
    
def stock():    #tambah produk
    global cur, c, columns, accept, flag, sto, apt
    apt.destroy()
    flag='sto'
    accept=['']*10
    
    sto=Tk()
    sto.title('Tambah Produk')
    sto.geometry("800x650")
    sto.iconbitmap(r'medicine.ico')

    frame_menu = Frame(sto, bd=5, bg="white" )
    frame_menu.place(width=800, height=650)

    judul = Label(sto, text="Inventory Obat", bg="white", font=('Helvetica 15')).place(x=20, y=20)
    garis = Label(sto, text="-------------------------------------", fg="#068f1f", bg="white", font=('Helvetica 8 bold'))
    garis.place(x=20, y=50, height=5)
    for i in range(1,len(columns)):
        label_nama = Label(sto, text="Nama Obat", font=('Helvetica 12'), bg="white").place(x=20, y=110)
        panel_nama = Frame(sto, bg="#068f1f").place(x=150, y=105, width=380, height=30)
        accept[1] = input_nama = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[1].place(x=152, y=107, width=376, height=26)

        label_jenis = Label(sto, text="Jenis Obat", font=('Helvetica 12'), bg="white").place(x=20, y=170)
        panel_jenis = Frame(sto, bg="#068f1f").place(x=150, y=165, width=380, height=30)
        accept[2]= input_jenis = ttk.Combobox(sto, font=('Helvetica 12'),state='readonly', values =  ["Tablet", "Kapsul", "Cair"])
        accept[2].place(x=152, y=167, width=376, height=26)

        label_stok = Label(sto, text="Stok Obat", font=('Helvetica 12'), bg="white").place(x=20, y=230)
        panel_stok = Frame(sto, bg="#068f1f").place(x=150, y=225, width=380, height=30)
        accept[3]= input_stok = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[3].place(x=152, y=227, width=376, height=26)

        label_harga = Label(sto, text="Harga Obat", font=('Helvetica 12'), bg="white").place(x=20, y=290)
        panel_harga = Frame(sto, bg="#068f1f").place(x=150, y=285, width=380, height=30)
        accept[4]=  input_harga = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[4].place(x=152, y=287, width=376, height=26)

        label_tujuan = Label(sto, text="Tujuan Obat", font=('Helvetica 12'), bg="white").place(x=20, y=350)
        panel_tujuan = Frame(sto, bg="#068f1f").place(x=150, y=345, width=380, height=30)
        accept[5]= input_tujuan = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[5].place(x=152, y=347, width=376, height=26)

    #button dibawah
    button_submit = Button(sto, text='SIMPAN', bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command=submit)
    button_submit.place(x=600, y=100, width=125, height=50)

    button_menu_barang = Button(sto, text='MAIN MENU', bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command=main_menu)
    button_menu_barang.place(x=600, y=325, width=125, height=50)

    #Table di bawah
    frame_table = Frame(sto, bg="#068f1f").place(x=20, y=425, width=760, height=217)

    label_nama_tbl = Label(sto, text="Nama Obat", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=40,y=435)
    

    label_jenis_tbl = Label(sto, text="Jenis Obat", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=250,y=435)
    

    label_stok_tbl = Label(sto, text="Stok", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=370,y=435)
    

    label_harga_tbl = Label(sto, text="Harga", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=460,y=435)
    

    label_tujuan_tbl = Label(sto, text="Tujuan Obat", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=550,y=435)
    

    ref()

    sto.mainloop()

def ref(): # membuat multi-listbox manual untuk menujukkan database 
    global sto, c, cur
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)
        lb4.yview(*args)
        lb5.yview(*args)
        # lb6.yview(*args)

    def onmousewheel():
        lb1.ywiew=('scroll',event.delta,'units')
        lb2.ywiew=('scroll',event.delta,'units')
        lb3.ywiew=('scroll',event.delta,'units')
        lb4.ywiew=('scroll',event.delta,'units')
        lb5.ywiew=('scroll',event.delta,'units')
        # lb6.ywiew=('scroll',event.delta,'units')
        
        return 'break'
    cx=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(sto,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set)
    lb2=Listbox(sto,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set)
    lb3=Listbox(sto,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set,width=10)
    lb4=Listbox(sto,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set,width=7)
    lb5=Listbox(sto,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set,width=25)
    # lb6=Listbox(sto,yscrollcommand=vsb.set,width=37)
    vsb.place(relx=1, rely=0, relheight=1, anchor='ne')
    lb1.place(x=40,y=465, width=190, height=160)
    lb2.place(x=250,y=465, width=100, height=160)
    lb3.place(x=370,y=465, width=70, height=160)
    lb4.place(x=460,y=465, width=70, height=160)
    lb5.place(x=550,y=465, width=210, height=160)
    # lb6.grid(row=15,column=5)
    lb1.bind('<MouseWheel>',onmousewheel)
    lb2.bind('<MouseWheel>',onmousewheel)
    lb3.bind('<MouseWheel>',onmousewheel)
    lb4.bind('<MouseWheel>',onmousewheel)
    lb5.bind('<MouseWheel>',onmousewheel)
    # lb6.bind('<MouseWheel>',onmousewheel)
    cur.execute("select *from med")
    for i in cur:
        cx+=1
        seq=(str(i[0]),str(i[1]))
        lb1.insert(cx,'. '.join(seq))
        lb2.insert(cx,i[2])
        lb3.insert(cx,i[3])
        lb4.insert(cx,i[4])
        lb5.insert(cx,i[5])
        # lb6.insert(cx,i[6]+'    '+i[7]+'    '+i[8])
    c.commit()

def reset():
    global sto, accept
    for i in range(1,len(columns)):
        label_nama = Label(sto, text="Nama Obat", font=('Helvetica 12'), bg="white").place(x=20, y=110)
        panel_nama = Frame(sto, bg="#068f1f").place(x=150, y=105, width=380, height=30)
        accept[1] = input_nama = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[1].place(x=152, y=107, width=376, height=26)

        label_jenis = Label(sto, text="Jenis Obat", font=('Helvetica 12'), bg="white").place(x=20, y=170)
        panel_jenis = Frame(sto, bg="#068f1f").place(x=150, y=165, width=380, height=30)
        accept[2]= input_jenis = ttk.Combobox(sto, font=('Helvetica 12'),state='readonly', values =  ["Tablet", "Kapsul", "Cair"])
        accept[2].place(x=152, y=167, width=376, height=26)

        label_stok = Label(sto, text="Stok Obat", font=('Helvetica 12'), bg="white").place(x=20, y=230)
        panel_stok = Frame(sto, bg="#068f1f").place(x=150, y=225, width=380, height=30)
        accept[3]= input_stok = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[3].place(x=152, y=227, width=376, height=26)

        label_harga = Label(sto, text="Harga Obat", font=('Helvetica 12'), bg="white").place(x=20, y=290)
        panel_harga = Frame(sto, bg="#068f1f").place(x=150, y=285, width=380, height=30)
        accept[4]=  input_harga = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[4].place(x=152, y=287, width=376, height=26)

        label_tujuan = Label(sto, text="Tujuan Obat", font=('Helvetica 12'), bg="white").place(x=20, y=350)
        panel_tujuan = Frame(sto, bg="#068f1f").place(x=150, y=345, width=380, height=30)
        accept[5]= input_tujuan = Entry(sto, bg="white", font=('Helvetica 12'))
        accept[5].place(x=152, y=347, width=376, height=26)
    
def submit(): #submit stok baru
    global accept, c, cur, columns, sto, acp
    # prev=time.clock()
    # acp= accept[2]
    x=['']*10
    cur.execute("select * from med")
    for i in cur:
        y=int(i[0])
    
    for i in range(1,6):
        x[i]=accept[i].get()
    sql="insert into med values('%s','%s','%s','%s','%s','%s')" % (y+1,x[1],x[2],x[3],x[4],x[5])
   

    cur.execute(sql)
    cur.execute("select * from med")
    c.commit() 
    ref()
    reset()

    top=Tk()
    top.iconbitmap(r'medicine.ico')
    Label(top,width=20, text='Success!').pack()
    top.mainloop()
    main_menu()
   

def chk(): #chek stok baru apakah sudah tersedia
    global cur, c, accept, sto
    cur.execute("select * from med")
    for i in cur:
        if accept[6].get()==i[6] and i[1]==accept[1].get():
            sql="update med set qty_left = '%s' where name = '%s'" % (str(int(i[3])+int(accept[3].get())),accept[1].get())
            cur.execute(sql)
            c.commit()
            top=Tk()
            Label(top,width=20, text='Modified!').pack()
            top.mainloop()
            main_menu()
        else:
            submit()
    c.commit()

    
def billing(): #pembayran
    global c, cur, apt, flag, t, name, name1, add, st, names, qty, sl, qtys, vc_id, n, namee, lb1
    t=0
    vc_id=''
    names=[]
    qty=[]
    sl=[]
    n=[]
    qtys=['']*10
    cur.execute("select *from med")
    for i in cur:
        n.append(i[1])
    c.commit()
    if flag=='st':
        st.destroy()
    else:
        apt.destroy()
    flag='st'
    st = Tk()
    st.geometry("700x500")
    st.resizable(False, False)
    st.iconbitmap(r'medicine.ico')
    st.title("Kasir")


    frame_menu = Frame(st, bd=5, bg="white" )
    frame_menu.place(width=700, height=500)

    judul = Label(st, text="Kasir", bg="white", font=('Helvetica 15')).place(x=20, y=20)
    garis = Label(st, text="-----------", fg="#068f1f", bg="white", font=('Helvetica 8 bold'))
    garis.place(x=20, y=50, height=5)

    label_jumlah_beli = Label(st, text="Jumlah Beli", font=('Helvetica 12'), bg="white").place(x=20, y=360)
    panel_jumlah_beli = Frame(st, bg="#068f1f").place(x=150, y=355, width=280, height=30)
    qtys = Entry(st, bg="white", font=('Helvetica 12'))
    qtys.place(x=152, y=357, width=276, height=26)

    label_total = Label(st, text="Total", font=('Helvetica 12'), bg="white").place(x=20, y=440)
    panel_total = Frame(st, bg="#068f1f").place(x=150, y=435, width=280, height=30)
    input_total = Entry(st, bg="white", font=('Helvetica 12')).place(x=152, y=437, width=276, height=26)

    #button dibawah
    button_bayar = Button(st, text='BAYAR', bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command = append2bill)
    button_bayar.place(x=515, y=180, width=125, height=50)
        
    button_menu_barang = Button(st, text='MAIN MENU', bg="#068f1f", fg="white", bd="3", font=('Helvetica 12'), command=main_menu)
    button_menu_barang.place(x=515, y=30, width=125, height=50)

    #Table di bawah
    frame_table = Frame(st, bg="#068f1f").place(x=20, y=100, width=410, height=217)

    label_nama_tbl = Label(st, text="Nama Obat", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=40,y=115)
    # Listbox(st, bg="white", font=('Helvetica 12')).place(x=40,y=140, width=190, height=160)

    label_stok_tbl = Label(st, text="Stok", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=250,y=115)
    # Listbox(st, bg="white", font=('Helvetica 12')).place(x=250,y=140, width=70, height=160)

    label_harga_tbl = Label(st, text="Harga", bg="#068f1f", fg="white", font=('Helvetica 12')).place(x=340,y=115)
  
    refresh()
    
    st.mainloop()

def refresh():
    global cur, c, st, lb1, lb2, lb3, vsb
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)

    def onmousewheel():
        lb1.ywiew=('scroll',event.delta,'units')
        lb2.ywiew=('scroll',event.delta,'units')
        lb3.ywiew=('scroll',event.delta,'units')
        return 'break'
    cx=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(st, width=25, bg="white", font=('Helvetica 12'), yscrollcommand=vsb.set)
    lb2=Listbox(st, width=25,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set)
    lb3=Listbox(st, width=25,bg="white", font=('Helvetica 12'),yscrollcommand=vsb.set)
    vsb.place(relx=1, rely=0, relheight=1, anchor='ne')
    lb1.place(x=40,y=140, width=190, height=160)
    lb2.place(x=250,y=140, width=80, height=160)
    lb3.place(x=340,y=140, width=80, height=160)
    lb1.bind('<MouseWheel>',onmousewheel)
    lb2.bind('<MouseWheel>',onmousewheel)
    lb3.bind('<MouseWheel>',onmousewheel)
    cur.execute("select *from med")
    for i in cur:
        cx+=1
        lb1.insert(cx,str(i[0])+'. '+str(i[1]))
        lb2.insert(cx,' '+str(i[3]))
        lb3.insert(cx,' Rp '+ str(i[4]))
    c.commit()
    lb1.bind('<<ListboxSelect>>', select_mn)

def select_mn(e): #pilih produk
    global st, lb1, n ,p, nm, sl1
    p=lb1.curselection()
    x=0
    sl1=''

    cur.execute("select * from med")
    for i in cur:
        if x==int(p[0]):
            sl1=int(i[0])
            break
        x+=1    
    c.commit()
    print (sl1)
    nm=n[x]
    print (nm)
    
def append2bill(): # append to the bill
    global st, names, nm , qty, sl,cur, c, sl1
    entryText = tk.StringVar()
    entryBayar = StringVar()
    entryKembalian = StringVar()
    sl.append(sl1)
    names.append(nm)
    qty.append(qtys.get())
    print (qty)
    print (sl[len(sl)-1],names[len(names)-1],qty[len(qty)-1])

    price=[0.0]*10
    q=0
    det=['','','','','','','','']
    det[2]=str(sl)
    for i in range(len(sl)):
        print (sl[i],' ',qty[i],' ',names[i])
    for k in range(len(sl)):
        cur.execute("select * from med where sl_no=?",(sl[k],))
        for i in cur:
            price[k]=int(qty[k])*float(i[4])
            print (qty[k],price[k])
            cur.execute("update med set qty_left=? where sl_no=?",(int(i[3])-int(qty[k]),sl[k]))
        c.commit()
    det[5]=str(random.randint(100,999))
    B='bill_'+str(det[5])+'.txt'
    total=0.00
    for i in range(10):
        if price[i] != '':
            total+=price[i]
    # cur.execute('insert into bills values("%s","%s","%s","%s","%s")',(det[0],det[1],det[2],det[3],det[4]))
    label_total = Label(st, text="Total", font=('Helvetica 12'), bg="white").place(x=20, y=440)
    panel_total = Frame(st, bg="#068f1f").place(x=150, y=435, width=280, height=30)
    input_total = Entry(st, bg="white", font=('Helvetica 12'),  textvariable=entryText).place(x=152, y=437, width=276, height=26)
    entryText.set(total)
  
    refresh()
    
    c.commit()

def show_rev(): # opens revenue window-----------------------------------------------------------------------TOTAL REVENUE
    global c, cur, flag,rev
    apt.destroy()
    cb=('cus_name','cus_add','items','Total_cost','bill_dt','bill_no','bill','val_id')
    flag='rev'
    rev=Tk()
    total=0.0
    today=str(time.localtime()[2])+'/'+str(time.localtime()[1])+'/'+str(time.localtime()[0])
    Label(rev,text='Today: '+today).grid(row=0,column=0)
    cur.execute('select * from bills')
    for i in cur:
        if i[4]==today:
            total+=float(i[3])
    print (total)
    Label(rev,width=22,text='Total revenue: Rp '+str(total), bg='black',fg='white').grid(row=1,column=0)
    cx=0
    vsb=Scrollbar(orient='vertical')
    lb1=Listbox(rev,width=25, yscrollcommand=vsb.set)
    vsb.grid(row=2,column=1,sticky=N+S)
    lb1.grid(row=2,column=0)
    vsb.config( command = lb1.yview )
    cur.execute("select * from bills")
    for i in cur:
        if i[4]==today:
            cx+=1
            lb1.insert(cx,'Bill No.: '+str(i[5])+'    : Rp '+str(i[3]))
    c.commit()
    Button(rev,text='Main Menu',command=main_menu).grid(row=15,column=0)
    rev.mainloop()
    
def again():    #for login window-----------------------------------------------------------------------------LOGIN WINDOW
    global input_username, input_password, flag, root, apt
    if flag=='apt':
        apt.destroy()
    root = Tk()
    root.iconbitmap(r'medicine.ico')
    root.title("Login")
    root.geometry("330x500")
    root.resizable(False, False)

    # username = StringVar()
    # password = StringVar()

    frame_menu = Frame(root, bd=5, bg="white" )
    frame_menu.place(width=330, height=500)

    gambar_logo = PhotoImage(file="F:/visual/final/logota.png")  #kalo nda muncul backgroundnya, sesuikan lokasi "Login.png"
    logo = Label(root, image=gambar_logo, bg="#04a216").place(x="133",y=35)

    gambar = PhotoImage(file="F:/visual/final/Login-fix.png")  #kalo nda muncul backgroundnya, sesuikan lokasi "Login.png"
    background = Label(frame_menu, image=gambar)
    background.pack(expand=True)

    label_judul2 = Label(frame_menu, text="SIGN-IN", font=('Calibri',14), bg="#04a216", fg="white")
    label_judul2.place(height=20, x=125, y=100)

    label_username = Label(frame_menu, text="Username", font=('Calibri',12), bg="#04a216", fg="white")
    label_username.place(height=40,x=20,y=150)

    input_username = Entry(frame_menu, bg="#ffffdf", font=('Calibri',12))
    input_username.place(x=23,y=190,height=20,width=273)

    label_password = Label(frame_menu, text="Password", font=('Calibri',12), bg="#04a216", fg="white")
    label_password.place(height=40,x=20, y=220)

    input_password = Entry(frame_menu, bg="#ffffdf", font=('Calibri',12), show="*")
    input_password.place(x=23,y=260,height=20,width=273)

    button_hitung = Button(frame_menu, bg="#02750f", fg="white", text="Login", font=('Calibri',14), command = check)
    button_hitung.place(x=23,y=310,height=30,width=273)

    #Untuk sementara masih ini dlu. nanti kalo mau tambah fungsi register, ku tambahkan icon regis

    label_password = Label(frame_menu, text="Created By Kelompok 8", font=('Calibri',10), bg="#fefefe", fg="black")
    label_password.place(height=40, y=458)

    root.mainloop()

def open_gagal():
    # flag='exp'
    # open_gagal.destroy()
    top=Tk()
    Label(top,width=50, text='Username atau Password Salah !').pack()
    top.mainloop()
    
def check():    #mengecek username dan password
    global input_username,input_password, login, l, root, exp
    u=input_username.get()
    p=input_password.get()
    l.execute("select * from log")
    for i in l:     
        if i[0]==u and i[1]==p and u=='admin':
            root.destroy()
            open_win()
        # else :
        #     top=Tk()
        #     Label(top,width=50, text='Username atau Password Salah !').pack()
        #     top.mainloop()
        #     root.destroy()
    login.commit()

def main_menu(): #controls open and close of main menu window----------------------------------------RETURN TO MAIN MENU
    global sto, apt, flag, root, st, val, exp, st1,rev
    if flag=='sto':
        sto.destroy()
    if flag=='rev':
        rev.destroy()
    elif flag=='st':
        st.destroy()
    elif flag=='st1':
        st1.destroy()
    elif flag=='val':
        val.destroy()
    elif flag=='exp':
        open_gagal.destroy()
    elif flag=='d':
        d.destroy()
    open_win()    

again()

