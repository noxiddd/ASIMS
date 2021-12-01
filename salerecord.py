#SALE RECORD MODULE
#AUTHOR: RAIMONA GOWIE-ROBERTS
#DATE: DECEMBER 1, 2021

import datetime

#Function to access price and quantity data for each item in the inventory file and create a working sale record list
def sales_data(inventoryfile):
  sales_lst = []
  file = open(inventoryfile, 'r')
  for entry in file:
    i, n, b, t, p, q, r = entry.split(",")
    r = r.strip()
    sales_lst.append([int(i), n.lower(), int(q), int(p)])
  file.close()
  return sales_lst
  

#Function to check the presence of an item in sale record list
def checkItem(sales_database, item):
  for salerecord in sales_database:
    if salerecord[1] == item.lower():
      return 1
  else:
    return -1

#Function to check the presence of an item in sale record list based on ID
def checkItemID(sales_database, ID):
  for salerecord in sales_database:
    if salerecord[0] == ID:
      return 1
  else:
    return -1

#Function to retrieve price for an item based on ID
def findPrice(sales_database, item):
  c = checkItem(sales_database, item)
  if c == 1:
    for x in range(len(sales_database)):
      if sales_database[x][1] == item.lower():
        price = sales_database[x][3]
        return price
  else:
    return 0 
    
#Function to retrieve price for an item based on ID
def findPriceID(sales_database, ID):
  c = checkItemID(sales_database, ID)
  if c == 1:
    for x in range(len(sales_database)):
      if sales_database[x][0] == ID:
        price = sales_database[x][3]
        return price
  else:
    return 0

#Function to calculate price for item based on quantity using item name
def calcTotalPrice(sales_database, item, quantity):
  price = findPrice(sales_database, item)
  if price != 0:
    total_price = int(price) * quantity
    return total_price
  else:
    return -1
  
#Function to calculate price for item based on quantity using ID
def calcTotalPriceID(sales_database, ID, quantity):
  price = findPriceID(sales_database, ID)
  if price != 0:
    total_price = int(price) * quantity
    return total_price
  else:
    return -1

#Function to process sale transactions
def transaction():
  inventoryfile = "inventory_file.txt"
  sales_database = sales_data(inventoryfile) 

  #Function to record sales and store in the sale log file
  def logSales(price):
    salelog = open("salelog.txt", "a")
    now = datetime.datetime.now()
    sale_month = now.strftime("%b")
    salelog.write(sale_month + ", " + str(price) + "\n")
    salelog.close()
      
  total_price = 0 #Initializing price
  while (1):
  
    #TAKING ORDER 
    print("\nWELCOME TO TRANSACTION PROCESSING VIRTUAL ASSISTANT\n")
    c = int(input("\nChoose: 1. Taking Order | 2. Cashing Out | 3. Cancel\n"))
    if (c == 1): #Taking Order
      print("\nTAKING ORDER ************************\n")
      opt = int(input("Using: 1. Name | 2. ID -    "))
      #USING ITEM NAME
      if opt == 1:
        item = input("Enter the name of the item: ")
        check = checkItem(sales_database, item)
        if check == 1:
          qty = int(input("Enter the quantity: "))
          price = calcTotalPrice(sales_database, item, qty)
          if price != -1:
            print("Cost: $", price,".00")
            d = int(input("Enter the discount amount: "))
            total_price = total_price + (price - d)
            print("Item added to bill!\n")
          else:
            print("\nTransaction cannot be processed!\n\n")
            main()
        else:
          print("\nItem not found!\n\n")
          main()
      #USING ITEM ID 
      elif opt == 2:
        ID = int(input("Enter item ID: "))
        check = checkItemID(sales_database, ID)
        if check == 1:
          qty = int(input("Enter the quantity: "))
          price = calcTotalPriceID(sales_database, ID, qty)
          if price != -1:
            print("Cost: $", price,".00")
            d = int(input("Enter the discount amount: "))
            total_price = total_price + (price - d)
            print("Item added to bill!\n")
          else:
            print("\nTransaction cannot be processed!\n\n")
            main()
        else:
          print("\nItem not found!\n\n")
          main()
    
    #CASHING OUT              
    elif (c == 2): 
      print("\nCASHING OUT NOW ************************\n")
      print("Total Cost: $" + str(total_price) +"\n")
      if (total_price > 0):
        receive = int(input("Money Collected:    "))
        if receive >= total_price:
          change = receive - total_price
          print("Change:",float(change))
          logSales(total_price)
          print("\n+++++++++++ Transaction has been finalized. ++++++++++\n\n")
          main()
        else:
          print("Insufficent funds!Try Again")
          receive = int(input("Money Collected:    "))
          if receive >= price:
            change = receive - price
            print("Change: $",float(change))
            logSales(price)
            print("+++++++++++ Transaction has been finalized. +++++++++++\n\n")
            main()
      else:
        print("No on-going transaction found!\n\n")
        main()
    
    # EXITING TRANSACTION            
    elif (c == 3): 
      print("Exiting Transaction ! ! !\n\n")
      main()

    #INVALID OPTION          
    else:
      print("Invalid option. Try Again!\n\n")
      transaction()

#Function to calculate the monthly revenue
def calcMonthlyRevenue(month):
  print("\nWELCOME TO REVENUE PROCESSING VIRTUAL ASSISTANT\n")
  file = open("salelog.txt", "r")
  total_revenue = 0
  lst = []
  
  for entry in file:
    m, p = entry.split(", ")
    p = p.strip()
    lst.append([m, int(p)])
  file.close()

  cash = []
  for i in range(len(lst)):
    if lst[i][0] == month:
      a = lst[i][1]
      cash.append(a)
    else:
      pass
  mth = []
  
  for i in range(len(lst)):
    mth.append(lst[i][0])
  if month not in mth:
    print("No revenue found!")
    revenue = 0.0
    return revenue
  else:
    total_revenue = sum(cash)
    file1 = open("revenuelog.txt", "a")
    file1.write(month + ", " + str(total_revenue) +"\n")
    file1.close()
    print("\n\nRevenue log has been updated successfully!\n")
    print("The revenue for "+ month.upper()+ " is: $" + str(total_revenue)+ ".00\n")
    return total_revenue
    main()

#Main Function for Sales Record Requirement   
def main(c):
  print("PAT'S AUTO SUPPLIES\nEWARTON, ST.CATHERINE\nJAMAICA")
  now = datetime.datetime.now()
  current_date = now.strftime("%A, %B %d, %Y - %H:%M:%S")
  print(f"{current_date}")
  while (1):
    print("\n\n Hello, Welcome to your Virtual Sales Assistant!\n\n")
    #c = int(input("1. Transactions  |  2. Monthly Revenue   |  3. Exit Application\n"))
    
    #TRANSACTIONS
    if c == 1:
      transaction()
    
    #REVENUE
    elif c == 2:
      #mth = input("Enter the month for which you which to calculate revenue:\nEnter- Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec\n")
      print("Option 2 Selected")
      #calcMonthlyRevenue(mth)
      
    #EXITING APPLICATION
    elif c == 3:
            print("Exiting Sales Application\n\n")
            quit()
    
    #INVALID OPTION
    else:
      print("Invalid Option! Try Again!\n")
      main()

#main()

#Generate and print receipts

