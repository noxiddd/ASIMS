# INVOICE MODULE
# AUTHOR: RAIMONA GOWIE-ROBERTS(620119136)
# DATE: DECEMBER 1, 2021

from fpdf import FPDF
import datetime
      

def invoice(data_lst, total, item_no, cash, chg):
  now = datetime.datetime.now()
  current_date = now.strftime(" %a, %b %d, %Y - %H:%M:%S")
  opt = input("Enter customer's name for receipt --->  ")
  textfile = opt +".txt"
  pdf_file = opt +".pdf"
  f = open(textfile, "a") 
  print("--------------------------------------------------------------------------------\n")
  f.write("-------------------------------------------------------------------------------------\n")
  print(" PAT'S AUTO SUPPLIES LTD.\n EWARTON, ST. CATHERINE")
  f.write(" PAT'S AUTO SUPPLIES LTD.\n EWARTON, ST. CATHERINE\n")
  print(f"{current_date}")
  print("--------------------------------------------------------------------------------\n")
  f.write("------------------------------------------------------------------------------------\n")
  dataString = "\n"
  for data in data_lst:
    string = '       '.join(map(str, data))
    dataString = dataString + string + "\n"
  print(dataString)
  f.write(dataString)

  print("--------------------------------------------------------------------------------")
  f.write("____________________________________________________________________________________\n")
  print("TOTAL ITEM(S): {:d}".format(item_no))
  f.write("TOTAL ITEM(S): {:d}".format(item_no)+ "\n")
  print("TOTAL: ${:.2f}".format(total))
  f.write("TOTAL: ${:.2f}".format(total)+ "\n")
  print("CASH RECEIVED: ${:.2f}".format(cash))
  f.write("CASH RECEIVED: ${:.2f}".format(cash)+ "\n")
  print("CHANGE: ${:.2f}".format(chg))
  f.write("CHANGE: ${:.2f}".format(chg)+ "\n")

  print("--------------------------------------------------------------------------------\n")
  f.write("--------------------------------------------------------------------------------------\n")

  print ("Receipt")
  f.write("*Receipt*\n")
  f.write(str(current_date) + "\n")
  print("--------------------------------------------------------------------------------\n")
  f.write("--------------------------------------------------------------------------------------\n")

  print("Thank you for shopping with us! Come Again!\n\n")
  f.write("THANK YOU FOR SHOPPING WITH US! COME AGAIN!\n\n")
  f.close()

  pdf = FPDF()   
  pdf.add_page()
  pdf.set_font("Arial", size = 12)

  f = open(textfile, "r")
 
  for x in f:
      pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
  
  pdf.output(pdf_file)  
  
#END OF MODULE