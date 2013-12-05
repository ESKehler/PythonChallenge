import urllib.request

def page_source_reader(url, start_at, nothing):
    urlHandle = urllib.request.urlopen(url)
    mess = urlHandle.read().decode()
    urlHandle.close()
    if mess!="Yes. Divide by two and keep going.":
        ## Crop the string to only include the text between the start and end. ##
        mess_start=mess.find(start_at)
        if mess_start!=-1:
            mess_start+=len(start_at)
        else:
            mess_start=0
        mess=mess[mess_start:]
    else:
        print (mess)
        mess=str((int(nothing)/2))
    return mess

url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing="12345"

nothings=[]


while nothing not in nothings:
    print(nothing)
    nothings+=[nothing]
    nothing = page_source_reader(url+nothing, "and the next nothing is ", nothing)
print(nothing)
print(nothings)
