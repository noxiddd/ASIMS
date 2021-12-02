#import pydr
from os import name
from tkinter import *
import search 
from tkinter import ttk
import salerecord
import lowstockalert
import inventory
import sort

#from pydrive.auth import Googleau


#mainFrame=Frame()
screen=Tk()

#screen_main=Toplevel(screen)
#screen_main=Tk()


#mainFrame=Frame(screen_main)
#mainFrame.grid(row=0,column=1,rowspan=6,columnspan=2)

filepath="inventory_file.txt" 
mainscreenopen=0#check if main screen of program already open, 0 not open, 1 is open

#global searchedresults
#searchredesults=[""]*search.searchsize
searchedresults=[""]*4

global login_state
login_state=""
global table



def clear_screen():
    
    for widgets in mainFrame.winfo_children():
      widgets.destroy()

def create_user():  
    print("create new user account")   
    reg_username=username.get()
    reg_password=password.get()
    file3=open("login_info.txt","a")
    file3.write("\n"+reg_username+","+reg_password)
    file3.close()
    loggg.configure(text="User created Sucessfully")
    loggg.pack()

    username_entered.delete(0,END)#clears the text that was input
    password_entered.delete(0,END)



def login_screen():##first screen that pops up
    #global screen
    
    screen.geometry("300x300")
    screen.title("ASIMMS")
    screen.resizable(width=False,height=False)

    global login_state
    login_state=""
    global username
    username=StringVar()
    global password
    password=StringVar()
    global username_entered
    global password_entered
    global login_button
    global loggg
    
    Label(screen, text="Enter Credentials").pack()
    Label(screen,text="Username").pack()
    username_entered=Entry(screen, textvariable=username)
    username_entered.pack()
    Label(screen,text="Password").pack()
    password_entered=Entry(screen,textvariable=password)
    password_entered.pack()
    Label(screen, text="").pack()
    login_button= Button(text="Login",height=2,bg="lightgrey",activebackgroun="green",activeforeground="red",width="20",command=login).pack()
    Label(screen,height=2, text="").pack()
    Button(text="Create User",height=2,bg="lightgrey",width="20",command=create_user).pack()
    Label(screen, text="").pack()
    loggg=Label(screen, text="")
    
    
    screen.mainloop()#show screen

def login():    #check input against file to login
    global login_state
    #global mainscreenopen
    global mainscreenopen


    username_data=username.get()
    password_data=password.get()
    file=open("login_info.txt","r")
    #credential=file.readline()
    #credentials=credential.split(',')
    credential=file.readlines()
    print("usernamedata: "+username_data)
    print("passworddata: "+password_data)
    
 
    #result=Label(screen, text="Logged In").pack()
    #Label(screen, text=login_state).pack()
    
    for i in range(len(credential)):
        
        credentials=credential[i].split(',')
        credentials[1]=credentials[1].replace('\n','')#remove the newline character from end of string
        if username_data==credentials[0] and password_data==credentials[1] and mainscreenopen==0 :#//check password againts file working
            login_state="logged in"
            loggg.configure(text=login_state)
            loggg.pack()
            #print(login_state)
            open_program()
            mainscreenopen=1

        elif i>=len(credential)-1:
            
            login_state="Login Failed"
            loggg.configure(text=login_state)
            loggg.pack()
            #print(login_state)

    username_entered.delete(0,END)#clears the text that was input
    password_entered.delete(0,END)
    #file.close()





def manageInventory():
    clear_screen()

    print("Manage Inventory")

    mainFrame.grid(row=0,column=1,columnspan=2,rowspan=6)
    
    global var_name
    global var_brand
    global var_type
    global var_price
    global var_qty
    global var_reorderlvl

    global namevar
    global brandvar
    global typevar
    global pricevar
    global qtyvar
    global reoderlvlvar 
    global additem_
    global removeitem_
    
    global removeIDvar
    global var_removeID

    var_name=StringVar()
    var_brand=StringVar()
    var_type=StringVar()
    var_price=StringVar()
    var_qty=StringVar()
    var_reorderlvl=StringVar()
    var_removeID=StringVar()

 
    
    
    Label(mainFrame, text="Name").grid(row=0,column=1)
    namevar=Entry(mainFrame,textvariable=var_name).grid(row=0,column=2)
    Label(mainFrame, text="Brand").grid(row=1,column=1)
    brandvar=Entry(mainFrame,textvariable=var_brand).grid(row=1,column=2)
    Label(mainFrame, text="Type").grid(row=2,column=1)
    typevar=Entry(mainFrame,textvariable=var_type).grid(row=2,column=2)
    Label(mainFrame, text="Price").grid(row=3,column=1)
    pricevar=Entry(mainFrame,textvariable=var_price).grid(row=3,column=2)
    Label(mainFrame, text="Quantity").grid(row=4,column=1)
    qtyvar=Entry(mainFrame,textvariable=var_qty).grid(row=4,column=2)
    Label(mainFrame, text="Reorder Level").grid(row=5,column=1)
    reoderlvlvar=Entry(mainFrame,textvariable=var_reorderlvl).grid(row=5,column=2)
    additem_=Label(mainFrame, text="")

    Button(mainFrame, text="Add Item",bg="dark grey",command=intermed_addinventory).grid(row=6,column=1,pady=20)

    removeIDvar=Entry(mainFrame,textvariable=var_removeID).grid(row=7,column=2,pady=50,padx=30)
    Button(mainFrame, text="Remove Item",bg="dark grey",command=intermed_removeinventory).grid(row=7,column=1,pady=20)
    removeitem_=Label(mainFrame, text="")
    


def intermed_addinventory():
    global additemresult
    #global additem_
    additemresult=inventory.additem(var_name.get(),var_brand.get(),var_type.get(),float(var_price.get()),int(var_qty.get()),int(var_reorderlvl.get()))
    additem_.configure(text=additemresult)
    additem_.grid(row=6,column=2)

def intermed_removeinventory():
    if var_removeID.get().isdigit():
        removemessage=inventory.removeitem(int(var_removeID.get())) 
    removeitem_.configure(text=removemessage)
    removeitem_.grid(row=8, column=1,pady=30)




def displayInventory():
    inventory_list = []
    inventory_listli = []
    with open('inventory_file.txt','r') as f:
        inventory_list = f.readlines()
        for x in inventory_list:
          xsplit = x.rstrip("\n").split(",")
          inventory_listli.append(xsplit)
    print ("Would you like to sort the inventory listing?")
    while True:
        answer = int(input("1. Yes  |  2. No\n"))
        if answer == 1:
            print("How would you like to sort the inventory listing?")
            while True:
                sortby = int(input("1. Name  | 2. Brand  | 3. Type  | 4. Quantity  | 5. ID\n"))
                if sortby == 1:
                    inventory_listli.sort(key=sort.sortName)
                    print("ID Name Brand Type  Price Qty Reorder Level")
                    for i in inventory_listli:
                        print(i)
                    break
                if sortby == 2:
                    inventory_listli.sort(key=sort.sortBrand)
                    print("ID Name Brand Type  Price Qty Reorder Level")
                    for i in inventory_listli:
                        print(i)
                    break    
                if sortby == 3:
                    inventory_listli.sort(key=sort.sortType)
                    print("ID Name Brand Type  Price Qty Reorder Level")
                    for i in inventory_listli:
                        print(i)
                    break
                if sortby == 4:
                    inventory_listli.sort(key=sort.sortQuantity)
                    print("ID Name Brand Type  Price Qty Reorder Level")
                    for i in inventory_listli:
                        print(i)
                    break
                if sortby == 5:
                    inventory_listli.sort(key=sort.sortID)
                    print("ID Name Brand Type  Price Qty Reorder Level")
                    for i in inventory_listli:
                        print(i)
                    break
                print("Invalid option chosen, please try again.\n")
            break
        if answer == 2:
            print("ID Name Brand Type  Price Qty  Reorder Level")
            for i in inventory_listli:
                print(i)
            break
        print("Invalid option chosen, please try again.\n")

def inventoryReport():   
    print("Inventory Report")

def searchInventory():
    
    clear_screen()
    #global mainFrame
    #mainFrame=Frame(screen_main)
    mainFrame.grid(row=0,column=1,columnspan=2,rowspan=6)

    global IDsearchentry
    global IDsearchvar
    IDsearchvar=StringVar()

    global namesearchentry
    global namesearchvar
    namesearchvar=StringVar()
       
    global brandsearchentry
    global brandsearchvar
    brandsearchvar=StringVar()

    global typesearchentry
    global typesearchvar
    typesearchvar=StringVar()

    IDsearchentry=Entry(mainFrame,textvariable=IDsearchvar)
    IDsearchentry.grid(row=0,column=2,padx=0)

    namesearchentry=Entry(mainFrame,textvariable=namesearchvar)
    namesearchentry.grid(row=1,column=2,padx=0)
    
    brandsearchentry=Entry(mainFrame,textvariable=brandsearchvar)
    brandsearchentry.grid(row=2,column=2,padx=0)

    typesearchentry=Entry(mainFrame,textvariable=typesearchvar)
    typesearchentry.grid(row=3,column=2,padx=0)
    
    
    #brandsearch_data=brandsearchvar.get()
    #typesearch_data=typesearchvar.get()
    
    #print("namesearch_data: "+namesearch_data)
    Button(mainFrame, text="SearchbyID",bg="dark grey",command=intermed_searchbyID).grid(row=0,column=1,pady=20)
    Button(mainFrame, text="SearchbyName",bg="dark grey",command=intermed_searchbyname).grid(row=1,column=1,pady=20)
    Button(mainFrame, text="SearchbyBrand",bg="dark grey",command=intermed_searchbybrand).grid(row=2,column=1,pady=20)
    Button(mainFrame, text="SearchbyType",bg="dark grey",command=intermed_searchbytype).grid(row=3,column=1,pady=20)
    
    
    frame1=Frame(mainFrame,bg="black")
    frame1.grid(row="4",column=1,columnspan=2, rowspan=3)

    #Label(screen, text="Enter Credentials").pack()
    #Label(frame1, text="Enter Credentials").pack()
    
    style=ttk.Style()
    style.theme_use('clam')   
    global table
    table=ttk.Treeview(frame1, column=("ID","Name","Brand","Type","Price","Quantity","Reorder Level"),show='headings',height=8)
    table.column("# 1", anchor=CENTER,width=150)
    table.heading("# 1", text="ID")
    table.column("# 2", anchor=CENTER,width=250)
    table.heading("# 2", text="Name")
    table.column("# 3", anchor=CENTER,width=150)
    table.heading("# 3", text="Brand")
    table.column("# 4", anchor=CENTER,width=150)
    table.heading("# 4", text="Type")
    table.column("# 5", anchor=CENTER,width=150)
    table.heading("# 5", text="Price")
    table.column("# 6", anchor=CENTER,width=150)
    table.heading("# 6", text="Quantity")
    table.column("# 7", anchor=CENTER,width=150)
    table.heading("# 7", text="Reorder Level")
    
    table.pack()

    

    #table.grid(row=3)
    #print("The search button click works")
    #searched=search.searchbyname("Nissan",filepath)
    #for i in searched:
    #    print(i)    
#.......................................

def intermed_searchbyID():
    cleartable(table)
    global searchedresults
    global filepath
    IDsearch_data=IDsearchvar.get()
    print("IDsearch_data: "+IDsearch_data)
    searchedresults=search.searchbyID(IDsearch_data,filepath)
    print(searchedresults)
    if searchedresults is not None:
        for i in range(len(searchedresults)):
            tabledata=searchedresults[i].split(',')
            table.insert('', 'end', text="1", values=(tabledata[0],tabledata[1],tabledata[2],tabledata[3],tabledata[4],tabledata[5],tabledata[6]))



def intermed_searchbyname():
    cleartable(table)
    global searchedresults
    global filepath
    namesearch_data=namesearchvar.get()
    print("namesearch_data: "+namesearch_data)
    searchedresults=search.searchbyname(namesearch_data,filepath)
    print(searchedresults)
    if searchedresults is not None:
        for i in range(len(searchedresults)):
            tabledata=searchedresults[i].split(',')
            table.insert('', 'end', text="1", values=(tabledata[0],tabledata[1],tabledata[2],tabledata[3],tabledata[4],tabledata[5],tabledata[6]))


def intermed_searchbybrand():
    cleartable(table)
    global searchedresults
    global filepath
    brandsearch_data=brandsearchvar.get()
    print("brandsearch_data: "+brandsearch_data)
    searchedresults=search.searchbybrand(brandsearch_data,filepath)
    print(searchedresults)
    if searchedresults is not None:
        for i in range(len(searchedresults)):
            tabledata=searchedresults[i].split(',')
            table.insert('', 'end', text="1", values=(tabledata[0],tabledata[1],tabledata[2],tabledata[3],tabledata[4],tabledata[5],tabledata[6]))


def intermed_searchbytype():
    cleartable(table)
    global searchedresults
    global filepath
    typesearch_data=typesearchvar.get()
    print("typesearch_data: "+typesearch_data)
    searchedresults=search.searchbytype(typesearch_data,filepath)
    print(searchedresults)
    if searchedresults is not None:
        for i in range(len(searchedresults)):
            tabledata=searchedresults[i].split(',')
            table.insert('', 'end', text="1", values=(tabledata[0],tabledata[1],tabledata[2],tabledata[3],tabledata[4],tabledata[5],tabledata[6]))
            


def cleartable(tablevar):
    for i in tablevar.get_children():
        tablevar.delete(i)
    return tablevar    


#def clearsearchtabel():

#.........................................



def lowStockAlert():
    clear_screen()

    print("Low Stock Alert")
    global mainFrame
    global table

    mainFrame.grid(row=0,column=1,rowspan=6,columnspan=2)
    

    frame2=Frame(mainFrame,bg="black")
    frame2.grid(row=2,column=1,columnspan=2, rowspan=3)
    
    style=ttk.Style()
    style.theme_use('clam')   

    
    #table=cleartable(table)

    table=ttk.Treeview(frame2, column=("ID","Name","Brand","Type","Price","Quantity","Reorder Level"),show='headings',height=8)
    table.column("# 1", anchor=CENTER,width=150)
    table.heading("# 1", text="ID")
    table.column("# 2", anchor=CENTER,width=250)
    table.heading("# 2", text="Name")
    table.column("# 3", anchor=CENTER,width=150)
    table.heading("# 3", text="Brand")
    table.column("# 4", anchor=CENTER,width=150)
    table.heading("# 4", text="Type")
    table.column("# 5", anchor=CENTER,width=150)
    table.heading("# 5", text="Price")
    table.column("# 6", anchor=CENTER,width=150)
    table.heading("# 6", text="Quantity")
    table.column("# 7", anchor=CENTER,width=150)
    table.heading("# 7", text="Reorder Level")

    
    table.pack()

    Button(mainFrame,text="Get Items Low on Stock",bg="grey",command=intermed_lowstock).grid(row=0,column=1,sticky='n')
    
    

def intermed_lowstock():
    #global table
    cleartable(table)
    lowstockitems=lowstockalert.lowStockAlert()
    print(lowstockitems)
    if lowstockitems is not None:
        for i in lowstockitems:
            tabledata=i
            table.insert('', 'end', text="1", values=(tabledata[0],tabledata[1],tabledata[2],tabledata[3],tabledata[4],tabledata[5],tabledata[6]))
    
    

def salesRecord():  #one of main button functions
    clear_screen()  
    global mainFrame
    
    global salesoptionentrybox
    global salesoptionentry
    global salesoptionvar
    
    salesoptionvar=StringVar()


    #mainFrame=Frame(screen_main)
    mainFrame.grid(row=0,column=1,rowspan=6,columnspan=2)
    Label(mainFrame,text="PAT'S AUTO SUPPLIES").grid(row=0,column=0,padx=400,sticky='n',columnspan=2)
    Label(mainFrame,text="Hello, Welcome to your Virtual Sales Assistant!").grid(row=1,column=0,sticky='n',columnspan=2)
    Label(mainFrame,text="Options: 1. Transactions  |  2. Monthly Revenue ").grid(row=2,column=0,sticky='n',columnspan=2)


    
    salesoptionentrybox=Entry(mainFrame,textvariable=salesoptionvar)
    salesoptionentrybox.grid(row=3,column=1)
    
    
    Button(mainFrame,text="Enter Option",bg="grey",command=intermed_salesoption).grid(row=3,column=0,sticky='n')

    #Label(screen_main)
    print("Sales Record")


def intermed_salesoption():   
    global monthvar
    global monthlyresults
    monthvar=StringVar()
    
    def intermed_calcmonthlyrevenue():
        monthlyresults= salerecord.calcMonthlyRevenue(monthvar.get())
        monthlylabel.configure(text="The Revenue for "+str(monthvar.get())+": $"+str(monthlyresults)) 
        monthlylabel.grid(row=5,column=1,pady=20)

    if(salesoptionvar.get() is not None and salesoptionvar.get() != ""):
        option=int(salesoptionvar.get())

        if  option == 1:
            #salerecord.main(int(salesoptionvar.get()))
            salesoptionentrybox.delete(0,END)#clear entry box
        elif option == 2:
            #salerecord.main(int(salesoptionvar.get()))
            salesoptionentrybox.delete(0,END)#clear entry box
            
            Entry(mainFrame,textvariable=monthvar).grid(row=4,column=1)
            Button(mainFrame, text="Enter Month",bg="grey",command=intermed_calcmonthlyrevenue).grid(row=4,column=0,sticky='s',pady=10)
            monthlylabel=Label(mainFrame,text="")

        

def backupData():
    print("Backup Data")


def open_program():#display main list of buttons
    screen_main=Toplevel()
    global mainFrame
    mainFrame=Frame(screen_main)
    screen_main.title("ASIMS")
    screen_main.geometry("1300x700")
    screen_main.resizable(width=False,height=False)
    components=["Manage Inventory","Display Inventory","Inventory Report","Search Inventory","Low Stock Check","Sales Record","Backup Data"]
    components_functionnames=[manageInventory,displayInventory,inventoryReport,searchInventory,lowStockAlert,salesRecord,backupData]
    gridx=0
    gridy=0
    #print(components_functionnames)
    for i in range(len(components)):
      #Button(screen_main,height=6,bg="lightgrey",activebackground="green",activeforeground="blue",width=20,text=components[i],command=components_functionnames[i]).grid(row=gridy, column=0)
      Button(screen_main,height=6,bg="lightgrey",activebackground="green",activeforeground="blue",width=20,text=components[i],command=components_functionnames[i]).grid(row=gridy, column=0)
      gridy+=1

      
    
#Button(text="Create User",height=2,bg="lightgrey",width="20",command=create_user).pack()


      
    


login_screen()

