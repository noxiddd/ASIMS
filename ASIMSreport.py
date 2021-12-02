from fpdf import FPDF
import tkinter 
from tkinter import *
import tkinter as tk

my_pdf = FPDF()
my_pdf.add_page()
my_pdf.set_font("Arial", size = 16)

InventoryFile = open ("Inventory.txt", "r+")
SalesFile = open("sales.txt", "r+")
def sel():
   selection = "You selected the option " + str(var.get())
   pdfindicate = "You selected Inventory, a pdf file will be generated." 
   print(str(var.get()))
   if var.get() == 1:
        label.config(text = pdfindicate)
        InventorySelectionReport()
   else:
       label.config(text = selection)
       SaleSelectionReport()

       
    
        
def InventorySelectionReport():
        #my_pdf.set_font("Arial", style = 'B', size = 20)
        my_pdf.cell(200, 10, txt = "ASIMS Inventory File Details", border = 1, ln = 1, align = "C")
        for each in InventoryFile:
            my_pdf.cell(200, 10, txt = each, ln = 1, align = "L")
        my_pdf.output("ASIMS Inventory Report.pdf")

def SaleSelectionReport():
     ws = tk.Tk()
     ws.geometry('300x300')
     ws.config(bg='#1FDE31')
     ws.title("Sales Report Generation")
     btn = Button(
    ws,
    text='OK',
    relief=SOLID,
    command= generateSalespdf
)
     month1_lab = Label(
    ws,
    text='Please enter the month you would you like to generate a pdf for: ',
    bg='#0f4b6e',
    fg='white',  
)
     month_tf = Entry(ws)
     month_tf.pack()
     month1_lab.pack()
     btn.pack()
     month = month_tf.get()
     my_pdf.cell(200, 10, txt = "ASIMS Sales File Details", border = 1, ln = 1, align = "C")
     for each in SalesFile:
                my_pdf.cell(200, 10, txt = each, border = 1, ln = 1, align = "C")
                generateSalespdf()
     
    
     
def generateSalespdf():
    my_pdf.output("ASIMS Sales Report.pdf")
        
        
    


root = Tk()
root.title("ASIMS Report Generation")
root.geometry("500x400")
var = IntVar()
R1 = Radiobutton(root, text="Inventory", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Monthly Sales Revenue", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )



label = Label(root)
label.pack()
root.mainloop()
