from tkinter import *  #making graphical user interface
from tkinter import ttk  #for combo box
from deep_translator import GoogleTranslator   #making translation

#main functional workflow
def change(text,src,dest):
    trans = GoogleTranslator(source=src, target=dest).translate(text)
    return trans

def data():
    s = comb_sour.get()
    d = comb_dest.get()
    masg = sour_textbox.get(1.0,END)
    textget = change(masg,s,d)
    des_textbox.delete(1.0,END)
    des_textbox.insert(END,textget)

#making the main graphical user interface   
root = Tk()
root.title('Translator')
root.geometry("700x700")
root.config(bg ='#242424')
root.resizable(False,False)

#main title
lab_text =Label(root, text ='Translator', font=('Time New Roman',20,'bold'),fg='yellow',bg='#242424',relief=RAISED)
lab_text.place(x=280,y=20,height=30,width=150,)
frame = Frame(root).pack(side= BOTTOM)

#main source text label and text box
sour_text =Label(root, text ='source text:', font=('Time New Roman',20,'bold'),fg='yellow',bg='#242424')
sour_text.place(x=10,y=60,height=30,width=160,)
sour_textbox = Text(frame,font=('Time New Roman',20,),wrap=WORD)
sour_textbox.place(x=20,y=100,height=200,width=660)
#operating the translations
languages = GoogleTranslator().get_supported_languages()

#option for the languages
comb_sour = ttk.Combobox(frame,values=languages)
comb_sour.place(x=40,y=310,height=40,width=100)
comb_sour.set('English')

#operating the whole function
button = Button(frame,text = 'Translate',relief=RAISED, bg='red',command=data)
button.place(x=290,y=310,height=40,width=100)

#translated languages option
comb_dest = ttk.Combobox(frame,values=languages)
comb_dest.place(x=560,y=310,height=40,width=100)
comb_dest.set('Bangla')

#translated text labeling
des_text =Label(root, text ='Destination text:', font=('Time New Roman',20,'bold'),fg='yellow',bg='#242424')
des_text.place(x=10,y=360,height=30,width=220)

#translated text will show there
des_textbox = Text(frame,font=('Time New Roman',20,),wrap=WORD)
des_textbox.place(x=20,y=400,height=200,width=660)

root.mainloop()