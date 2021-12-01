from datetime import date
from os import write

def logitem(name, qty,date):
    file = open('LogFiles.txt', 'a')
    file.write("Added Item: "+name+" "+str(qty)+" "+str(date)+"\n")
    file.close()
    return 1

def additem(name,brand,type,price,quantity,reorderLevel):
    d=date.today()
    print("Adding Inventory")
    print("================")
    #name,brand,type='','',''
    #price=0.00
    #quantity,reorderLevel=0,0
    num=1
    
    if (name =='' or brand =='' or type =='' or price ==0.00 or quantity ==0 or reorderLevel ==0):
        print("Missing infomation try again")
        num=0
        return "Missing infomation try again"
        
       

    #getting last id in the file
    file4=open("inventory_file.txt", "r") 
    line = len(file4.readlines())
    id=line+1

    #Adding New item to file, separated by ","
    file = open('inventory_file.txt', 'a')
    file.write( str(id)+ ',')
    file.write( name+ ',')
    file.write( brand+ ',')
    file.write( type+ ',')
    file.write( str(price)+ ',')
    file.write( str(quantity)+ ',')
    file.write( str(reorderLevel))
    file.write("\n")
    file.close()
    #Adding Chnages to log file
    num=logitem(name,quantity,d)
    #Sucesss Message
    if (num == 1):
        print("Sucess! New Item added to file")
        return "Sucess! New Item added to file"
    else:
        print("Error: Saving to Log failed")
        return "Error: Saving to Log failed"

def removeitem(idnum):
    print("Removing Item from Inventory")
    print("==================")
    #idnum= int(input("Enter the item id to remove from inventory: "))
     #read_file.close()

    read_file=open("inventory_file.txt",'r')
    lines = read_file.readlines()
    read_file.close()
       
    write_file=open('inventory_file.txt','w')
    write_file.write("")
    write_file.close()

    write_file=open('inventory_file.txt','a')
    for line in lines:
        attributes=line.split(",")
        if attributes[0].isdigit():
            if(int(attributes[0])!=idnum):
                write_file.write(line)
                
    write_file.close()        

    print("Success,item was removed from the inventory")
    return "Success,item was removed from the inventory"