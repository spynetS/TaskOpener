import webbrowser, sys ,os
from os import system, name 

try:
    f = open("urls.txt","w")
    f.write("go,www.google.com")

    # Do something with the file
except IOError:
        print("error")
finally:
    f.close()


path= "urls.txt"
run = True

def Show():
        try:
                file = open(path,"r")
                for line in file:
                        print(line)
                file.close()
        except:
                print("no urls")
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
def DeleteContentInFile():
        sourceFileWrite = open(path,"w")
        sourceFileWrite.write("")
        sourceFileWrite.close()
        print("deleteContent")

def Delete():
        print("Write shortcut to delete url")
        fileToDelete = raw_input()
        sourceFileReader = open(path, "r")        
        sourceFile = open(path, "a")        
        my_list = []

        if fileToDelete == "-cancel":
                Loop()
        if fileToDelete == "-help":
              Help()
        if fileToDelete == "-exit":
                sys.exit("Exited program")
        if fileToDelete == "-show":
                Show()
        
        for line in sourceFileReader:
                if(fileToDelete!=line.split(',')[0]):
                        my_list.append(line)

        sourceFileWrite = open(path,"w")
        sourceFileWrite.write("")
        sourceFileWrite.close()  

        for line in my_list:
                sourceFile.write(line)

        newFile.close()
        newFileReader.close()
        sourceFile.close()
        sourceFileReader.close()
        sourceFileWrite.close()
        print("end")
        #os.remove("new"+path)

        
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
        print("-delete take you to deleting window")  
        print("github link: https://github.com/spynetS/TaskOpener")  
        print("Program by Alfred Roos")  

def Loop():
        print("MAIN")
        print("Type -help for help")
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