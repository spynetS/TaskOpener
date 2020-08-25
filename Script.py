import webbrowser
path= "C:/Users/Elev/Desktop/Projects/TaskOpeningScript/urls.txt"

lines = open(path,"r")
website = input()

def NewSite():
        print("Write new url and shortcut")
        print("ex,www.example.com")
        newsite=input()
	
        if "," in newsite:
                print("you added "+newsite)
                file = open(path,"a")
                file.write(newsite+"\n")
                file.close()
        else:
                print("Syntax error")
                NewSite()

if website == "NEW":
	NewSite()

for line in lines:
	splittedline = line.split(',')[0]
	
	if splittedline==website: 
		webbrowser.open(line.split(',')[1])
lines.close()

input()
