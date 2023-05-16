from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x700+0+0")
                self.root.title("Resturant Billing system")
                bg_color="light pink"
                
                title=Label(self.root,text="Anmol Resturant",bd=14,relief=GROOVE,bg=bg_color,fg="Black", font=("times new roman",30,"bold"),pady=2).pack(fill=X)
                #======variable===========
                #=======Veg menu=========
                self.kadhai_paneer=IntVar()
                self.chilli_paneer=IntVar()
                self.veg_chowmein=IntVar()  
                self.chola_bhatura=IntVar()
                self.veg_cheese_pizza=IntVar()
                self.Edli_sambar=IntVar()
                
                #======= NON Veg menu=========
                self.chicken_gravy=IntVar()
                self.chicken_lolipop=IntVar()
                self.chicken_swarma=IntVar()  
                self.chicken_chowmein=IntVar()
                self.chicken_cheese_pizza=IntVar()
                self.fish_fry=IntVar()
                
                #=======desserts=========
                self.strawberry_icecream=IntVar()
                self.Jalaebi=IntVar()
                self.Rasmalai=IntVar()  
                self.Fruit_custurd=IntVar()
                self.Gulab_jamun=IntVar()
                self.Vanilla_pastry=IntVar()
                
                #=======total price and tax variable=========
                self.VEG_PRICE=StringVar()
                self.DESSERT_PRICE=StringVar()
                self.NONVEG_PRICE=StringVar()  
                self.VEG_TAX=StringVar()
                self.NONVEG_TAX=StringVar()
                self.DESSERT_TAX=StringVar()
                
                
                
                #=======customer details=========
                self.c_name=StringVar()
                self.c_phone=StringVar()
                self.c_bill_no=StringVar()  
                x=random.randint(1000,9999)
                self.c_bill_no.set(str(x))
                self.search_bill=StringVar()
                
                
                
                #=================customer Detail Frame
                F1=LabelFrame(self.root,bd=10,text="Customer Details", font=("times new roman",20,"bold"),fg="black",bg=bg_color)
                F1.place(x=0,y=80,relwidth=1)
                
                cname_lbl=Label(F1,text="customer Name",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
                cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=6,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
                
                cphone_lbl=Label(F1,text="phone.No",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
                cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=6,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
                
                cbiilno_lbl=Label(F1,text="Bill Number",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
                cbillno_txt=Entry(F1,width=15,textvariable=self.c_bill_no,font="arial 15",bd=6,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)
                
                search_btn=Button(F1,text="Search",command=self.find_bill,bg="White",fg="black",bd=7,pady=15,width=10,font="arial 15 bold").grid(row=0,column=6,padx=5,pady=5)
                #bill_btn=Button(F1,text="save",command=self.find_bill,width=15,textvariable=self.search_bill,activeforeground="Black",activebackground = "green",bd=7,font=("arial 10 bold")).grid(row=0,column=6,padx=10,pady=10)
                #bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=6,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)
                #=======Veg menu=========
                F2=LabelFrame(self.root,bd=10,text="VEG MENU", font=("times new roman",18,"bold"),fg="black",bg=bg_color)
                F2.place(x=5,y=180,width=330,height=380)
                
                paneer_Lbl=Label(F2,text="kadhai paneer",font=("times new roman",16,"bold"),bg=bg_color,fg="Blue",bd=5).grid(row=0,column=0,padx=0,pady=0,sticky="w")
                paneer_txt=Entry(F2,width=15,textvariable=self.kadhai_paneer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
                
                chilli_Lbl=Label(F2,text="Chilli Paneer",font=("times new roman",16,"bold"),bg=bg_color,fg="Blue",bd=5).grid(row=1,column=0,padx=0,pady=0,sticky="w")
                chilli_txt=Entry(F2,width=15,textvariable=self.chilli_paneer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
                
                chowmein_Lbl=Label(F2,text="Veg Chowmein",font=("times new roman",16,"bold"),bg=bg_color,fg="Blue",bd=5).grid(row=2,column=0,padx=0,pady=0,sticky="w")
                chowmein_txt=Entry(F2,width=15,textvariable=self.veg_chowmein,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
                
                chola_Lbl=Label(F2,text="Chola bhatura",font=("times new roman",16,"bold"),bg=bg_color,fg="Blue",bd=5).grid(row=3,column=0,padx=0,pady=0,sticky="w")
                chola_txt=Entry(F2,width=15,textvariable=self.chola_bhatura,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
                
                pizza_Lbl=Label(F2,text="Veg Cheese Pizza",font=("times new roman",16,"bold"),bg=bg_color,fg="Blue",bd=5).grid(row=4,column=0,padx=0,pady=0,sticky="w")
                pizza_txt=Entry(F2,width=15,textvariable=self.veg_cheese_pizza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                
                Edli_Lbl=Label(F2,text="Edli sambar",font=("times new roman",16,"bold"),bg=bg_color,fg="Blue",bd=5).grid(row=5,column=0,padx=0,pady=0,sticky="w")
                Edli_txt=Entry(F2,width=15,textvariable=self.Edli_sambar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
                
                
                #=======Non Veg menu=========
                F3=LabelFrame(self.root,bd=10,text="NON VEG MENU", font=("times new roman",18,"bold"),fg="black",bg=bg_color)
                F3.place(x=340,y=180,width=330,height=380)
                
                Chicken_Lbl=Label(F3,text="Chicken Gravy ",font=("times new roman",16,"bold"),bg=bg_color,fg="red").grid(row=0,column=0,padx=10,pady=10,sticky="w")
                chicken_txt=Entry(F3,width=15,textvariable=self.chicken_gravy,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
                
                lolipop_Lbl=Label(F3,text="Chicken Lolipop",font=("times new roman",16,"bold"),bg=bg_color,fg="red").grid(row=1,column=0,padx=10,pady=10,sticky="w")
                lolipop_txt=Entry(F3,width=15,textvariable=self.chicken_lolipop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
                
                swarma_Lbl=Label(F3,text="Chicken Swarma",font=("times new roman",16,"bold"),bg=bg_color,fg="red").grid(row=2,column=0,padx=10,pady=10,sticky="w")
                swarma_txt=Entry(F3,width=15,textvariable=self.chicken_swarma,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
                
                chick_Lbl=Label(F3,text="Chicken chowmein",font=("times new roman",16,"bold"),bg=bg_color,fg="red").grid(row=3,column=0,padx=10,pady=10,sticky="w")
                chick_txt=Entry(F3,width=15,textvariable=self.chicken_chowmein,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
                
                cheese_Lbl=Label(F3,text="Chicken Cheese Pizza",font=("times new roman",16,"bold"),bg=bg_color,fg="red").grid(row=4,column=0,padx=10,pady=10,sticky="w")
                cheese_txt=Entry(F3,width=15,textvariable=self.chicken_cheese_pizza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                
                fish_Lbl=Label(F3,text="Fish Fry",font=("times new roman",16,"bold"),bg=bg_color,fg="red").grid(row=5,column=0,padx=10,pady=10,sticky="w")
                fish_txt=Entry(F3,width=15,textvariable=self.fish_fry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
                
                
                
                #=======Dessert=========
                F4=LabelFrame(self.root,bd=10,text="DESSERTS", font=("times new roman",18,"bold"),fg="black",bg=bg_color)
                F4.place(x=670,y=180,width=330,height=380)
                
                cream_Lbl=Label(F4,text="Strawberry icecream",font=("times new roman",16,"bold"),bg=bg_color,fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
                cream_txt=Entry(F4,width=15,textvariable=self.strawberry_icecream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
                
                jilabi_Lbl=Label(F4,text="Jalaebi",font=("times new roman",16,"bold"),bg=bg_color,fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
                jilabi_txt=Entry(F4,width=15,textvariable=self.Jalaebi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
                
                rasmalai_Lbl=Label(F4,text="Rasmalai",font=("times new roman",16,"bold"),bg=bg_color,fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
                rasmalai_txt=Entry(F4,width=15,textvariable=self.Rasmalai,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
                
                custurd_Lbl=Label(F4,text="Fruit custurd",font=("times new roman",16,"bold"),bg=bg_color,fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
                custurd_txt=Entry(F4,width=15,textvariable=self.Fruit_custurd,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
                
                jamun_Lbl=Label(F4,text="Gulab Jamun",font=("times new roman",16,"bold"),bg=bg_color,fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
                jamun_txt=Entry(F4,width=15,textvariable=self.Gulab_jamun,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                
                Vanilla_Lbl=Label(F4,text="Vanilla pastry",font=("times new roman",16,"bold"),bg=bg_color,fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
                vanilla_txt=Entry(F4,width=15,textvariable=self.Vanilla_pastry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
                
                #====Bill area====
                F5=LabelFrame(self.root,bd=10,relief=GROOVE)
                F5.place(x=1010,y=180,width=515,height=380)
                bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
                scrol_y=Scrollbar(F5,orient=VERTICAL)
                self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.txtarea.yview)
                self.txtarea.pack()
                
                #=======Button frame======
                F6=F4=LabelFrame(self.root,bd=10,text="Bill Menu", font=("times new roman",18,"bold"),fg="black",bg=bg_color)
                F6.place(x=0,y=560,relwidth=1,height=235)
                m1_lbl=Label(F6,text="TOTAL VEG PRICE",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
                m1_txt=Entry(F6,width=15,textvariable=self.VEG_PRICE,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=2)
                
                m2_lbl=Label(F6,text="TOTAL NONVEG PRICE",bg=bg_color,font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
                m2_txt=Entry(F6,width=15,textvariable=self.NONVEG_PRICE,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=2)
                
                m3_lbl=Label(F6,text="TOTAL DESSERT PRICE",bg=bg_color,font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
                m3_txt=Entry(F6,width=15,textvariable=self.DESSERT_PRICE,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=2)
                
                c1_lbl=Label(F6,text="VEG TAX",bg=bg_color,bd=5,font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
                c1_txt=Entry(F6,width=15,textvariable=self.VEG_TAX,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=2)
                
                c2_lbl=Label(F6,text="NONVEG TAX",bg=bg_color,bd=5,font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
                c2_txt=Entry(F6,width=15,textvariable=self.NONVEG_TAX,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=2)
                
                c3_lbl=Label(F6,text="DESSERT TAX",bg=bg_color,bd=5,font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
                c3_txt=Entry(F6,width=15,textvariable=self.DESSERT_TAX,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=2)
                
                btn_F=Frame(F6,bd=7,relief=GROOVE)
                btn_F.place(x=740,width=750,height=205)
                
                total_btn=Button(btn_F,command=self.total,text="Total",bg=bg_color,fg="black",bd=7,pady=15,width=15,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
                Gbill_btn=Button(btn_F,text="GENERATE BILL",command=self.bill_area,bg=bg_color,fg="black",bd=7,pady=15,width=15,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
                clear_btn=Button(btn_F,text="CLEAR",command=self.clear_data,bg=bg_color,fg="black",bd=7,pady=15,width=15,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
                Exit_btn=Button(btn_F,text="EXIT",command=self.Exit_app,bg=bg_color,fg="black",bd=7,pady=15,width=15,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
                #search_btn=Button(btn_F,text="Search",command=self.find_bill,bg=bg_color,fg="black",bd=7,pady=15,width=10,font="arial 12 bold").grid(row=0,column=4,padx=5,pady=5)
                self.welcome_bill()
                
                
        def total(self):
                self.v_k_p =self.kadhai_paneer.get()*120
                self.v_c_p=self.chilli_paneer.get()*80
                self.v_c=self.veg_chowmein.get()* 100
                self.v_c_b=self.chola_bhatura.get()*90
                self.v_c_pz=self.veg_cheese_pizza.get()*220
                self.v_e_s=self.Edli_sambar.get()*60
                
                self.total_veg_price=float(
                                            self.v_k_p +
                                            self.v_c_p+
                                            self.v_c+
                                            self.v_c_b+
                                            self.v_c_pz+
                                            self.v_e_s
                                         )
                        
                self.VEG_PRICE.set("Rs. " +str(self.total_veg_price))                
                self.V_tax=round((self.total_veg_price*0.03),2)
                self.VEG_TAX.set("Rs. "+str( self.V_tax))
                
                self.c_g=self.chicken_gravy.get()*180
                self.c_l=self.chicken_lolipop.get()*120
                self.c_s=self.chicken_swarma.get()*140
                self.c_c=self.chicken_chowmein.get()*130
                self.c_c_p=self.chicken_cheese_pizza.get()*260
                self.f_f=self.fish_fry.get()*100
                
                
                
                self.total_NON_veg_price=float(
                                                self.c_g+
                                                self.c_l+
                                                self.c_s +
                                                self.c_c+
                                                self.c_c_p+
                                                self.f_f
                                               )
                        
                self.NONVEG_PRICE.set("Rs. " +str(self.total_NON_veg_price))
                self.NV_tax=round((self.total_NON_veg_price*0.06),2)
                self.NONVEG_TAX.set("Rs. "+str( self.NV_tax))
                
                self.s_i=self.strawberry_icecream.get()*50
                self.s_j=self.Jalaebi.get()*90
                self.R=self.Rasmalai.get()*60
                self.F_c=self.Fruit_custurd.get()*80
                self.G_j=self.Gulab_jamun.get()*40
                self.V_p=self.Vanilla_pastry.get()*70
                
                
                self.total_DESSERT_price=float(
                                                self.s_i+
                                                self.s_j+
                                                self.R+
                                                self.F_c+
                                                self.G_j+
                                                self.V_p
                                                )
                 
                 
                self.DESSERT_PRICE.set("Rs. " +str(self.total_DESSERT_price))
                self.D_tax=round((self.total_DESSERT_price*0.01),2)
                self.DESSERT_TAX.set("Rs. "+str(self.D_tax ) )      
                
                self.Total_bill=float(self.total_veg_price+
                              self.total_NON_veg_price+
                              self.total_DESSERT_price+self.V_tax+self.NV_tax+self.D_tax)
                
        def welcome_bill(self):
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,"\tWelcome Anmol Resturant")
                self.txtarea.insert(END,f"\nBill Number : {self.c_bill_no.get()} ")
                self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
                self.txtarea.insert(END,f"\nCustomer Phone Number: {self.c_phone.get()}")
                self.txtarea.insert(END,f"\n===========================================================")
                self.txtarea.insert(END,f"\nProduts\t\t\tQuantity\t\t\tPrice")
                self.txtarea.insert(END,f"\n===========================================================")
                
        def bill_area(self):
                if self.c_name.get()=="" or self.c_phone.get()=="":
                     messagebox.showerror("Error","Customer details are must")
                elif self.VEG_PRICE.get()=="Rs.0.0" and self.NONVEG_PRICE.get()=="Rs.0.0" and self.DESSERT_PRICE.get()=="Rs.0.0":
                      messagebox.showerror("Error","No food purchased")
                else:
                        self.welcome_bill()
                #=======veg menu =======
                if self.kadhai_paneer.get()!=0:
                        self.txtarea.insert(END,f"\nkadhai paneer\t\t\t{self.kadhai_paneer.get()}\t\t\t{self.v_k_p}")        
                if self.chilli_paneer.get()!=0:
                        self.txtarea.insert(END,f"\nChilli Paneer\t\t\t{self.chilli_paneer.get()}\t\t\t{self.v_c_p}")        
                if self.veg_chowmein.get()!=0:
                        self.txtarea.insert(END,f"\nVeg Chowmein\t\t\t{self.veg_chowmein.get()}\t\t\t{self.v_c}")        
                if self.chola_bhatura.get()!=0:
                        self.txtarea.insert(END,f"\nChola bhatura\t\t\t{self.chola_bhatura.get()}\t\t\t{self.v_c_b}")        
                if self.veg_cheese_pizza.get()!=0:
                        self.txtarea.insert(END,f"\nVeg Cheese Pizza\t\t\t{self.veg_cheese_pizza.get()}\t\t\t{self.v_c_pz}")        
                if self.Edli_sambar.get()!=0:
                        self.txtarea.insert(END,f"\nEdli sambar\t\t\t{self.Edli_sambar.get()}\t\t\t{self.v_e_s}")        
                
                
                #=======nonveg menu =======
                if self.chicken_gravy.get()!=0:
                        self.txtarea.insert(END,f"\nchicken gravy\t\t\t{self.chicken_gravy.get()}\t\t\t{self.c_g}")        
                if self.chicken_lolipop.get()!=0:
                        self.txtarea.insert(END,f"\nChicken lolipop\t\t\t{self.chicken_lolipop.get()}\t\t\t{self.c_l}")        
                if self.chicken_swarma.get()!=0:
                        self.txtarea.insert(END,f"\nchicken swarma\t\t\t{self.chicken_swarma.get()}\t\t\t{self.c_s}")        
                if self.chicken_chowmein.get()!=0:
                        self.txtarea.insert(END,f"\nChicken chowmein\t\t\t{self.chicken_chowmein.get()}\t\t\t{self.c_c}")        
                if self.chicken_cheese_pizza.get()!=0:
                        self.txtarea.insert(END,f"\nchicken cheese pizza\t\t\t{self.chicken_cheese_pizza.get()}\t\t\t{self.c_c_p}")        
                if self.fish_fry.get()!=0:
                        self.txtarea.insert(END,f"\nFish fry\t\t\t{self.fish_fry.get()}\t\t\t{self.f_f}")        
                
                
                #=======dessert menu =======
                if self.strawberry_icecream.get()!=0:
                        self.txtarea.insert(END,f"\nstrawberry_icecream\t\t\t{self.strawberry_icecream.get()}\t\t\t{self.s_i}")        
                if self.Jalaebi.get()!=0:
                        self.txtarea.insert(END,f"\nJalaebi\t\t\t{self.Jalaebi.get()}\t\t\t{self.s_j}")        
                if self.Rasmalai.get()!=0:
                        self.txtarea.insert(END,f"\nRasmalai\t\t\t{self.Rasmalai.get()}\t\t\t{self.R}")        
                if self.Fruit_custurd.get()!=0:
                        self.txtarea.insert(END,f"\nFruit_custurd\t\t\t{self.Fruit_custurd.get()}\t\t\t{self.F_c}")        
                if self.Gulab_jamun.get()!=0:
                        self.txtarea.insert(END,f"\nGulab_jamun\t\t\t{self.Gulab_jamun.get()}\t\t\t{self.G_j}")        
                if self.Vanilla_pastry.get()!=0:
                        self.txtarea.insert(END,f"\nVanilla_pastry\t\t\t{self.Vanilla_pastry.get()}\t\t\t{self.V_p}")        

                self.txtarea.insert(END,f"\n-----------------------------------------------------------")
                if self.VEG_TAX.get()!="Rs.0.0":
                     self.txtarea.insert(END,f"\n Veg Tax\t\t\t\t\t\t{self.VEG_TAX.get()}")
                if self.NONVEG_TAX.get()!="Rs.0.0":
                     self.txtarea.insert(END,f"\n NONVeg Tax\t\t\t\t\t\t{self.NONVEG_TAX.get()}")
                if self.DESSERT_TAX.get()!="Rs.0.0":
                             self.txtarea.insert(END,f"\n Dessert Tax\t\t\t\t\t\t{self.DESSERT_TAX.get()}")
                self.txtarea.insert(END,f"\n-----------------------------------------------------------")
                self.txtarea.insert(END,f"\n Total Bill : \t\t\t\t\t\t Rs.{str(self.Total_bill)}")
                self.txtarea.insert(END,f"\n-----------------------------------------------------------")
                self.save_bill()
        def save_bill(self):
                op=messagebox.askyesno("save Bill","Do you want to save the Bill?")
                if op>0:
                    self.bill_data=self.txtarea.get('1.0',END)
                    f1=open("bills/"+str(self.c_bill_no.get())+".txt","w")
                    f1.write(self.bill_data)
                    f1.close()
                    messagebox.showinfo("saved",f"Bill no. :{self.c_bill_no.get()} saved successfully ")
                else:
                    return
                
        def find_bill(self):
                present="no"
                for i in os.listdir("bills/"):
                        if i.split('.')[0] ==self.search_bill.get():
                                f1=open(f"bills/{i}","r")
                                self.txtarea.delete('1.0',END)
                                for d in f1:
                                   self.txtarea.insert(END,d)
                                f1.close()
                                present=="yes" 
                        if present=="no":
                                messagebox.showerror("Error","Invalid Bill no")
        
        def clear_data(self):
                op=messagebox.askyesno("clear","Do you really want to clear?")
                if op>0:
                #=======Veg menu=========
                    self.kadhai_paneer.set(0)
                self.chilli_paneer.set(0)
                self.veg_chowmein.set(0)  
                self.chola_bhatura.set(0)
                self.veg_cheese_pizza.set(0)
                self.Edli_sambar.set(0)
                
                #======= NON Veg menu=========
                self.chicken_gravy.set(0)
                self.chicken_lolipop.set(0)
                self.chicken_swarma.set(0)  
                self.chicken_chowmein.set(0)
                self.chicken_cheese_pizza.set(0)
                self.fish_fry.set(0)
                
                #=======desserts=========
                self.strawberry_icecream.set(0)
                self.Jalaebi.set(0)
                self.Rasmalai.set(0)  
                self.Fruit_custurd.set(0)
                self.Gulab_jamun.set(0)
                self.Vanilla_pastry.set(0)
                
                #=======total price and tax variable=========
                self.VEG_PRICE.set("")
                self.DESSERT_PRICE.set("")
                self.NONVEG_PRICE.set("")  
                self.VEG_TAX.set("")
                self.NONVEG_TAX.set("")
                self.DESSERT_TAX.set("")
                
                
                
                #=======customer details=========
                self.c_name.set("")
                self.c_phone.set("")
                self.c_bill_no.set("")  
                x=random.randint(1000,9999)
                self.c_bill_no.set(str(x))
                self.search_bill.set("")
                self.welcome_bill()
        
        
        def Exit_app(self):
                op=messagebox.askyesno("Exit","Do you really want to exit")
                if op>0:
                        self.root.destroy()
        
        
        
                                             
                
root=Tk()  
obj=Bill_App(root)
root.mainloop()
