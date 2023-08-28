from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1450x750+0+0")
        self.root.title("Restaurent Billing System")
        bgcolor = "#0D3AE1"
        title = Label(self.root,text="Restaurent Name",bd=12,relief=GROOVE,bg=bgcolor,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        # Customer Details        
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",bg="#770B89",font=("times new roman",20,"bold"))
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl = Label(F1,text="Customer Name :",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=30,pady=17)
        cname_txt = Entry(F1,width=20,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        cphone_lbl = Label(F1,text="Customer Phone No :",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=30,pady=17)
        cphone_txt = Entry(F1,width=15,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)
        c_bill_lbl = Label(F1,text="Customer Bill No :",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=30,pady=17)
        c_bill_txt = Entry(F1,width=15,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)
        bill_btn = Button(F1,text="Search",width=10,bd=7,fg="black",font=("times new roman",15,"bold")).grid(row=0,column=6)
        
        # Restaurent Menu 1. Fast-Food Menu
        F2 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Fast-Food Menu",bg="#CA0E2E",font=("times new roman",17,"bold"))
        F2.place(x=50,y=190,width=380,height=360)
        bath_lbl = Label(F2,text="Samosa",font=("times new roman",20,"bold"),fg="black").grid(row=0,column=0,padx=10,sticky="w")
        bath_txt = Entry(F2,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        kc_lbl = Label(F2,text="Kachori",font=("times new roman",20,"bold"),fg="black").grid(row=1,column=0,padx=10,sticky="w")
        kc_txt = Entry(F2,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        fj_lbl = Label(F2,text="Fafda-Jalebi",font=("times new roman",20,"bold"),fg="black").grid(row=2,column=0,padx=10,sticky="w")
        fj_txt = Entry(F2,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        sad_lbl = Label(F2,text="Sandwich",font=("times new roman",20,"bold"),fg="black").grid(row=3,column=0,padx=10,sticky="w")
        sad_txt = Entry(F2,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        pak_lbl = Label(F2,text="Bread Pakoda",font=("times new roman",20,"bold"),fg="black").grid(row=4,column=0,padx=10,sticky="w")
        pak_txt = Entry(F2,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        # Restaurent Menu 2. Chinese Menu
        F3 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Chinese Menu",bg="#327B21",font=("times new roman",17,"bold"),fg="white")
        F3.place(x=450,y=190,width=450,height=360)
        bath_lbl = Label(F3,text="Noodles",font=("times new roman",20,"bold"),fg="black").grid(row=0,column=0,padx=10,sticky="w")
        bath_txt = Entry(F3,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        piz_lbl = Label(F3,text="Chaumin Soop",font=("times new roman",20,"bold"),fg="black").grid(row=1,column=0,padx=10,sticky="w")
        piz_txt = Entry(F3,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        bir_lbl = Label(F3,text="Maggie",font=("times new roman",20,"bold"),fg="black").grid(row=2,column=0,padx=10,sticky="w")
        bir_txt = Entry(F3,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        sad_lbl = Label(F3,text="Manchurian",font=("times new roman",20,"bold"),fg="black").grid(row=3,column=0,padx=10,sticky="w")
        sad_txt = Entry(F3,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        pag_lbl = Label(F3,text="Tomato Soop",font=("times new roman",20,"bold"),fg="black").grid(row=4,column=0,padx=10,sticky="w")
        pag_txt = Entry(F3,width=10,font=("times new roman",20,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        # Bill Area.
        F4 =LabelFrame(self.root,bd=10,relief=GROOVE)
        F4.place(x=940,y=190,width=460,height=360)
        bill_title = Label(F4,text="Billing Area",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F4,orient=VERTICAL)
        self.txtarea = Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # Button Frame
        F5 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",bg="#FFFF00",font=("times new roman",17,"bold"),fg="black")
        F5.place(x=0,y=560,relwidth=1,height=180)
        l1 = Label(F5,text="Fast-Food Items",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        l1_txt = Entry(F5,width=10,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        l2 = Label(F5,text="Chinese-Food Items",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        l2_txt = Entry(F5,width=10,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        l3 = Label(F5,text="Total Items",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        l3_txt = Entry(F5,width=10,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c1_l1 = Label(F5,text="Total Fast-Food",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_l1_txt = Entry(F5,width=10,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)
        c2_l2 = Label(F5,text="Total Chinese-Food",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_l2_txt = Entry(F5,width=10,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)
        c3_l3 = Label(F5,text="Total Bill",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_l3_txt = Entry(F5,width=10,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)
        
        btn_F = Frame(F5,bd=7,relief=GROOVE)
        btn_F.place(x=640,width=785,height=130)
        total = Button(btn_F,text="Total",font=("times new roman",15,"bold"),bd=5,bg=bgcolor,fg="white",padx=15).grid(row=0,column=0,padx=10,pady=10)
        gen_Bill = Button(btn_F,text="Generate Bill",font=("times new roman",15,"bold"),bd=5,bg=bgcolor,fg="white",padx=15).grid(row=0,column=1,padx=10,pady=10)
        clear = Button(btn_F,text="Clear",font=("times new roman",15,"bold"),bd=5,bg=bgcolor,fg="white",padx=15).grid(row=0,column=2,padx=10,pady=10)
        exit = Button(btn_F,text="Exit",font=("times new roman",15,"bold"),bd=5,bg=bgcolor,fg="white",padx=15).grid(row=0,column=3,padx=10,pady=10)
root = Tk()
obj = Bill_App(root)
root.mainloop()
