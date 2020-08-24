import webbrowser
path= "C:/Users/Elev/Desktop/Projects/TaskOpeningScript/urls.txt"

lines = open(path,"r")
website = str(input())
#branch s

for line in lines:
	splittedline = line.split(',')[0]
	if splittedline==website: 
		webbrowser.open(line.split(',')[1])
lines.close()

input()