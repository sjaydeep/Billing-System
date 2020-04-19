from tkinter import*
import math,random,os
from tkinter import messagebox



class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x7000+0+0")
        # root.geometry('200x150') 

        self.root.title("Billing Software")
        bg_color="#006699"
        #bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        
        #==============================variable=====================================
        #==============================cosmetics====================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()

        #=============================Grocery===========================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        

        #==============================coldDrinks===========================
        self.mazaa=IntVar()
        self.cock=IntVar()
        self.frooty=IntVar()
        self.thumbsUp=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #==============================Total product price and tax====================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocry_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #==============================Customer=================================
        self.c_name=StringVar()
        self.c_phn=StringVar()

        x=random.randint(1000,9999)
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        
        #=============================Customer Detail Frame==========================
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        c_name_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        c_name_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        c_phn_lbl=Label(F1,text="Phone number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        c_php_txt=Entry(F1,width=15,textvariable=self.c_phn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_lbl=Label(F1,text="Bill Number ",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)



        #===================================cosmetic Frame ================================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl=Label(F2,text="Face Cream", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl=Label(F2,text="Face Wash", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl=Label(F2,text="hair Spray", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F2,text="Hair Gel", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Lotion", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        
        #===================================Grocery Frame ================================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery Items",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=335,y=180,width=325,height=380)

        sugar_lbl=Label(F3,text="Sugar", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        rice_lbl=Label(F3,text="Rice", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        oil_lbl=Label(F3,text="Food Oil", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        oil_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        daal_lbl=Label(F3,text="Daal", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        wheat_lbl=Label(F3,text="Wheet", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #===================================Cold Drink Frame ================================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=665,y=180,width=325,height=380)

        maaza_lbl=Label(F4,text="Maaza", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maaza_txt=Entry(F4,width=10,textvariable=self.mazaa,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cock_lbl=Label(F4,text="Cock", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cock_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        frooty_lbl=Label(F4,text="Frooty", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooty_txt=Entry(F4,width=10,textvariable=self.frooty,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        thumbs_lbl=Label(F4,text="Thumbs Up", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        thumbs_txt=Entry(F4,width=10,textvariable=self.thumbsUp,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        limca_lbl=Label(F4,text="Limca", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sprite_lbl=Label(F4,text="Sprite", font=("times new roman",16,"bold"), bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #==========================Bill Area=============================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=350,height=380)

        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        #======================Button Frame==========================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="white",font=("times new romans",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new romans",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new romans",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_lbl=Label(F6,text="Cosmetics Tax",bg=bg_color,fg="white",font=("times new romans",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new romans",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocry_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new romans",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=790,height=105,width=540)

        Total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).grid(row=0,column=0,padx=2,pady=5)
        Generate_Bill=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=9, width=10, font=("arial 14 bold")).grid(row=0,column=1,padx=2,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).grid(row=0,column=2,padx=2,pady=5)
        Exit_btn=Button(btn_F,text="Exit", command=self.Exit_app,bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).grid(row=0,column=3,padx=2,pady=5)
        self.welcome_bill()


    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_g_p=self.gel.get()*140
        self.c_sp_p=self.spray.get()*180
        self.c_l_p=self.lotion.get()*180

        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_g_p+
            self.c_l_p+
            self.c_sp_p
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*80
        self.g_d_p=self.daal.get()*60
        self.g_fo_p=self.food_oil.get()*180
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*40
        self.g_t_p=self.tea.get()*150

        self.total_grocery_price=float(
            self.g_r_p+
            self.g_d_p+
            self.g_fo_p+
            self.g_w_p+
            self.g_s_p+
            self.g_t_p
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocry_tax.set("Rs. "+str(self.g_tax))


        self.cd_m_p=self.mazaa.get()*40
        self.cd_c_p=self.cock.get()*40
        self.cd_t_p=self.thumbsUp.get()*40
        self.cd_s_p=self.sprite.get()*40
        self.cd_l_p=self.limca.get()*40
        self.cd_f_p=self.frooty.get()*15

        self.total_cold_drink_price=float(
            self.cd_m_p+
            self.cd_c_p+
            self.cd_t_p+
            self.cd_s_p+
            self.cd_l_p+
            self.cd_f_p
        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price+
                              self.c_tax+
                              self.g_tax+
                              self.cd_tax)
    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\tWelcome Food Code Retails\n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phn.get()}")
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,"\nProducts\t\t Qty\t\tPrice")
        self.txtarea.insert(END,"\n======================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phn.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","Products are must Purchase")
        else:
            self.welcome_bill()
            #======================cosmetics======================
            if self.soap.get()!=0:
                    self.txtarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            
            if self.face_cream.get()!=0:
                    self.txtarea.insert(END,f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.face_wash.get()!=0:
                    self.txtarea.insert(END,f"\nFace Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            if self.spray.get()!=0:
                    self.txtarea.insert(END,f"\nHair Spray\t\t{self.face_wash.get()}\t\t{self.c_sp_p}")

            if self.gel.get()!=0:
                    self.txtarea.insert(END,f"\nHair Gel\t\t{self.gel.get()}\t\t{self.c_g_p}")

            if self.lotion.get()!=0:
                    self.txtarea.insert(END,f"\nBody Lotion\t\t{self.lotion.get()}\t\t{self.c_l_p}")                        


    #======================grocery======================
            if self.rice.get()!=0:
                    self.txtarea.insert(END,f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            
            if self.daal.get()!=0:
                    self.txtarea.insert(END,f"\nDaal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.food_oil.get()!=0:
                    self.txtarea.insert(END,f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")

            if self.wheat.get()!=0:
                    self.txtarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.tea.get()!=0:
                    self.txtarea.insert(END,f"\nTea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            if self.sugar.get()!=0:
                    self.txtarea.insert(END,f"\nSugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")         


            #======================cold drink======================
            if self.mazaa.get()!=0:
                    self.txtarea.insert(END,f"\nMazza\t\t{self.mazaa.get()}\t\t{self.cd_m_p}")
            
            if self.cock.get()!=0:
                    self.txtarea.insert(END,f"\nCock\t\t{self.cock.get()}\t\t{self.cd_c_p}")

            if self.thumbsUp.get()!=0:
                    self.txtarea.insert(END,f"\nThumbs UP\t\t{self.thumbsUp.get()}\t\t{self.cd_t_p}")

            if self.sprite.get()!=0:
                    self.txtarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t\t{self.cd_s_p}")

            if self.limca.get()!=0:
                    self.txtarea.insert(END,f"\nLimca\t\t{self.limca.get()}\t\t{self.cd_l_p}")

            if self.frooty.get()!=0:
                    self.txtarea.insert(END,f"\nFrooty\t\t{self.frooty.get()}\t\t{self.cd_f_p}")         

            self.txtarea.insert(END,"\n--------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")

            if self.grocry_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocry_tax.get()}")

            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END,f"\nTotal Bill :\t\t\tRs .{self.Total_bill}")
            self.txtarea.insert(END,"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no.{self.bill_no.get()} Saved Successfully")

        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")


    def clear_data(self):
        op = messagebox.askyesno("Exit","Do you Want to Exit!")
        if op>0:    
            #==============================variable=====================================
            #==============================cosmetics====================================
            self.soap=set(0)
            self.face_cream=set(0)
            self.face_wash=set(0)
            self.spray=set(0)
            self.gel=set(0)
            self.lotion=set(0)

            #=============================Grocery===========================
            self.rice=set(0)
            self.food_oil=set(0)
            self.daal=set(0)
            self.wheat=set(0)
            self.sugar=set(0)
            self.tea=set(0)
            

            #==============================coldDrinks===========================
            self.mazaa=set(0)
            self.cock=set(0)
            self.frooty=set(0)
            self.thumbsUp=set(0)
            self.limca=set(0)
            self.sprite=set(0)

            #==============================Total product price and tax====================
            self.cosmetic_price=StringVar()
            self.grocery_price=StringVar()
            self.cold_drink_price=StringVar()

            self.cosmetic_tax=StringVar()
            self.grocry_tax=StringVar()
            self.cold_drink_tax=StringVar()

            #==============================Customer=================================
            self.c_name=StringVar()
            self.c_phn=StringVar()

            x=random.randint(1000,9999)
            self.bill_no=StringVar()
            self.bill_no.set(str(x))
            self.search_bill=StringVar()
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you Want to Exit!")
        if op>0:
            self.root.destroy()


root=Tk()
obj = Bill_App(root)
root.mainloop()