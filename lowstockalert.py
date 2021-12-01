lowstock_list = []
inventory_list = []
inventory_listli = []


#Function to determine whether items in the inventory fall within the parameters to be considered low in stock; also gives the option to record any additonal units of the item
def lowStockAlert():
    with open("inventory_file.txt", "r") as f:
        inventory_list = f.readlines()
        for x in inventory_list:
            xsplit = x.rstrip("\n").split(",")
            inventory_listli.append(xsplit)
        for i in inventory_listli:
            if i[5].isdigit() and i[6].isdigit():#check if it contains a number first
                if int(i[5]) <= int(i[6]):
                    print("Warning! ", i[1], " is currently low in stock!")
                    #print(
                    #   "Do you have additional stock that has not been reported?")
                    #answer = int(input("1. Yes  | 2. No"))
                    #if answer == 1:
                        #new_qty = input("How many additional units of ", i[1]," do you have?")
                        #self.quantity += new_qty
                        #lowstockalert(self)
                    #    return 0
                    #elif answer == 2:
                    lowstock_list.append(i)
    return lowstock_list


#Function to determine whether items that are currently marked as low in stock retain the parameters required to remain on the list
#def maintainlowlist(self):
#  for i in range(len(lowstock_list)):
#    if getquantity(self) > getReorderlevel(self):
#      lowstock_list.remove(self.name)
#  return lowstock_list


#Function to display the list of items that are currently low in stock
def displaylowlist():
    print("Warning! Low stock of the following! Reorder soon!")
    for i in lowstock_list:
        print(i)
