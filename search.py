
#Module to search the inventory file and return items matching search


#folderpath="C:\\Users\\JD039274\\Downloads\\UWI_2021\\ASIMMS\\"
filepath="inventory_file.txt"    

#searchsize=7
#searchresults=[""]*searchsize

lastline=0#last line searched in file

#prevent_recur=0



def removeemptyresults(searchresults):
    while "" in searchresults:   
        searchresults.remove("")
    return searchresults    

def searchbyID(searchstr,filepath):
  if(searchstr!="" and searchstr is not None and isinstance(searchstr,str)):  
    return searchby(searchstr,0,filepath)
    

def searchbyname(searchstr,filepath):
    if(searchstr!="" and searchstr is not None and isinstance(searchstr,str)):  
        return searchby(searchstr,1,filepath)
        

def searchbybrand(searchstr,filepath):
    if(searchstr!="" and searchstr is not None and isinstance(searchstr,str)):  
        return searchby(searchstr,2,filepath)

def searchbytype(searchstr,filepath):
    if(searchstr!="" and searchstr is not None and isinstance(searchstr,str)):
        return searchby(searchstr,3,filepath)

#search batch, 0 for first batch, 1 for second batch etc
#search attribte, dtermine whether to search by ID, name, brand or type
def searchby(searchstr,searchattribute,filepath):#search batch is the batch of e.g. it returns the first 5 matches is one batch, 6-10 matches it batch 2
    #global searchsize
    searchsize=4
    global searchresults
    global prevent_recur
    linecount=0
    searchresultscount=0
    searchresults=[""]*searchsize
    resultscount=0
    #global searchedresults
    file1= open(filepath,"r")
    while True:   
       linecount=linecount+1
       global lastline
       row=file1.readline()#get 
       if not row:#exit loop when end of file reached
            break
       if (linecount>= lastline):
            rowlist=row.split(',')
            if searchstr.isdigit() and searchstr==rowlist[searchattribute]:
                searchresults[0]=row
                break

            elif rowlist[searchattribute].lower().find(searchstr.lower()) != -1:        
            
                searchresults[searchresultscount%searchsize]=row
                searchresultscount+=1
                #lastline=linecount+1
                if searchresultscount > searchsize-1:
                    lastline=linecount+1
                    print("\nLastline: "+str(lastline))
                    break
                
                #print(row)
                #print(searchresults[searchresultscount-1])
            #print(rowlist[1])     
    lastline=linecount+1
    print("\nLastline: "+str(lastline))
    searchresults=removeemptyresults(searchresults) 
    if searchresults==[]:
        lastline=0
        #searchby(searchstr,searchattribute,filepath)
        
        
    #print(searchresults)
    #print("Debug line")#debug line
    file1.close()
    
    return searchresults
    


#searched=searchbyname("Mits",filepath)
#for i in searched:
#    print(i)

#searched=searchbyname("Mits",filepath)
#for i in searched:
#    print(i)





#def searchbyname(searchstr,filepath):
#    filenames=os.listdir(filepath)
 #       for f in filenames:
#            if f.lower().find(searchstr.lower()) != -1:
#                foundfiles=f
#                print(f)
  