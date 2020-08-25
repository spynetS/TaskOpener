import webbrowser, sys ,os
from os import system, name 

path= "urls.txt"
run = True

def Show():
        file = open(path,"r")
        for line in file:
                print(line)
        file.close()

def NewSite():
        print("Write new url and shortcut")
        print("ex,www.example.com")
        newsite=raw_input()
        
        if newsite == "-cancel":
                Loop()
        if newsite == "-help":
              Help()
        if newsite == "-exit":
                sys.exit("Exited program")
        if newsite == "-show":
                Show()
        if newsite == "-clear":
                Clear()
      
        if "," in newsite:
                print("you added "+newsite)
                file = open(path,"a")
                file.write(newsite+"\n")
                file.close()
        else:
                print("Syntax error")
                NewSite()
def Delete():
        print("Write shortcut to delete url")
        fileToDelete = raw_input()
        lines = open(path, "r")
        newFile = open("new"+path,"a")
        for line in lines:
                if(fileToDelete!=line.split(',')[0]):
                        newFile.write(line)
        line.close()
        newFile.close()
        os.rename("new"+path,path)
        os.remove(path)
def Clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        Loop()
def Help():
        print("-show shows you your urls")           
        print("-new takes you to the add window")           
        print("-exit closes the program")
        print("-cancel takes you back to the main window")           
        print("-clear clears console")  

def Loop():
        print("MAIN")
        print("Type HELP for help")
        lines = open(path,"r")
        website = raw_input()
        
        if website == "-new":
        	NewSite()

        if website == "-help":
              Help()  
        if website == "-delete":
                Delete()          
   

        if website == "-exit":
                sys.exit("Exited program")
        if website == "-show":
                Show()
        if website == "-clear":
                Clear()

        for line in lines:
        	splittedline = line.split(',')[0]
        	if splittedline==website: 
        		webbrowser.open(line.split(',')[1])

        	
        lines.close()
        Loop()

if __name__ == '__main__':
        Loop()