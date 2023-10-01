filename = "namestest.txt"

with open(filename) as f:
    names =[n.strip() for n in  f.readlines()]

ncs= [] # name and its count

for n in names:
    flgExists = False
    for nc in ncs:
        if nc[0] == n:
            nc[1] = nc[1] + 1
            flgExists = True
            break
    if not flgExists:
        ncs.append([n, 1])



print(len(names))
print(len(ncs))

ncsSortedByName = sorted(ncs, key=lambda nc: nc[0])
#ncsSortedByCount = sorted(ncs, key=lambda nc: nc[1])
#ncsSortedByName = ncs

#print(len(ncsSortedByName))
#print(len(ncsSortedByCount))


print("<HTML>")
print("<!doctype html><html lang=\"ja\"><head>	<meta charset=\"UTF-8\">	<title>Names</title></head>")
print("<BODY>")
print("<H1>Names</H1>")

for nc in  ncsSortedByName:
    #print("<A href=\"https://www.google.com/search?q="+nc[0]+"&tbm=isch&tbs=isz:l\" target=\"_blank\">"+nc[0]+"</A> : "+str(nc[1]))
    print(F"{nc[0]}&nbsp;({str(nc[1])})&nbsp;:&nbsp;")
    print(F"<A href=\"https://www.google.com/search?q={nc[0]}&tbm=isch&tbs=isz:l\" target=\"_blank\">Google</A>")
    print(F"&nbsp;/&nbsp; <A href=\"https://www.bing.com/images/search?q={nc[0]}&qft=+filterui:imagesize-wallpaper\" target=\"_blank\">Bing</A>")
    print("<BR>")

print("</BODY>")
print("</HTML>")
