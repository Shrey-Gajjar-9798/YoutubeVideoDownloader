from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

folder_path =""

def openlocation():
    global folder_path
    folder_path = filedialog.askdirectory()
    if(len(folder_path)>1):
        locationError.config(text =folder_path,fg="green")

    else:
         locationError.config(text="Please Choose Folder !",fg="red")

def downloadVideo():
    choice=ytdchoices.get()
    url= ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt =YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True).last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else :
            ytdError.config(text="Paste link again !",fg="red")
    
    select.download(folder_path)
    ytdError.config(text="Download Completed !")




root = Tk()
root.title("YTD Downloader")
root.geometry("400x500")
#root.resizable(0,0)
root.columnconfigure(0,weight=11)

#ytd link label in gui
ytdLabel = Label(root,text="Enter the url of the video",font=("jost",15))
ytdLabel.grid()

#Entry box
ytdEntryVar = StringVar()
ytdEntry =Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#For Error Message
ytdError = Label(root,text="Error message",fg="red",font=("jost",10))
ytdError.grid()

#Save label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#button to save file
saveEntry = Button(root,width=20,bg="green",fg="white",text="Choose Path",command=openlocation)
saveEntry.grid()

#Error message file
locationError = Label(root,text="Error message of path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#choice box
choices = ["720","144p","Only Audio"]
ytdchoices =ttk.Combobox(root,values =choices)
ytdchoices.grid()

#download button
downloadbtn = Button(root,text="Download",width=20,bg="red",fg="white",command=downloadVideo)
downloadbtn.grid()

#download label
developerLabel = Label(root,text="Shrey Gajjar",font = ("jost",15))
developerLabel.grid()


root.mainloop()