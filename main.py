import os
import subprocess
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter.font as font
import sys
import time
import json
import requests



doj=tkinter.Tk()
ver="1.0.0"
verdate = "May 2020"

doj.title("DOJ FiveM Server Select")
doj.geometry("669x750")
doj.resizable(0, 0)
doj.configure(background="#232323")
txt= "DOJ FiveM Server Selection | System by: Mike S. & Alex M."




fivemdir=r"Select Your FiveM.exe!"


#with open("setting.txt","w") as f:
    #f.write("{}".format(fivemdir))


def resource_path(relative_path):
    try:
        base_path= sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

dojlogo=PhotoImage(file=resource_path('DOJRP.png'))
doj.iconbitmap(resource_path('dojrp.ico'))

global servertra
global servertra2
global ft1dir
global ft2dir

server1dir=" +connect server1.dojrp.com"
server2dir=" +connect server2.dojrp.com"
server3dir=" +connect server3.dojrp.com"
server4dir=" +connect server4.dojrp.com"
server5dir=" +connect server5.dojrp.com"
server6dir=" +connect server6.dojrp.com"
serverXdir=" +connect serverX.dojrp.com"
dojtraindir=" +connect dojtrain.dojrp.com"
ft1dir=" +connect training.dojrp.com"
ft2dir=" +connect training2.dojrp.com"




#Server Commands
def server1():
    server1 = "".join((fivemdir,server1dir))
    server="Server 1"
    subprocess.Popen(server1)


def server2():
    server2 = "".join((fivemdir,server2dir))
    server="Server 2"
    subprocess.Popen(server2)


def server3():
    server3 = "".join((fivemdir,server3dir))
    server="Server 3"
    subprocess.Popen(server3)


def server4():
    server4 = "".join((fivemdir,server4dir))
    server="Server 4"
    subprocess.Popen(server4)

def server5():
    server5 = "".join((fivemdir,server5dir))
    server="Server 5"
    subprocess.Popen(server5)

def server6():
    server6 = "".join((fivemdir,server6dir))
    server="Server 6"
    subprocess.Popen(server6)

def serverx():
    serverx = "".join((fivemdir,serverXdir))
    server="Server X"
    subprocess.Popen(serverx)


def servertra():
    servertra = "".join((fivemdir,ft1dir))
    server="The FTO Training Server 1"
    subprocess.Popen(servertra)


def servertra2():
    servertra2 = "".join((fivemdir,ft2dir))
    server="The FTO Training Server 2"
    subprocess.Popen(servertra2)

def dojtrain():
    dojtrain = "".join((fivemdir,dojtraindir))
    server="The After Recruit Training/Testing Server"
    subprocess.Popen(dojtrain)


#Info Box
def infobox():
    infobox=messagebox.showinfo("DOJ FiveM Server Select","System by: Mike S. & Alex M.")

def filegrab():
    global fivemdir
    f=open("settings.txt","r")
    if f.mode == 'r':
        contents = f.read()
        if contents =="":
            fivemdir="Select Your FiveM.exe!"
        else:
            fivemdir=contents

#File Input
def fileinput():
    global fivemdir
    doj.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("executeable files","*.exe"),("all files","*.*")))
    fivemdir=doj.filename
    loadall()
    hideall()
    if os.path.exists('settings.txt'):
        os.remove('settings.txt')

    f=open("settings.txt","w+")
    f.write(fivemdir)



#Fonts
myFont = font.Font(family='Nunito',weight="bold")
secFont = font.Font(family='Nunito',weight="bold")
triFont = font.Font(family='Nunito',weight="normal")

#Further Information
version=Label(doj,text="V"+ver, bg="#232323", fg="grey")
version.place(x=630,y=0)

spacer1=Label(doj,bg="#232323")
spacer1.pack()

logo=Label(doj,image=dojlogo, bd=0)
logo.pack()

#Get server count
list1 = requests.get("http://"+"158.69.254.53:3001"+"/players.json")
count1= str(len(list1.json()))

list2 = requests.get("http://"+"158.69.254.53:3002"+"/players.json")
count2= str(len(list2.json()))

list3 = requests.get("http://"+"158.69.254.53:3003"+"/players.json")
count3= str(len(list3.json()))

list4 = requests.get("http://"+"158.69.254.53:3004"+"/players.json")
count4= str(len(list4.json()))

list5 = requests.get("http://"+"158.69.254.53:3005"+"/players.json")
count5= str(len(list5.json()))

list6 = requests.get("http://"+"158.69.254.53:3006"+"/players.json")
count6= str(len(list6.json()))

listx = requests.get("http://"+"192.99.20.123:3010"+"/players.json")
countx= str(len(listx.json()))

listt1 = requests.get("http://"+"158.69.254.53:3051"+"/players.json")
countt1= str(len(listt1.json()))

listt2 = requests.get("http://"+"158.69.254.53:3052"+"/players.json")
countt2= str(len(listt2.json()))

listtd = requests.get("http://"+"158.69.254.53:3053"+"/players.json")
counttd= str(len(listtd.json()))



def refresh():
    hideall()
    loadall()



#To get around variable issues
settinginfo=Label(doj, bg="#232323", text="SETTINGS\n\nPlease select your FiveM application using the below selection button.\nThis will only be a '.exe' file!", fg="white",highlightbackground="white")
settinginfo['font'] = secFont
settinginfo.place(relx=.5,rely=.4,anchor="center")
directoryselection=Label(doj, bg="#232323", text=f"Current Directory:\n{fivemdir}", fg="white",highlightbackground="white")
directoryselection['font'] = triFont
directoryselection.place(relx=.5,rely=.55,anchor="center")
fileinput1=Button(doj,text="Select",width=10,height=1,command=fileinput,bg="#04b5bc",fg="white",relief="flat")
fileinput1['font'] = myFont
fileinput1.place(relx=.5,rely=.7,anchor="center")
global display
display=Label(doj, bg="#232323", text=f"{txt}", fg="white",highlightbackground="white")
display['font'] = triFont
display.pack(side="bottom")
#Buttons
def loadall():
    global button1
    button1=Button(doj,text=f"Server 1\n{count1}/32",width=25,height=3,command=server1,bg="#04b5bc",fg="white",relief="flat")
    button1['font'] = myFont
    button1.place(y=250,x=62)

    global button2
    button2=Button(doj,text=f"Server 2\n{count2}/32",width=25,height=3,command=server2,bg="#04b5bc",fg="white",relief="flat")
    button2['font'] = myFont
    button2.place(y=250,x=345)

    global button3
    button3=Button(doj,text=f"Server 3\n{count3}/32",width=25,height=3,command=server3,bg="#04b5bc",fg="white",relief="flat")
    button3['font'] = myFont
    button3.place(y=329,x=62)

    global button4
    button4=Button(doj,text=f"Server 4\n{count4}/32",width=25,height=3,command=server4,bg="#04b5bc",fg="white",relief="flat")
    button4['font'] = myFont
    button4.place(y=329,x=345)

    global button5
    button5=Button(doj,text=f"Server 5\n{count5}/32",width=25,height=3,command=server5,bg="#04b5bc",fg="white",relief="flat")
    button5['font'] = myFont
    button5.place(y=408,x=62)

    global button6
    button6=Button(doj,text=f"Server 6\n{count6}/32",width=25,height=3,command=server6,bg="#04b5bc",fg="white",relief="flat")
    button6['font'] = myFont
    button6.place(y=408,x=345)

    global buttonx
    buttonx=Button(doj,text=f"Server X\n{countx}/64",width=25,height=3,command=serverx,bg="#04b5bc",fg="white",relief="flat")
    buttonx['font'] = myFont
    buttonx.place(y=487,x=62)

    global buttont
    buttont=Button(doj,text=f"DOJTrain\n{counttd}/32",width=25,height=3,command=dojtrain,bg="#04b5bc",fg="white",relief="flat")
    buttont['font'] = myFont
    buttont.place(y=487,x=345)

    global Misc
    Misc=Label(doj,text="Misc. Servers",fg="white",bg="#232323")
    Misc['font'] = myFont
    Misc.place(y=590, x=282)

    global buttontra
    buttontra=Button(doj,text=f"Training 1 (FTO)\n{countt1}/32",width=25,height=3,command=servertra,bg="#04b5bc",fg="white",relief="flat")
    buttontra['font'] = myFont
    buttontra.place(y=625,x=62)

    global buttontra2
    buttontra2=Button(doj,text=f"Training 2 (FTO)\n{countt2}/32",width=25,height=3,command=servertra2,bg="#04b5bc",fg="white",relief="flat")
    buttontra2['font'] = myFont
    buttontra2.place(y=625,x=345)

    global settings1
    settings1=Button(doj,text="Settings",width=10,height=1,command=hideall,bg="#04b5bc",fg="white",relief="flat")
    settings1['font'] = myFont
    settings1.place(y=10,x=10)

    global refresh1
    refresh1=Button(doj,text="Refresh",width=10,height=1,command=refresh,bg="#04b5bc",fg="white",relief="flat")
    refresh1['font'] = myFont
    refresh1.place(y=50,x=10)


    settinginfo.place_forget()
    directoryselection.place_forget()
    fileinput1.place_forget()


def hideall():
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    buttonx.place_forget()
    buttont.place_forget()
    Misc.place_forget()
    buttontra.place_forget()
    buttontra2.place_forget()
    settings1.place_forget()
    refresh1.place_forget()
    settings2=Button(doj,text="Return Home",width=10,height=1,command=loadall,bg="#04b5bc",fg="white",relief="flat")
    settings2['font'] = myFont
    settings2.place(y=10,x=10)
    global settinginfo
    settinginfo=Label(doj, bg="#232323", text="SETTINGS\n\nPlease select your FiveM application using the below selection button.\nThis will only be a '.exe' file!", fg="white",highlightbackground="white")
    settinginfo['font'] = secFont
    settinginfo.place(relx=.5,rely=.4,anchor="center")
    global directoryselection
    directoryselection=Label(doj, bg="#232323", text=f"Current Directory:\n{fivemdir}", fg="white",highlightbackground="white")
    directoryselection['font'] = triFont
    directoryselection.place(relx=.5,rely=.55,anchor="center")
    global fileinput1
    fileinput1=Button(doj,text="Select",width=10,height=1,command=fileinput,bg="#04b5bc",fg="white",relief="flat")
    fileinput1['font'] = myFont
    fileinput1.place(relx=.5,rely=.62,anchor="center")



startconstant="ready"

if startconstant=="ready":
    loadall()
    filegrab()
    if fivemdir=="Select Your FiveM.exe!":
        hideall()

doj.mainloop()
