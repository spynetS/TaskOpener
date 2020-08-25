import webbrowser, sys
path= "urls.txt"
run = True

def Show():
        file = open(path,"r")
        for line in file:
                print(line)
        Loop()

def NewSite():
        print("Write new url and shortcut")
        print("ex,www.example.com")
        newsite=raw_input()
        
        if newsite == "CANCEL":
                Loop()


        if "," in newsite:
                print("you added "+newsite)
                file = open(path,"a")
                file.write(newsite+"\n")
                file.close()
        else:
                print("Syntax error")
                NewSite()
def Loop():
        print("MAIN")
        print("Type HELP for help")
        lines = open(path,"r")
        website = raw_input()
        
        if website == "NEW":
        	NewSite()

        if website == "HELP":
                print("SHOW shows you your urls")           
                print("NEW takes you to the add window")           
                print("EXIT closes the program")
                print("CANCEL takes you back to the main window")           
           

        if website == "EXIT":
                sys.exit("Exited program")
        if website == "SHOW":
                Show()

        for line in lines:
        	splittedline = line.split(',')[0]
        	if splittedline==website: 
        		webbrowser.open(line.split(',')[1])

        	
        lines.close()
        Loop()

if __name__ == '__main__':
        Loop()