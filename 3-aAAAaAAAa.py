import re
import os
from pickle import load, dump

def page_source_reader(url, start_at, end_at):
    import urllib.request
    urlHandle = urllib.request.urlopen(url)
    mess = urlHandle.read().decode()
    urlHandle.close()
    ## Crop the string to only include the text between the start and end points. ##
    mess_start=mess.find(start_at)+len(start_at)
    mess_end=mess[mess_start:].find(end_at)
    ## If the end point isn't found, just keep on til the end! ##
    if mess_end!=-1:
        mess_end+=mess_start
    mess=mess[mess_start:mess_end]
    return mess.replace("\n", "")

url='http://www.pythonchallenge.com/pc/def/equality.html'

## Load the source and save it if not already done. ##
if os.path.exists("equality.txt"):
    mess=load(open("equality.txt", "rb"))
else:
    mess = page_source_reader(url, "<!--", "-->")
    dump(mess, open("equality.txt", "wb"))

## Finally, examine the string! ##

mess_upper="".join([str(int(i.isupper())) for i in mess])
result=([mess[i.start():i.start()+9] for i in re.finditer("011101110", mess_upper)])
print("".join([i[4] for i in result]))
