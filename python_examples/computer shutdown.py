from tkinter import *
import  os
def res():
    os.system('sudo reboot')

def resti():
    os.system('sudo shutdown -r +20')

def logout():
    os.system('gnome-session-quit --logout --no-prompt')

def shutdown():
    os.system('sudo shutdown now')

root = Tk()
root.title('switch')
root.config(bg='#1C1C1C')
root.geometry('500x400')
res_butt = Button(root,text = 'Restart',font = ('Arial',20,'bold'),relief =RAISED,cursor = 'plus',bg='green',command=res)
res_butt.place(x= 160,y= 40,width= 200)

restime_butt = Button(root,text = 'Restart Time',font = ('Arial',20,'bold'),relief =RAISED,cursor = 'plus',bg='green',command=resti)
restime_butt.place(x= 160,y= 120,width= 200)

logout_butt = Button(root,text = 'Log Out',font = ('Arial',20,'bold'),relief =RAISED,cursor = 'plus',bg='green',command=logout)
logout_butt.place(x= 160,y= 200,width= 200)

shut_butt = Button(root,text = 'Shut Down',font = ('Arial',20,'bold'),relief =RAISED,cursor = 'plus',bg='green',command=shutdown)
shut_butt.place(x= 160,y= 280,width= 200)

root.mainloop()