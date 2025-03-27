from tkinter import *
from speedtest import Speedtest
import threading

def speedchek():
    sp = Speedtest()
    sp.get_best_server()
    down = f"{round(sp.download() / 10 ** 6, 3)} Mbps"
    up = f"{round(sp.upload() / 10 ** 6, 3)} Mbps"
    dspval.config(text=down)
    uspval.config(text=up)

thread = threading.Thread(target=speedchek)
thread.start()
#for graphical user interface
root = Tk()
root.title('Internet speed Test')
root.config(bg='#1C1C1C')
root.geometry('500x300+710+390')
root.resizable(False,False)

#programme name
inst = Label(root,text='Internet speed test',font=('Arial',20,'bold'),bg='black',fg='cyan',relief=SUNKEN)
inst.place(x= 120,y= 30)

# label donwload speed
dsp = Label(root,text='Download speed',font=('Arial',20,'bold'),bg='black',fg='cyan')
dsp.place(x= 20,y= 100)
#value of the download speed
dspval = Label(root,text='00',font=('Arial',20,'bold'),bg='white',fg='black')
dspval.place(x= 40,y= 150,width=170)

#label upload speed
usp = Label(root,text='Upload speed',font=('Arial',20,'bold'),bg='black',fg='cyan')
usp.place(x= 290,y= 100)
#value of the upload speed
uspval = Label(root,text='00',font=('Arial',20,'bold'),bg='white',fg='black')
uspval.place(x= 300,y= 150,width=170)

#making button that execute the whole programme
button = Button(root,text='Cheak Spead',font=('Arial',20,'bold'),relief=RAISED,fg='green',bg='orange',command=speedchek)
button.place(x= 150,y=220)

root.mainloop()

