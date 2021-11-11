import urllib.request
import re
import pytube
from pytube import YouTube
import os 
from tkinter import *
from tkinter import messagebox
import re 




SAVE_PATH ="Desktop\\Downloaded Music"

def Ok():
  

    fileName =e3.get()
    
    
    if(fileName!=""):
        with open(fileName) as f: 
            lines = f.readlines()
        for line in lines: 
            myLine = (re.split(',',line))
            artist =myLine[0] 
            song = myLine[1]     
            search_keyword= artist+song
            search_keyword = search_keyword.replace(" ","+")
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            print("https://www.youtube.com/watch?v=" + video_ids[0])

            Link = "https://www.youtube.com/watch?v=" + video_ids[0]



            yt = YouTube(Link) 
            video = yt.streams.filter(only_audio=True).first()

            try: 
                out_file = video.download(SAVE_PATH)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            except: 
                print("Could not download")

        messagebox.showinfo("Success","Downloaded all songs from text file")
        
              
        




    else: 
        artist = e1.get()
        song = e2.get() 
        if(artist=="" and song==""):
            messagebox.showinfo("", "Fields can't be empty!")

        search_keyword= artist+song
        search_keyword = search_keyword.replace(" ","+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print("https://www.youtube.com/watch?v=" + video_ids[0])

        Link = "https://www.youtube.com/watch?v=" + video_ids[0]



        yt = YouTube(Link) 
        video = yt.streams.filter(only_audio=True).first()

        try: 
            out_file = video.download(SAVE_PATH)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

        except: 
            print("Could not download")

        print("Downloaded "+song+ " by " + artist)    

        messagebox.showinfo("Success","Downloaded "+song + " by "+ artist)


root = Tk() 
root.title("Download Music")
root.geometry("300x200")
global e1
global e2 
global e3
Label(root,text="Artist").place(x=10, y=10)
Label(root, text="Song Name").place(x=10, y = 40) 
Label(root, text = "File Name (optional)").place(x=10, y=70) 

e1 = Entry(root)
e1.place(x=140, y =10) 

e2 = Entry(root) 
e2.place(x=140,y=40) 

e3 = Entry(root) 
e3.place(x=140, y=70) 

Button(root, text="Submit!", command=Ok, height= 3, width=13).place(x=10, y=100) 
root.mainloop()